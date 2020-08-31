import tkinter as tk
import tkinter.ttk as ttk

#create label_input class from label and entry widgets
class label_input(ttk.Frame):

    def __init__(self,parent,input_var=tk.StringVar,label_text=None,*args,**kwargs):
        ttk.Frame.__init__(self,parent)
        self.label_arggs = {}
        self.imput_args = {}
        self.text_variable = input_var()
        
        if input_var and label_text:
            label_widget = ttk.Label(self,text=label_text)
            label_widget.grid(row=0,column=0)
            entry_widget = ttk.Entry(self,textvariable=self.text_variable)
            entry_widget.grid(row=1,column=0)

    def grid(self,row,column,padx=10,pady=10):
        super().grid(row=row,column=column,padx=padx,pady=pady)

#create the main applicaton class
class Application_window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("ogr2ogr-PostGIS")
        self.geometry("800x800")
        self.resizable(height=False,width=False)

class label_frame(ttk.Labelframe):
    def __init__(self,parent,text=None,border=2):
        ttk.Labelframe.__init__(self,parent,text=text)

#button class
class buttons(ttk.Frame):
    def __init__(self,parent):
        ttk.Frame.__init__(self,parent)
        self.button1 = ttk.Button(self,text="Confirm")
        self.button2 = ttk.Button(self,text="Reset")
        self.button1.grid(row=0,column=0,sticky=(tk.W+tk.E),padx=10)
        self.button2.grid(row=0,column=1,sticky=(tk.W+tk.E),padx=10)

if __name__ == "__main__":
    Mainwindow = Application_window()
    Mainwindow.columnconfigure(0,weight=1)
    #CODE FOR DATA SECTION

    Data_frame1  = ttk.Labelframe(Mainwindow,text="Data",height=200,width=800)
    Data_frame1.grid(row=0,column=0,padx=10,pady=10,sticky=(tk.W+tk.E))

    format_entry = label_input(Data_frame1,input_var=tk.StringVar,label_text="Format")
    format_entry.grid(row=0,column=0)
    source_entry = label_input(Data_frame1,input_var=tk.StringVar,label_text="Source")
    source_entry.grid(row=0,column=1)
    output_entry = label_input(Data_frame1,input_var=tk.StringVar,label_text="Output")
    output_entry.grid(row=0,column=2)
    extent_entry = label_input(Data_frame1,input_var=tk.StringVar,label_text="Extents")
    extent_entry.grid(row=1,column=0)
    Sql_entry = label_input(Data_frame1,input_var=tk.StringVar,label_text="SQL")
    Sql_entry.grid(row=1,column=1)
    fields_entry = label_input(Data_frame1,input_var=tk.StringVar,label_text="Fields")
    fields_entry.grid(row=1,column=2)
    #clear and reset buttons for the forms
    buttons_frame1 = buttons(Data_frame1)
    buttons_frame1.grid(row=1,column=4,sticky=(tk.W+tk.E+tk.S+tk.N))
    #CODE FOR LAYER CREATION SECTION

    Data_frame2  = ttk.Labelframe(Mainwindow,text="Layer Creation",height=200,width=800)
    Data_frame2.grid(row=1,column=0,padx=10,pady=10,sticky=(tk.W+tk.E))
    Geom_type_entry = label_input(Data_frame2,input_var=tk.StringVar,label_text="Geometry Type")
    Geom_type_entry.grid(row=0,column=0)
    Geom_name_entry = label_input(Data_frame2,input_var=tk.StringVar,label_text="Geometry Name")
    Geom_name_entry.grid(row=0,column=1)
    schema_entry = label_input(Data_frame2,input_var=tk.StringVar,label_text="Schema")
    schema_entry.grid(row=0,column=2)
    output_srs_entry = label_input(Data_frame2,input_var=tk.StringVar,label_text="Output SRS")
    output_srs_entry.grid(row=1,column=0)
    where_entry = label_input(Data_frame2,input_var=tk.StringVar,label_text="Where Phrase")
    where_entry.grid(row=1,column=1)
    spatial_index_entry = label_input(Data_frame2,input_var=tk.StringVar,label_text="Spatial Index")
    spatial_index_entry.grid(row=1,column=2)
    #clear and reset buttons
    buttons_frame1 = buttons(Data_frame2)
    buttons_frame1.grid(row=1,column=4,sticky=(tk.W+tk.E+tk.S+tk.N))

    #CODE FOR DATABSE OPTIONS
    Data_frame3  = ttk.Labelframe(Mainwindow,text="Database",height=200,width=800)
    Data_frame3.grid(row=2,column=0,padx=10,pady=10,sticky=(tk.W+tk.E))
 
    host_entry = label_input(Data_frame3,input_var=tk.StringVar,label_text="Host")
    host_entry.grid(row=0,column=0)
    username_entry = label_input(Data_frame3,input_var=tk.StringVar,label_text="Username")
    username_entry.grid(row=0,column=1)
    port_entry = label_input(Data_frame3,input_var=tk.StringVar,label_text="Port")
    port_entry.grid(row=0,column=2)
    dbname_entry = label_input(Data_frame3,input_var=tk.StringVar,label_text="Database name")
    dbname_entry.grid(row=1,column=0)
    password_entry = label_input(Data_frame3,input_var=tk.StringVar,label_text="Password")
    password_entry.grid(row=1,column=1)
    table_name_entry = label_input(Data_frame3,input_var=tk.StringVar,label_text="Table name")
    table_name_entry.grid(row=1,column=2)
    #clear and reset buttons
    buttons_frame1 = buttons(Data_frame3)
    buttons_frame1.grid(row=1,column=4,sticky=(tk.W+tk.E+tk.S+tk.N))

    Mainwindow.mainloop()

    

    


    

















































