### Скрипт для отслеживания изменений в файле

on_any_event — обработчик событий Catch-all.
on_created вызывается при создании файла или каталога.
on_deleted вызывается при удалении файла или каталога.
on_modified вызывается при изменении файла или каталога.
on_moved вызывается при перемещении или переименовании файла или каталога.

event_type — тип события в виде строки. По умолчанию значение None.
is_directory — true, если событие было выдано для каталога. В противном случае — false.
src_path — исходный путь объекта файловой системы, вызвавшего это событие.