import wx
from streamsets.sdk import ControlHub
from streamsets.sdk import Transformer
# 3770a813-d654-47b9-81d9-d3b16968d282
# eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJzIjoiMTM1N2U3MjQxYjIyMmVkMTg4MzEyN2Y4YTQwN2YxNDIzMjUzYzQ3YmU2NzY2ODIzNTNiODkzMTI5ZTc5M2NhM2I0Mzc4NjI4MWJkOTdjNDhkYzEzYWU4MjIxMzVkYjg5NTgxOTJmYjI2NzE3MDUyNGE5M2M2YTVlMTBhOWI2ZTgiLCJ2IjoxLCJpc3MiOiJldTAxIiwianRpIjoiMzc3MGE4MTMtZDY1NC00N2I5LTgxZDktZDNiMTY5NjhkMjgyIiwibyI6Ijc0NmVjOTA3LWYzNzYtMTFlYi1hZTJlLWFiNmJjNjA2M2I5NiJ9.
class TabOne(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Add components for the first tab
        label_credential_id = wx.StaticText(self, label="Credential ID:", pos=(20, 20))
        self.text_ctrl_credential_id = wx.TextCtrl(self, pos=(170, 20), size=(280, -1))
        
        label_token = wx.StaticText(self, label="Token:", pos=(20, 50))
        self.text_ctrl_token = wx.TextCtrl(self, pos=(170, 50), size=(280, -1))
        
        self.button_validate = wx.Button(self, label="Connect", pos=(20, 80))
        self.button_validate.Bind(wx.EVT_BUTTON, self.on_validate_click)
        
        label_execution_engine = wx.StaticText(self, label="Execution Engine:", pos=(20, 120))
        self.choices_execution_engine = ['Simon 5.5 SDC', 'Giuseppe 5.6 SDC']
        self.choice_execution_engine = wx.Choice(self, choices=self.choices_execution_engine, pos=(170, 120))
        
        self.button_select_engine = wx.Button(self, label="Select", pos=(380, 120))
        self.button_select_engine.Bind(wx.EVT_BUTTON, self.on_select_engine)
        
        label_select_deployment_id = wx.StaticText(self, label="Source Deployment ID:", pos=(20, 160))
        self.choices_deployment_id = ['Simon SDC 5.5 Deployment', 'Boris 5.5 AWS']
        self.choice_deployment_id = wx.Choice(self, choices=self.choices_deployment_id, pos=(170, 160))
        
        self.button_select_deployment_id = wx.Button(self, label="Select", pos=(380, 160))
        self.button_select_deployment_id.Bind(wx.EVT_BUTTON, self.on_select_deployment_id)
        
        self.result_text_ctrl = wx.TextCtrl(self, pos=(20, 200), size=(440, 140), style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL | wx.VSCROLL)
        
        # Set initial tab 1 welcome message
        welcome_message = "Welcome to StreamSets Deployment Duplicator\n"
        self.result_text_ctrl.SetValue(welcome_message)
        self.result_text_ctrl.SetInsertionPointEnd()  # Set cursor at the end

    def on_validate_click(self, event):
        # First validate UUIDs - see https://stackoverflow.com/questions/53847404/how-to-check-uuid-validity-in-python
        credential_id = self.text_ctrl_credential_id.GetValue()
        token = self.text_ctrl_token.GetValue()
        try:
            sch = ControlHub(credential_id=credential_id, token=token)
            # The statement executed successfully
            greeting = "Validation successful"
            # message = f"Welcome, {credential_id}!\nYour token: {token}"
            message = f"Welcome to the StreamSets Platform"
            self.result_text_ctrl.SetValue(f"{greeting}\n{message}\n")
        except Exception as e:
            # An exception occurred
            greeting = str(e)
            message = f"You must enter valid credentials: "
            self.result_text_ctrl.SetValue(f"{greeting}\n{message}" + str(e)+ "\n")

        self.result_text_ctrl.SetInsertionPointEnd()  # Set cursor at the end
        

    def on_select_engine(self, event):
        selected_engine = self.choice_execution_engine.GetString(self.choice_execution_engine.GetSelection())
        self.result_text_ctrl.AppendText(f"Selected Execution Engine: {selected_engine}\n")

    def on_select_deployment_id(self, event):
        selected_deployment_id = self.choice_deployment_id.GetString(self.choice_deployment_id.GetSelection())
        self.result_text_ctrl.AppendText(f"Selected Deployment ID: {selected_deployment_id}\n")

class TabTwo(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Add components for the second tab
        label_deployment_name = wx.StaticText(self, label="Deployment Name:", pos=(20, 20))
        self.text_name = wx.TextCtrl(self, pos=(150, 20), size=(300, -1))
        
        label_deployment_type = wx.StaticText(self, label="Deployment Type:", pos=(20, 50))
        deployment_choices = ["SELF", "EC2", "Azure"]
        self.choice_deployment_type = wx.Choice(self, choices=deployment_choices, pos=(150, 50))

        label_deployment_tags = wx.StaticText(self, label="Deployment Tags:", pos=(20, 80))
        self.text_tags = wx.TextCtrl(self, pos=(150, 80), size=(300, -1))
        
        label_engine_type = wx.StaticText(self, label="Engine Type:", pos=(20, 110))
        engine_type_choices = ["DC", "Tx"]
        self.choice_engine_type = wx.Choice(self, choices=engine_type_choices, pos=(150, 110))
        
        label_engine_version = wx.StaticText(self, label="Engine Version:", pos=(20, 140))
        engine_version_choices = ["5.4", "5.5"]
        self.choice_engine_version = wx.Choice(self, choices=engine_version_choices, pos=(150, 140))
        
        label_engine_labels = wx.StaticText(self, label="Engine Labels:", pos=(20, 170))
        # set engine labels tooltip
        label_engine_labels_tooltip = wx.ToolTip("Use comma separated strings")        
        label_engine_labels.SetToolTip(label_engine_labels_tooltip)
        self.text_engine_labels = wx.TextCtrl(self, pos=(150, 170), size=(300, -1))
        
        self.button_clone = wx.Button(self, label="Clone", pos=(20, 200))
        self.button_clone.Bind(wx.EVT_BUTTON, self.on_clone_click)
        
        self.result_text_ctrl = wx.TextCtrl(self, pos=(20, 240), size=(440, 140), style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL | wx.VSCROLL)
        
        # Set initial tab 2 welcome message
        welcome_message = "Enter the target deployment details, then press Clone"
        self.result_text_ctrl.SetValue(welcome_message)
        self.result_text_ctrl.SetInsertionPointEnd()  # Set cursor at the end
    
    def on_clone_click(self, event):
        deployment_name = self.text_name.GetValue()
        deployment_type = self.choice_deployment_type.GetString(self.choice_deployment_type.GetSelection())
        deployment_tags = self.text_tags.GetValue()
        engine_type = self.choice_engine_type.GetString(self.choice_engine_type.GetSelection())
        engine_version = self.choice_engine_version.GetString(self.choice_engine_version.GetSelection())
        engine_labels = self.text_engine_labels.GetValue()
        
        self.result_text_ctrl.SetValue(f"Deployment Name: {deployment_name}\n"
                                   f"Deployment Type: {deployment_type}\n"
                                   f"Deployment Tags: {deployment_tags}\n"
                                   f"Engine Type: {engine_type}\n"
                                   f"Engine Version: {engine_version}\n"
                                   f"Engine Labels: {engine_labels}")
        self.result_text_ctrl.SetInsertionPointEnd()  # Set cursor at the end of the output screen

        # clone execution code starts here...

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(500, 400))
        
        self.panel = wx.Panel(self)
        
        # Create a notebook with two tabs
        notebook = wx.Notebook(self.panel)
        tab_one = TabOne(notebook)
        tab_two = TabTwo(notebook)
        
        # Add the tabs to the notebook
        notebook.AddPage(tab_one, "Source Deployment")
        notebook.AddPage(tab_two, "Target Deployment")
        
        # Create a sizer to manage the layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.EXPAND)
        
        self.panel.SetSizer(sizer)
        self.Show()

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None, "SDK Deployment Duplicator 0.1")
    app.MainLoop()