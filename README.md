# Python Practical Test
# Back-end development task: File Monitoring

1. Create venv
  - python -m venv cds_env
 
2. Activate env
    cds_env\Scripts\activate

3. install requeriments
    pip install -r requirement.txt

4. Update config.py

5. run script:
    python run.py
        OR
   to run each module separately:
    python file_monitor.py
    python file_writer.py
    
 --- Things can be improved:
 1 Read files into chunks(counting chunk with separate processes) then count for keyword for faster processing
 2 Error handling 

