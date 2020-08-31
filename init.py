import ui, caesar, vernam, aes
import rsa_encryption as rsa
#Defining the menu page,
menu = ui.Page(Caesar=ui.Button("Caesar Cipher", 50, 325, 250, 100),
            Vernam=ui.Button("Vernam Cipher", 724, 325, 250, 100),
            RSA=ui.Button("RSA", 50, 575, 250, 100),
            AES=ui.Button("AES", 724, 575, 250, 100),
            subtitle1=ui.Text("Simple Ciphers", (512, 250), ui.subtitle_font),
            subtitle2=ui.Text("Complex Ciphers", (512, 500), ui.subtitle_font),
            explanation=ui.Text("A program for teaching people about encryption", (512, 150), ui.header3))
#Defining the back to menu button that is used across all the pages.
back_button = ui.Button("Menu", 50, 35, 150, 100, function_to_call=menu.run_page)
#Defining the Caesar cipher page
caesar_page = ui.Page(back_button,
                   encrypt_text_box = ui.Textbox(360, 250, 300, 50, ui.screen, 20),
                    encrypt_shift_box = ui.Textbox(360, 400, 300, 50, ui.screen, 15, True, 2, "1", True),
                      plaintext_title = ui.Text("Plaintext:", (512, 200), ui.subtitle_font),
                    shift_title=ui.Text("Shift:", (512, 350), ui.subtitle_font),
                      clear_textbox_button = ui.Button("Clear Boxes", 730, 300, 175, 100),
                      encrypt_button = ui.Button("Encrypt!", 330, 535, 150, 100, to_return=True),
                      decrypt_button = ui.Button("Decrypt!", 550, 535, 150, 100, to_return=True),
                      ciphertext = ui.OutputBox(50, 650, 924, 100),
                      ciphertext_label = ui.Text("Output:", (125, 630), ui.header3))

#Defining all of the buttons functions and linked textboxes and output boxes for the Caesar cipher page
menu.Caesar.function = caesar_page.run_page
caesar_page.clear_textbox_button.function = caesar_page.clear_textboxes
caesar_page.encrypt_button.dedi_output_box = caesar_page.ciphertext
caesar_instance = caesar.Caesar
caesar_page.encrypt_button.function = caesar_instance.caesar
caesar_page.encrypt_button.linked_textboxes = [caesar_page.encrypt_text_box, caesar_page.encrypt_shift_box]
caesar_page.encrypt_button.arguments = [caesar_instance]
caesar_page.decrypt_button.function = caesar_instance.decrypt
caesar_page.decrypt_button.linked_textboxes = [caesar_page.encrypt_text_box, caesar_page.encrypt_shift_box]
caesar_page.decrypt_button.arguments = [caesar_instance]
caesar_page.decrypt_button.dedi_output_box = caesar_page.ciphertext
#Defining the Vernam cipher page
vernam_page = ui.Page(back_button,
                   encrypt_text_box = ui.Textbox(360, 250, 300, 50, ui.screen, 20),
                    encrypt_key_box = ui.Textbox(360, 400, 300, 50, ui.screen, 15, False),
                      plaintext_title = ui.Text("Plaintext:", (512, 200), ui.subtitle_font),
                    shift_title=ui.Text("Key:", (512, 350), ui.subtitle_font),
                      clear_textbox_button = ui.Button("Clear Boxes", 730, 300, 175, 100),
                      encrypt_button = ui.Button("Encrypt!", 330, 500, 150, 100, to_return=True, provided_instance=False),
                      ciphertext = ui.OutputBox(50, 650, 924, 100),
                      ciphertext_label = ui.Text("Output:", (125, 630), ui.header3),
                     decrypt_button = ui.Button("Decrypt!", 550,500, 150, 100, to_return=True, provided_instance=True))

#Linking all of the buttons to their functions, textboxes and output boxes for the Vernam page
menu.Vernam.function = vernam_page.run_page
vernam_page.clear_textbox_button.function = vernam_page.clear_textboxes
vernam_page.decrypt_button.dedi_output_box = vernam_page.ciphertext
vernam_page.encrypt_button.dedi_output_box = vernam_page.ciphertext
vernam_instance = vernam.Vernam()
vernam_page.encrypt_button.function = vernam_instance.vernam
vernam_page.decrypt_button.function = vernam_instance.vernam
vernam_page.decrypt_button.arguments = [""]
vernam_page.encrypt_button.linked_textboxes = [vernam_page.encrypt_text_box, vernam_page.encrypt_key_box]
vernam_page.decrypt_button.linked_textboxes = [vernam_page.encrypt_key_box, vernam_page.encrypt_text_box]
#Defining the RSA page
rsa_page = ui.Page(back_button,
                   plaintext_text_box = ui.Textbox(50, 250, 300, 50, ui.screen, 100),
                    e_box = ui.Textbox(50, 380, 300, 50, ui.screen, 15, True),
                      plaintext_title = ui.Text("Plaintext:", (110, 220), ui.header3),
                    e_title=ui.Text("e value:", (110, 350), ui.header3),
                    privatekey1_text_box = ui.Textbox(400, 250, 300, 50, ui.screen, 25, True),
                   privatekey2_text_box=ui.Textbox(400, 380, 300, 50, ui.screen, 25, True),
                   privatekey1_title=ui.Text("First private key:", (510, 220), ui.header3),
                   privatekey2_title=ui.Text("Second private key:", (530, 350), ui.header3),
                   d_box=ui.Textbox(50, 510, 300, 50, ui.screen, 15, True),
                   d_title=ui.Text("d value:", (110, 480), ui.header3),
                   ciphertext=ui.OutputBox(50, 650, 924, 100),
                   ciphertext_label=ui.Text("Output:", (125, 630), ui.header3),
                   explanation_text=ui.Text("Please read the help page before use.", (512, 170), ui.header3),
                   help_page_button=ui.Button("Help", 824, 35, 150, 100),
                   clear_textboxes_button = ui.Button("Clear Boxes", 400, 460, 175, 100),
                   find_e_value_button=ui.Button("Find e", 824, 220, 150, 100, to_return=True),
                   encrypt_button=ui.Button("Encrypt", 824, 370, 150, 100, to_return=True),
                   decrypt_button=ui.Button("Decrypt", 824, 520, 150, 100, to_return=True))
#Clear textbox button
rsa_page.clear_textboxes_button.function=rsa_page.clear_textboxes
#Defining the RSA help page
rsa_help_page=ui.Page(back_to_rsa=ui.Button("Back", 50, 35, 150, 100),
                      page_subtitle=ui.Text("Please note the following things before using RSA:",(512, 170), ui.header2),
                      key_point=ui.Text("The most important thing is that both private key fields are prime numbers.",(512, 220), ui.header3),
                      explanation0=ui.Text("If you enter your own e value, make sure its coprime to the ", (512, 500), ui.header3),
                      expalanation02=ui.Text("product of privatekey1-1 and privatekey2-1",(512, 540), ui.header3),
                      explanation1=ui.Text("Before encrypting the private key and e fields must be full.", (512, 260), ui.header3),
                      explanation2=ui.Text("To use the e finding function, the private key fields must be full.", (512, 300), ui.header3),
                      explanation3=ui.Text("To decrypt, the private key fields and the e OR d fields must be full", (512, 340), ui.header3),
                      explanation4=ui.Text("When encrypting the output will be decimal ascii values.", (512, 380), ui.header3),
                      explanation5=ui.Text("Decryption must also be done on ascii values", (512, 420), ui.header3),
                      explanation6=ui.Text("The output of decryption will be text.", (512, 460), ui.header3))

#Allocating all of the buttons functions, textboxes and output boxes if needed for the RSA and RSA help pages
rsa_page.help_page_button.function = rsa_help_page.run_page
rsa_help_page.back_to_rsa.function=rsa_page.run_page
menu.RSA.function=rsa_page.run_page
rsa_page.find_e_value_button.dedi_output_box = rsa_page.ciphertext
rsa_page.encrypt_button.dedi_output_box = rsa_page.ciphertext
rsa_page.decrypt_button.dedi_output_box = rsa_page.ciphertext
rsa_instance = rsa.RSA
rsa_page.encrypt_button.function=rsa_instance.encrypt
rsa_page.encrypt_button.arguments=[rsa_instance]
rsa_page.encrypt_button.linked_textboxes = [rsa_page.plaintext_text_box, rsa_page.privatekey1_text_box, rsa_page.privatekey2_text_box,
                                            rsa_page.e_box]
rsa_page.find_e_value_button.function=rsa_instance.find_e_value
rsa_page.find_e_value_button.arguments=[rsa_instance]
rsa_page.find_e_value_button.linked_textboxes = [rsa_page.privatekey1_text_box, rsa_page.privatekey2_text_box]
rsa_page.decrypt_button.function=rsa_instance.decrypt
rsa_page.decrypt_button.arguments=[rsa_instance]
rsa_page.decrypt_button.linked_textboxes=[rsa_page.privatekey1_text_box, rsa_page.privatekey2_text_box, rsa_page.e_box, rsa_page.d_box,
                                          rsa_page.plaintext_text_box]
#Defining the AES page
aes_page = ui.Page(back_button,
                   encrypt_text_box = ui.Textbox(360, 250, 300, 50, ui.screen, 19),
                    encrypt_shift_box = ui.Textbox(360, 400, 300, 50, ui.screen, 16, char_limit=16),
                      plaintext_title = ui.Text("Message:", (512, 200), ui.subtitle_font),
                    shift_title=ui.Text("Keyword:", (512, 350), ui.subtitle_font),
                      clear_textbox_button = ui.Button("Clear Boxes", 730, 300, 175, 100),
                      encrypt_button = ui.Button("Encrypt!", 330, 475, 150, 100, to_return=True),
                      ciphertext = ui.OutputBox(50, 650, 924, 100, font = ui.aes_font),
                      ciphertext_label = ui.Text("Output:", (125, 630), ui.header3),
                    decrypt_button = ui.Button("Decrypt!", 550, 475, 150, 100, to_return=True))
#Allocating functions, output boxes and textboxes to buttons for the AES page where needed.
menu.AES.function = aes_page.run_page
aes_page.clear_textbox_button.function = aes_page.clear_textboxes
aes_instance = aes.AES
aes_page.encrypt_button.function = aes_instance.deal_with_encrypt
aes_page.encrypt_button.linked_textboxes = [aes_page.encrypt_text_box, aes_page.encrypt_shift_box]
aes_page.encrypt_button.arguments = [aes_instance]
aes_page.encrypt_button.dedi_output_box = aes_page.ciphertext
aes_page.decrypt_button.function = aes_instance.deal_with_decrypt
aes_page.decrypt_button.linked_textboxes = [aes_page.encrypt_text_box, aes_page.encrypt_shift_box]
aes_page.decrypt_button.arguments = [aes_instance]
aes_page.decrypt_button.dedi_output_box = aes_page.ciphertext

#Running the menu page at the start of the program.
menu.run_page()

