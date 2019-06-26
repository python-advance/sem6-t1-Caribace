from guestbookpackage import GuestBook


guest_book = GuestBook()
guest_book.add_guest("Mikhail", "Nikanorov", "caribace@mail.ru")
guest_book.add_guest("Caribace", "Caribovich", "caribovich@mail.ru")
guest_book.remove_guest("caribace@mail.ru")
guest_book.full_remove_guest("caribovich@mail.ru")
guest_book.rename_guest("caribovich@mail.ru","Caribace","Caribovich")
guest_book.write_file()
guest_book.file_cleanup()
