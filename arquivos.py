import os 
import asyncio

class Arquivo:
    def __init__(self,path_to_organize,type_table) -> None:
        self.type_table = type_table
        self.path_to_organize = path_to_organize
        self.build_empty_result_sender()

    def build_empty_result_sender(self):
        self.result_sender = {}
        for i in self.type_table.keys():
            self.result_sender[i] = []

    def organize_files(self):
        for file in os.listdir(self.path_to_organize):
            for future_dir_name in self.type_table.keys():
                for type_of_file in self.type_table[future_dir_name]:
                    try:
                        if file.endswith(type_of_file):
                            self.result_sender[future_dir_name].append(file)
                            break
                    except:
                        self.result_sender[future_dir_name] = []
                        if file.endswith(type_of_file):
                            self.result_sender[future_dir_name].append(file)
                            break
        
        return self.result_sender
    
    def get_type_table(self):
        return self.type_table

    def clear_type_table(self):
        self.get_type_table = {}

    async def organize(self,key):
        try:
            for file in self.result_sender[key]:
                os.rename(f'{self.path_to_organize}//{file}',f'{self.path_to_organize}//{key}//{file}')
        except FileNotFoundError:
            try:
                os.mkdir(f'{self.path_to_organize}//{key}')
                await self.organize(key)
                
            except Exception as e:
                raise Exception(f'{e} has occured wich means we need more debugging')
                

    def build_async_file_list(self):
        async_list = []
        for key in self.type_table.keys():
            
            async_list.append(self.organize(key))
        return async_list

    async def organize_files_final(self):
        await asyncio.gather(*self.build_async_file_list())

    def run(self):
        self.organize_files()
        asyncio.run(self.organize_files_final())



if __name__=='__main__':
    arq_obj = Arquivo(r'/home/henrique/Documentos',{'pdf_files':['pdf'], 'slides_presentation':['odg','odp'],'programs':['py']})
    arq_obj.run()