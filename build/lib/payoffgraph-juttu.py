import numpy as np
import pandas as pd
import streamlit as st 
import plotly.express as px # interactive charts 
import plotly.graph_objects as go



def call_buy(strike,cp,bs,premium,quantity):
  pnl=[]
  # print(expiry_list)
  if cp=="CE" and bs=="B":
    for i in range(len(expiry_list)):
      x=max((expiry_list[i]-strike),0)
      pnl.append((x-premium)*quantity)
    pnl = [round(item) for item in pnl]

  elif cp=="CE" and bs=="S":
    for i in range(len(expiry_list)):
      x=max((expiry_list[i]-strike),0)
      pnl.append((premium-x)*quantity)
    pnl = [round(item) for item in pnl]

  elif cp=="PE" and bs=="B":
    for i in range(len(expiry_list)):
      x=max((strike-expiry_list[i]),0)
      pnl.append((x-premium)*quantity)
    pnl = [round(item) for item in pnl]

  elif cp=="PE" and bs=="S":
    for i in range(len(expiry_list)):
      x=max((strike-expiry_list[i]),0)
      pnl.append((premium-x)*quantity)
    pnl = [round(item) for item in pnl]

  return pnl





expiry_list=[]

def get_payoff(positions_list,start,end):

  
  i=start
  while(i<=end):
    expiry_list.append(i)
    i=i+1
  
  
  pnl_lists=[]
  
  for position in positions_list:
    # print(position)
    pnl_lists.append(call_buy(position[0],position[1],position[2],position[3],position[4]))
 
  
  
  
  final_pnllist=[]
  for i in range(len(pnl_lists[0])):
    final_pnllist.append(0)
  for list1 in pnl_lists:
    final_pnllist=np.add(list1,final_pnllist)
  # print(final_pnllist)
  
  p_indexes=[]
  n_indexes=[]
  j1=0
  k1=0
  for i in range(len(final_pnllist)):
    if final_pnllist[i]>=0:
      p_indexes.append([final_pnllist[i],j1,i])
      k1=k1+1
    else:
      n_indexes.append([final_pnllist[i],k1,i])
      j1=j1+1
  
  # print(p_indexes)
  # print(n_indexes)
  
  arr1=[]
  arr2=[]
  for e in p_indexes:
    arr1.append(e[1])
  for e in n_indexes:
    arr2.append(e[1])
  # print(arr1)
  # print(arr2)
  
  res1 = [*set(arr1)]
  res1.sort()
  res2 = [*set(arr2)]
  res2.sort()
  
  # print(res1,res2)
  
  depths = [[] for i in range(len(res1))]
  # print(depths)
  depths1 = [[] for i in range(len(res2))]
  # print(depths1)
  
  i2=0
  for e in res1:
    for e1 in p_indexes:
      if e==e1[1]:
        depths[i2].append([e1[0],e1[2]])
    i2=i2+1
  
  # print(depths)
  
  j2=0
  for e in res2:
    for e1 in n_indexes:
      if e==e1[1]:
        depths1[j2].append([e1[0],e1[2]])
    j2=j2+1
  
  
  xp_list=[[] for i in range(len(res1))]
  
  for e in xp_list:
    e.append([])
    e.append([])
    
  # print(xp_list)
  
  xn_list=[[] for i in range(len(res2))]
  for e in xn_list:
    e.append([])
    e.append([])
    
  # print(xn_list)
  
  i3=0
  for e in depths:
    for e1 in e:
      xp_list[i3][0].append(e1[0])
      xp_list[i3][1].append(expiry_list[e1[1]])
      
    i3=i3+1
  
  # print(xp_list)
  # print(len(xp_list))
  
  i4=0
  for e in depths1:
    for e1 in e:
      xn_list[i4][0].append(e1[0])
      xn_list[i4][1].append(expiry_list[e1[1]])
      
    i4=i4+1
  
  # print(xn_list)
  # print(len(xn_list))
  
  
  
  
  
  test_p=xp_list
  test_n=xn_list
  
  
  
  placeholder = st.empty()
  st.markdown("###Chart")
  
  fig = go.Figure(go.Scatter(x=test_p[0][1],y=test_p[0][0], mode='lines',fill='tozeroy', fillcolor='#d6fdd6',line=dict(color="#4caf50")))
  for e in test_p:
    fig.add_trace(go.Scatter(x=e[1], y=e[0], mode='lines', fill='tozeroy', fillcolor='#d6fdd6',line=dict(color="#4caf50")))
  
  
  for e in test_n:
    fig.add_trace(go.Scatter(x=e[1], y=e[0], mode='lines', fill='tozeroy', fillcolor='#ffcdd2',line=dict(color="#f44336")))
  
  
  
    
  # fig.update_traces(mode="markers+lines", hovertemplate=None)
  fig.update_layout(hovermode="x")
  
  fig.update_layout(
      hoverlabel=dict(
          font_size=15,
      )
  )
  
  fig.update_xaxes(showline=True, linewidth=2, linecolor='black',tickformat = "digit")
  fig.update_yaxes(showline=True, linewidth=2, linecolor='black',tickformat = "digit")
  
  fig.update_yaxes(zeroline=True, zerolinewidth=1, zerolinecolor='black')
  
  fig.update_xaxes(ticks="outside", tickwidth=1, tickcolor='black', ticklen=5)
  fig.update_yaxes(ticks="outside", tickwidth=1, tickcolor='black', ticklen=5)
  
  
  
  st.write(fig)



# positions_list=[[15600.00,"CE","S",2210.2,100],[15600,"PE","S",5,50],[15200,"CE","B",2573,50],[15800,"PE","B",6.4,50],[15400,"PE","S",5.1,50]]



# get_payoff(positions_list,15000,20700)
