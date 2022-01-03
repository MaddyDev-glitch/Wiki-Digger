from selenium import webdriver
import time
from rich.live import Live
import sys
from rich.table import Table
from rich.console import Console

console = Console()
options = webdriver.ChromeOptions()
options.add_argument('headless');
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
console.log(f"\r[yellow]1. Hop from a topic endlessly \n2. Find out number of hops to reach 'Philosophy'\nYour choice(1 / 2): ")
choice = input("            ")
keyword = input("Enter KEYWORD:")
url = 'https://en.wikipedia.org/wiki/'+keyword
driver.get(url)

check=True
# print("DEBUG:===============================\n\n\n")
i=1
j=1
escape=0;
visited_nodes = {''}
visited_list=['']

def generate_table() -> Table:
    if choice=='2':
        table = Table()
        table.add_column("# of Hops")
        table.add_column("Starting Node")
        table.add_column("Current Node")
        table.add_column("Status")
        table.add_column("Elapsed Time")
        for row in range(1):
            table.add_row(
                f"{len(visited_list)}",f"{keyword}",f"[red]{y}" if y!='Philosophy' else f"[green]{y}", f"[red]{status}" if status!='RUNNING' else f"[green]{status}", f" %.4s seconds " % (time.time() - start_time)
            )
        return table
    else:
        table = Table()
        table.add_column("# of tries")
        table.add_column("# of Unique Nodes")
        table.add_column("Current Node")
        table.add_column("Status")
        table.add_column("Elapsed Time")
        value=1
        for row in range(1):
            value = value+1
            table.add_row(
                f"{pings}", f"{len(visited_list)}",f"{y}", f"[red]{status}" if status!='RUNNING' else f"[green]{status}", f" %.4s seconds " % (time.time() - start_time)
            )
        return table
        

status='NOT RUNNING'
pings=0;
y=''
start_time = time.time()
if(choice=='1'):
    console.log(f"[yellow]\n\rHit CTRL+C to end the program\n");
while check==True:
    with Live(generate_table(), refresh_per_second=4) as live:
        while check==True:
            status='RUNNING'
            live.update(generate_table())
            try:   
                y = driver.find_element_by_xpath('//*[@id="firstHeading"]').text
                if choice=='2':
                    if 'Philosophy' == y:
                        live.update(generate_table())
                        sys.exit(0)
                if y not in visited_nodes:
                    visited_nodes.add(y)
                    visited_list.append(y)
                    i=1 
                    if(j!=1):
                        j=1
                elif escape==1:
                    escape=0
                    i=i+1
                # print('//*[@id="mw-content-text"]/div[1]/p['+str(i)+']/a[1]')
                pings=pings+1
                x =driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p['+str(i)+']/a['+str(j)+']').click()
                escape=1;
            except SystemExit:
                status='NOT RUNNING'
                print("FINAL PATH:")
                visited_list.remove('')
                print(visited_list)
                # time.sleep(1)
                live.update(generate_table())
                exit()
            except KeyboardInterrupt:
                status='NOT RUNNING'
                print("FINAL PATH:")
                visited_list.remove('')
                print(visited_list)
                # time.sleep(1)
                live.update(generate_table())
                exit()
            except:
                # print("\nERROR\n")
                if(i<11):
                    i=i+1
                else:
                    i=1
                    j=j+1
                    if(len(visited_list)==2 and visited_list[0]==''):
                        print("SORRY WIKIPEDIA PAGE FOR "+keyword+" DOESN'T EXIST")
                        exit()
                escape=0
# print("\n\n\nDEBUG:===============================")
