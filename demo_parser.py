from demoparser2 import DemoParser

parser = DemoParser('test_demo.dem')       

df = parser.parse_events('bomb_planted')
