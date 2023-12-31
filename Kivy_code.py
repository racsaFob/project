import pyautogui


resolution = pyautogui.size()
width = resolution[0]-1
height = resolution[1]-1
move_value =150
kivy_code = f"""



<painter>:
    canvas:
        Color:
            rgb:(0.1, 0.1, 0.1)

        Rectangle:
            pos:  (0,0)
            size:  (3000,1900)

        Color:
            rgba:(1,1,1,1)
        Rectangle:
            pos: (0,{height/4})
            size:({width/1.15},2000)

        Color:
            rgba:(1,1,1,0.15)
        Line:
            points:({width/1.13},{height/4.5},{width/1.05},{height/4.5})
            width:5

        Line:
            points:({width/1.13},{height/6.2},{width/1.05},{height/6.2})
            width:5

        Color:
            rgb:(0,0,0)

<moving_painter_but>:
    size:{width/30},{height/30}
    pos: {width/10},{height/4 - height/30}
    
    on_release:root.released()
    
    
<moving_painter_widget>:
    Button:
        on_press: root.pressed(0,{move_value*(-1)})
        size:{width/50},{height/20}
        pos:{width/10+width/120},{height/4 - height/10}
        
    Button:
        on_press: root.pressed(0,{move_value})
        size:{width/50},{height/20}
        pos:{width/10+width/120},{height/4 - height/5}
        
    Button:
        on_press: root.pressed({move_value*(-1)},0)
        size:{height/20},{width/50}
        pos:{width/10+width/30},{height/4 - height/7}
        
    Button:
        on_press: root.pressed({move_value},0)
        size:{height/20},{width/50}
        pos:{width/10 - width/40},{height/4 - height/7}

<Personal_color_but>:
    size:{width/24},{width/24}
    center_x : {width/1.042}
    center_y: {height/3.25}
    on_release: root.pressed()
    background_normal:'images/ask_color_but.png'
    background_down:'images/ask_color_but.png' 


<Ask_Color>:
    Button:     
        center_x : {width/2-200}
        center_y : {height/2}
        size:(500,300)
        background_color:(0.15,0.15,0.15)
        background_normal:''
        background_down:'' 


    Button:     
        id:color_view
        center_x : {width/2+75}
        center_y : {height/2+50}
        size:(200,200)
        background_color:(0,0,0)
        background_normal:''
        background_down:''

    Button:
        
        center_x : {width/2+220}
        center_y : {height/2+260}
        size:(70,30)
        on_release: root.back()
        text:'НАЗАД'
        font_size:15
        font:'Arial Black'
        background_color:0.35, 0.35, 0.4, 1
        background_normal:''


    Label:
        text:'RED'
        color:1,0,0
        center_x: {width/2-182}
        center_y: {height/2+215}
        font_size:20


    Label:
        text:'GREEN'
        color:0,1,0
        center_x: {width/2-172}
        center_y: {height/2+140}
        font_size:20


    Label:
        text:'BLUE'
        color:0,0,1
        center_x: {width/2-177}
        center_y: {height/2+65}
        font_size:20

    Slider:
        center_x: {width/2-150}
        center_y: {height/2+200}
        size: 200,50
        value: 0
        on_value: root.red(self.value,color_view)


    Slider:
        center_x: {width/2-150}
        center_y: {height/2+125}
        size: 200,50
        value: 0
        on_value: root.green(self.value,color_view)

    Slider:
        center_x: {width/2-150}
        center_y: {height/2+50}
        size: 200,50
        value: 0
        on_value: root.blue(self.value,color_view)


    Button:
        
        center_x : {width/2}
        center_y : {height/2}
        size:(80,40)
        on_release: root.accept()
        text:'ПРИНЯТЬ'
        font_size:15
        font:'Arial Black'
        background_color:0.35, 0.35, 0.4, 1
        background_normal:''






<Figure_Buttons>:
    pos:{width/2},0
    size:({width/6},{height/4})
    cols: 3
    rows: 2
    spacing:5
    padding:10

    Button:
        background_normal:'images/square.'
        on_release:root.pressed('square')
    Button:
        background_normal:'images/square1.png'
        on_release:root.pressed('ellipse')
    Button:
        background_normal:'images/triangle.png'
        on_release:root.pressed('triangle')
    Button:
        background_normal:''
        on_release:root.pressed('pencil')
    Button:
        background_normal:''
    Button:
        background_normal:''



<Figure_buttons_settings>:
    pos:{width/2+width/6},{height/4-height/30*2}
    size:{width/40},{height/30}
    cols:2
    rows:2
    Button:
        background_normal:'images/check_mark.png'
        on_release:root.pressed('filling')



<clear_window>:
    center_x : {width/2-200}
    center_y : {height/2}
    size:(500,300)
    background_color:(0.15,0.15,0.15)
    background_normal:''
    background_down:''

    Label:
        text:'Вы уверены, что хотите очистить холст?'
        font_size:20
        center_x:{width/2}
        center_y:{height/2+170}

    Label:
        text:'Ваш результат не сохранится'
        font_size:15
        center_x:{width/2}
        center_y:{height/2+130}


    Button:
        id: yes_button
        center_x : {width/2-140}
        center_y : {height/2+30}
        size:(70,50)
        on_release: root.yes(root)

        text:'ДА'
        font_size:25
        font:'Arial Black'
       
        background_color:0.65, 0.01, 0.01, 1
        
        background_normal:''
        background_down:'images/red.png' 


    Button:
        id:no_button
        center_x : {width/2+150}
        center_y : {height/2+30}
        size:(70,50)
        on_release: root.no(root)
        text:'НЕТ'
        font_size:20
        font:'Arial Black'
        background_color:0.35, 0.35, 0.4, 1
        background_normal:''


    Button:
        
        center_x : {width/2+220}
        center_y : {height/2+260}
        size:(70,30)
        on_release: root.no(root)
        text:'НАЗАД'
        font_size:15
        font:'Arial Black'
        background_color:0.35, 0.35, 0.4, 1
        background_normal:''





<save_pic_but>:
    id: save_but
    size:{width/20},{width/20}
    center_x:{width/20/2}
    center_y:{width/20/2}
    background_normal:'images/save_but.png'
    background_down:'images/save_but.png'
    on_press: root.pressed(root)



<returns_buttons>:


    Button:
        id:left
        background_normal:'images/return_button_left.png'
        background_down:'images/return_button_left.png'
        on_press:root.pressed_left(left)
        
        center_x :{width/1.0955}
        center_y: {height-height/85}
        size:{width/20},{height/20}
        on_touch_up:root.touch_up(self)
        on_release:root.release_left()
        

    Button:
        id:right
        background_normal:'images/return_button.png'
        background_down:'images/return_button.png'
        on_press:root.pressed_right(right)
        center_x :{width/1.0955+width/20+(width/340)}
        center_y: {height-height/85}

        size:{width/20},{height/20}

        on_touch_up:root.touch_up(self)
        on_release:root.release_right()





<change_size>:
    size: (32,32)
    pos: ({width/1.13},{height/4.8})
    background_normal: 'images/button.png'
    background_down: 'images/button.png'
    Label:
        text:'size:'
        pos: ({width/1.15},{height/4.7})
        font_size:{width/65}




<change_bright>:
    size: (32,32)
    pos: ({width/1.05},{height/6.8})
    background_normal: 'images/button.png'
    background_down: 'images/button.png'
    
    Label:
        text:'bright:'
        pos: ({width/1.15},{height/6.7})
        font_size:{width/65}


            

<Window_ask_function>:
    Button:     
        center_x : {width/2-200}
        center_y : {height/2}
        size:(500,300)
        background_color:(0.15,0.15,0.15)
        background_normal:''
        background_down:''

    Label:
        text:'f(x):'
        font_size: 35
        center_x:{width/2-200}
        center_y:{height/2+170} 




    Button:
        background_color:(1,1,1)
        background_normal:''
        background_down:''        
        center_x : {width/2-100}
        center_y : {height/2+190}
        size:(350,50)

    TextInput:
        id: text     
        center_x : {width/2-100}
        center_y : {height/2+190}
        size:(350,50)
        multiline:False
        font_size:25


    Button:
        center_x : {width/2-200}
        center_y : {height/2} 
        size:60,40
        text:('÷')   
        font_size:25
        on_release:root.devision(text)

    Button:
        center_x : {width/2-200}
        center_y : {height/2+50} 
        size:60,40
        text:('X')   
        font_size:25
        background_color:(0.8,0,0)
        on_release:root.clear(text)

    Button:
        center_x : {width/2}
        center_y : {height/2}
        size:(80,40)
        on_release: root.accept(text)
        text:'ПРИНЯТЬ'
        font_size:15
        font:'Arial Black'
        background_color:0.35, 0.35, 0.4, 1
        background_normal:''


    Button:
        
        center_x : {width/2+220}
        center_y : {height/2+260}
        size:(70,30)
        on_release: root.back(text)
        text:'НАЗАД'
        font_size:15
        font:'Arial Black'
        background_color:0.35, 0.35, 0.4, 1
        background_normal:''




<Ask_function_but>:
    center_x: {width/5}
    center_y:{height/7+height/20}
    size: {width/6},{height/15}
    on_release:root.released()
    text:'ЗАДАТЬ ФУНКЦИЮ'
    font_size:25



<Ask_function_settings>:
    id: settings
    cols:4
    center_x : {width/5}
    y: 0
    size:({width/4.5},{height/7})
    ToggleButton:
        size:{width/60},{width/60}
        size_hint_x:None
        size_hint_y:None
        on_release:root.pressed_1(self.state)


    Label:
        text:'КЛЕТЧАТЫЙ ФОН'
        pos_hint_y: 0.8
        font_size:{width/100}

    ToggleButton:
        size:{width/60},{width/60}
        size_hint_x:None
        size_hint_y:None
        on_release:root.pressed_4(self.state)


    Label:
        text:'ВЫКОЛ. ТОЧКИ'
        pos_hint_y: 0.8
        font_size:{width/100}

    ToggleButton:
        size:{width/60},{width/60}

        size_hint_x:None
        size_hint_y:None
        on_release:root.pressed_2(self.state)


    Label:
        text:'ОСИ КООРДИНАТ'
        font_size:{width/100}

    ToggleButton:
        size:{width/60},{width/60}
        size_hint_x:None
        size_hint_y:None
        on_release:root.pressed_5(self.state)


    Label:
        text:'ОБЩИЕ ТОЧКИ'
        pos_hint_y: 0.8
        font_size:{width/100}

    ToggleButton:
        size:{width/60},{width/60}

        size_hint_x:None
        size_hint_y:None
        on_release:root.pressed_3(self.state)


    Label:
        text:'ЕДИН. ОТРЕЗКИ'
        font_size:{width/100}


    ToggleButton:
        size:{width/60},{width/60}
        size_hint_x:None
        size_hint_y:None
        on_release:root.pressed_6(self.state)


    Label:
        text:'СПИСОК ГРАФИКОВ'
        pos_hint_y: 0.8
        font_size:{width/130}



"""
