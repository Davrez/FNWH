o
    �Y�b�  �                   @   s�  d dl Z d dlmZ d dlmZmZ d dlZd dlmZ d dlZej�� Zd dl	Z	d dl
Z
d dlmZ d dlmZ e �d� e j�d�sIe �d� G d	d
� d
�Zed� ed� ed� eej� dej� �� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� eej� dej� �� ed� ee� ed� ed� eej� dej� �� ed� ed� ed� ed� e�d� ed� e�d� G dd
� d
�Zee
j�dk�rHed� eej� dej� �� e�d� ed� eej� dej� �� ed� ed� ed� ed� ed� ed� ed� ed � ed� ed!� e�d"� ed� ed� ed#� e�d� e
��  nVed� d dlmZ eed e d$���D ]Z!�q[ed� e�d� eej"� d%ej� �� e�d"� ed&� e#e
jd d'�Z$e$�%� Z&e$�'�  d(e
jd �(d)d� d* Z)e#e)d+�Z*e&D �]ZZ+z7d,e+�,� v �s�d-e+�,� v �r�e+�,� Z-nd,e+�,�  Z-e	�.� Z/e/j0e-dd.�Z1e1j2Z3e*�4e-d/ e5e1j6� d0 � W nx e	j7�y� Z8 zed0eje- ej d1 � W Y dZ8[8�q�dZ8[8w e	j9�y Z8 zeej� d2ej� �� W Y dZ8[8�q�dZ8[8w e	j:�y: Z8 zeej� d3ej� �� W Y dZ8[8�q�dZ8[8w e;�yR   e*�'�  ed4e) d0 � e�  Y nw e1j6d5k�rwzed0d6ej"d/e-e1j2d7 � W n e<�yv   ed8� Y nw e1j6d9k�r�zed0d:ej"d/e-e1j2d7 � W n e<�y�   ed8� Y nw e1j6d;k�r�ed0d<ej"e1j6d=e-e1j2d7 � e1j6d>k�r�zed0d?ej"d/e-e1j2d7 � W n e<�y�   ed8� Y nw e1j6d@k�r�zed0dAej"d/e-e1j2d7 � W �q� e<�y�   ed8� Y �q�w �q�ed� ed� eej"� dBej� �� ed� ed� edC� edDe) d0 � edC� ed� ed� ed� ed� ed� ed� ed� e*�'�  dS )E�    N)�tqdm)r   �trange)�colored)�HTTPAdapter)�Retry�clear�resultsc                   @   s4   e Zd ZdZdZdZdZdZdZdZ	dZ
dZd	Zd
S )�bcolors�[93m�[95m�[94m�[96m�[92m�[91m�[0m�[1m�[4mN)�__name__�
__module__�__qualname__�YELW�HEADER�OKBLUE�OKCYAN�OKGREEN�WARNING�FAIL�ENDC�BOLD�	UNDERLINE� r    r    �fnwh1.pyr	      s    r	   � a�  
::::::::::      ::::    :::      :::       :::      :::    :::
:+:             :+:+:   :+:      :+:       :+:      :+:    :+:
+:+             :+:+:+  +:+      +:+       +:+      +:+    +:+
:#::+::#        +#+ +:+ +#+      +#+  +:+  +#+      +#++:++#++
+#+             +#+  +#+#+#      +#+ +#+#+ +#+      +#+    +#+
#+#             #+#   #+#+#       #+#+# #+#+#       #+#    #+#
###             ###    ####        ###   ###        ###    ### zq
 _____ _____ _____ _____ _____ _____
|_____|NEW__|_____|_____|_____|_____|
|_____|_____|FREE_|NET__|SCAN_|TOOL_|zHeader ResponsezScanning ScriptzSimple User_modeZSTAY_____ETHICALzRunning F N W H @exactz==========================zVNOTE:For perfect results Use this scanner with zero internet bundles or subscriptions!zPlease Wait...g      �?zStarting Scanner�   c                   @   s0   e Zd ZdZdZdZdZdZdZdZ	dZ
d	Zd
S )r	   r   r   r   r   r
   r   r   r   r   N)r   r   r   r   r   r   r   r   r   r   r   r   r    r    r    r!   r	   P   s    �   u   ERROR⚠a,                                                                                                                                                                                                                                                                                                              zUSAGE:z
fnwh.py [Yourlist.txt]
z%
example: python3 fnwh.py mylist.txt
zh
>> NOTE: you need to save yourlist.txt or what ever you name it to this same directory as fnwh.py tool
z�
>> with your list in this same directory/folder copy the example above and remember to replace yourlist.txt with the file name you want to scan.
�   zPress enter to continueg     jAzSuccess!z  �rzresults/z../z_results.txtzw+zhttp://zhttps://)Ztimeout�:�
z Cant connect zOops Timeout!zGeneral Error!z
Results saved in : ��   z[6;39;40m[200]Zserverzserver not foundi4  z[6;39;40m[308]i.  z[6;39;40m[302]z : i-  z[6;39;40m[301]i�  z[6;39;40m[403]zDone!z9=========================================================z
 Your Results are saved in : )=�osr   r   �timeZ	termcolorr   ZdatetimeZtodayZnowZrequests�sysZrequests.adaptersr   Z$requests.packages.urllib3.util.retryr   �system�path�exists�makedirsr	   �printr   r   r   r   �sleep�len�argvr   �input�exit�range�int�ir   �open�f�	readlines�lines�close�replace�filename�out�line�stripZurlZSession�s�headr&   ZheadersZresponse�write�strZstatus_code�ConnectionError�eZTimeoutZRequestException�KeyboardInterrupt�KeyErrorr    r    r    r!   �<module>   s*  	



�










 ���
���� ��