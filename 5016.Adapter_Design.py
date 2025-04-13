from time import sleep

class Xml():
    def __init__(self, xmldata: str):
        # protected 
        _xmldata = xmldata
        
    # public 
    def getXmldata(self):
        return _xmldata

class DataAnalytics_Tool():
    def __init__(self, argJSONdata: str):
        # protected
        _jsondata = argJSONdata
    
    def analyseData():
        print("⭕ Analysing data: ", self._jsondata)
        sleep(1)
        print("✅ Analysis completed.")

class Cliet():
    def processData(self, tool: DataAnalytics_Tool):
        tool.analyseData()



# client accessing the tool
if __name__ == "__main__":
    # sample xml data
    to_analyse_data_xml = Xml("!! Sample XML data !!")

    # passing xml data (adapter to make this compartible with the tool)
    analysis_tool = DataAnalytics_Tool(to_analyse_data_xml)
    
    # client analyzing the data
    client_xyz = Client()
    client_xyz.processData(analysis_tool)
    
    return