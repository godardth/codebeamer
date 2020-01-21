class ProjectMixin:
    
    def getProjects(self):
        return self.get('/projects')
        
    def getProject(**kwargs):
        if not len(kwargs) == 1: 
            raise Exception('getProject method takes one argument in : name, id')
        elif kwargs.get('name', None):
            return self.get(f"/project/{kwargs['name']}")
        elif kwargs.get('id', None):
            return self.get(f"/project/{kwargs['id']}")
        else:
            raise Exception('getProject method takes one argument in : name, id')
