import pygame
import sys


pygame.init()
pygame.font.init()
#Define colours and fonts
font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 30)
subtitle_font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 50)
header2 = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 40)
header3 = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 30)
textbox_font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 30)
aes_font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 20)
Black = (0,0,0)
White = (255,255,255)
Green = (0,255,0)
Red = (255,0,0)
Blue = (0,0,255)
Gray = (200,200,200)

#Opening a window
size = (1024,768)
screen = pygame.display.set_mode(size)
screen.fill(Red)
#Set window title
pygame.display.set_caption("CipherTime")

#loop unti the user clicks the close button
done = False

#Used to manage how fast the screen updates
clock = pygame.time.Clock()

class OutputBox:
    """This class is used for displaying the output of the various algorithms"""
    def __init__(self, x, y, width, height, text="", font=font):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.surface = screen
        self.colour = White
        self.font = font

    def draw_output_box(self):
        """Draws the output box on the page, including the text to be displayed, when called."""
        pygame.draw.rect(self.surface, self.colour, (self.x, self.y, self.width, self.height))
        text = self.font.render(self.text, True, Black, None)
        text_rectangle = text.get_rect(center = ((self.x + self.width/2), (self.y + self.height/2)))
        screen.blit(text, text_rectangle)
        pygame.display.flip()


class Textbox:
    """This class is used to create the textboxes on the pages"""
    def __init__(self, x, y, width, height, surface, max_characters, ints_only=False, char_limit=None, current_text="", ints_only_text=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surface = surface
        self.rectangle = None
        self.current_text = current_text
        self.max_characters = max_characters
        self.colour = White
        self.clicked = False
        self.ints_only = ints_only
        self.char_limit = char_limit
        self.ints_only_text = ints_only_text

    def draw_textbox(self):
        """Draws the textbox on the page, colours it grey if it is in use"""
        if self.clicked:
            self.colour = Gray
        else: self.colour = White
        self.rectangle = pygame.draw.rect(self.surface, self.colour, (self.x, self.y, self.width, self.height))

    def collide(self, current_x, current_y):
        """Checks if the mouse cursor is currently within the textbox."""
        if self.x<current_x<self.x+self.width and self.y<current_y<self.y+self.height:
            return True
        else: return False

    def draw_text(self, _input):
        """Draws the text that is currently stored within the textbox, but only draws a certain amount of the characters
        if the length exceeds the length that the textbox can display at once, creating the scrolling effect"""
        if len(_input) > self.max_characters:
            text = textbox_font.render(_input[-self.max_characters:], True, Black, None)
            screen.blit(text, (self.x+2, self.y+2))
        else:
            text = textbox_font.render(_input, True, Black, None)
            screen.blit(text, (self.x+2, self.y+2))

    def take_text(self, input_key):
        """Takes an input, which is a key press, adds it to what is currently stored within the textbox and makes a call
        to draw text to display the new text"""
        if self.ints_only:
            try:
                int(input_key)
                self.current_text += input_key
                if self.char_limit and len(self.current_text) > self.char_limit:
                    self.current_text = self.current_text[:self.char_limit]
                self.draw_text(self.current_text)
            except:
                pass
        else:
            self.current_text += input_key
            if self.char_limit and len(self.current_text) > self.char_limit:
                self.current_text = self.current_text[:self.char_limit]
            self.draw_text(self.current_text)


    def delete_text(self):
        """Used to delete one charater from the textbox"""
        self.current_text = self.current_text[:-1]
        self.draw_text(self.current_text)

    def clear_text(self):
        """Deletes everything currently stored within the textbox"""
        self.current_text=""


class Button:
    """Creates the buttons that are displayed on the page, and processes events in which these buttons are pressed,
    including function calls"""
    def __init__(self, text, x, y, width, height, colour=White, surface=screen, function_to_call=None, arguments=[], dedi_output_box=None, to_return=False, textboxes=None
                 ,provided_instance=True):
        """Takes in a function and any potential arguments that may be needed, as well as coordinates and linked textboxes
        to retrieve text from in the event of a press"""
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surface = surface
        self.function = function_to_call
        self.colour = colour
        self.arguments = arguments
        self.linked_textboxes = textboxes
        self.dedi_output_box = dedi_output_box
        self.to_return = to_return
        self.provided_instance = provided_instance

    def collide(self, current_x, current_y):
        """Checks if the user's cursor is currently over the button"""
        if self.x<current_x<self.x+self.width and self.y<current_y<self.y+self.height:
            return True
        else:
            return False

    def on_press(self):
        """On the event of a button press it grabs all the text currently stored within the textboxes that are used by
        the button, and calls the button's designated function with these as arguments as well as any predetermined
        arguments passed in to the class constructor. If no arguments are needed the function is simply called,
        for example switching pages. If it needs to return something which would be sent to an output box,
        that is returned"""
        if self.linked_textboxes:
            for i in self.linked_textboxes:
                self.arguments.append(i.current_text)

        if self.to_return:
            if len(self.arguments)>0:
                if self.provided_instance:
                    what_to_return = self.function(*self.arguments)
                    self.arguments = self.arguments[:1]
                    return what_to_return
                elif not self.provided_instance:
                    what_to_return = self.function(*self.arguments)
                    self.arguments=[]
                    return what_to_return
            else:
                return self.function()
        else:
            self.function()

    def draw_button(self):
        """Draws the button on the page"""
        pygame.draw.rect(self.surface, self.colour, (self.x, self.y, self.width, self.height))
        text = font.render(self.text, True, Black, None)
        text_rectangle = text.get_rect(center = ((self.x + self.width/2), (self.y + self.height/2)))
        screen.blit(text, text_rectangle)
        pygame.display.flip()



class Page:
    def __init__(self, active=False, title="CipherTime", **kwargs):
        """Takes in any additional arguments, these may be buttons, texboxes etc so the __dict__ is updated
        accordingly if they are textboxes, buttons etc."""
        self.surface = screen
        self.active = active
        self.title = title
        self.__dict__.update(kwargs)
        self.text_boxes = []
        self.output_boxes = []
        for i in self.__dict__.values():
            if type(i) is Textbox:
                self.text_boxes.append(i)
            elif type(i) is OutputBox:
                self.output_boxes.append(i)


    def clear_page(self):
        """Wipes the page"""
        self.surface.fill((0, 0, 0))

    def run_page(self):
        """Executes the page, draws any buttons, textboxes, output boxes or text, and processes events such
        as key down or mouse down."""
        title_font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 70)
        buttons, text_to_add = [], []
        self.clear_page()
        for i in self.__dict__.values():
            if type(i) is Button:
                buttons.append(i)
            elif type(i) is Text:
                text_to_add.append(i)

        done = False
        while not done:
            title = title_font.render(self.title, True, White, None)
            title_rect = title.get_rect(center=(512,35))
            screen.blit(title, title_rect)
            # --- Main event loop
            for i in buttons:
                i.draw_button()
                current_mouse_pos = pygame.mouse.get_pos()
                if i.collide(current_mouse_pos[0], current_mouse_pos[1]):
                    i.colour = Gray
                else:
                    i.colour = White
            for i in self.text_boxes:
                i.draw_textbox()
                i.draw_text(i.current_text)
                if i.ints_only_text:
                    text = header3.render("This field must be an integer!", True, White, None)
                    text_rectangle = text.get_rect(center=(i.x + i.width / 2, i.y + 100))
                    screen.blit(text, text_rectangle)
                    pygame.display.flip()
            for i in text_to_add:
                if i.active == True:
                    i.draw_text()
            for i in self.output_boxes:
                i.draw_output_box()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    current_mouse_pos = pygame.mouse.get_pos()
                    for i in buttons:
                        if i.collide(current_mouse_pos[0], current_mouse_pos[1]):
                            if i.to_return and i.dedi_output_box:
                                i.dedi_output_box.text = i.on_press()
                            else:
                                i.on_press()
                    for i in self.text_boxes:
                        if i.collide(current_mouse_pos[0], current_mouse_pos[1]):
                            i.clicked = True
                        elif not i.collide(current_mouse_pos[0], current_mouse_pos[1]) and i.clicked:
                            i.clicked = False
                elif event.type == pygame.KEYDOWN:
                    for i in self.text_boxes:
                        if i.clicked:
                            pressed = pygame.key.get_pressed()
                            if pressed[pygame.K_BACKSPACE]:
                                i.delete_text()
                            elif pressed[pygame.K_RETURN]:
                                pass
                            elif pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]:
                                i.take_text(event.unicode)
                            elif pressed[pygame.K_SPACE]:
                                i.take_text(" ")
                            else:
                                i.take_text(event.unicode)
            clock.tick(60)
            pygame.display.flip()

    def clear_textboxes(self):
        """Empties all of the textboxes on the page"""
        for i in self.text_boxes:
            i.clear_text()
        for i in self.output_boxes:
            i.text = ""


class Text:
    """Just text to display on the page"""
    def __init__(self, text_to_say, center, text_type, active=True):
        self.text_to_say = text_to_say
        self.center = center
        self.type = text_type
        self.active = active

    def draw_text(self):
        """Draws the text that needs displaying on the page"""
        text = self.type.render(self.text_to_say, True, White, None)
        text_rectangle = text.get_rect(center=self.center)
        screen.blit(text, text_rectangle)
        pygame.display.flip()



