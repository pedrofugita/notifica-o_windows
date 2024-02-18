from winotify import Notification

notificacao = Notification(app_id="Monitoramento de preços de celular",
                           title="Planilha atualizada",
                           msg="Os preços dos celulares monitorados foram adicionados à planilha.",
                           duration="short",
                           icon=r"C://Users/pedro/Desktop/Python/logo.png")

notificacao.add_actions(label="Abrir planilha", launch="file:///C:/Users/pedro/Desktop/Python/preços_celulares.xlsx")
notificacao.show()