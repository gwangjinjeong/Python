def open_Folder(self):
    print('open')
    dirPath = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
    file_list = os.listdir(dirPath)
    for filename in file_list:
        full_filename = os.path.join(dirPath, filename)
        if os.path.isdir(full_filename):
            itemTop2 = QTreeWidgetItem(self.treeWidget_dir)
            itemTop2.setText(0,filename)
            print(full_filename)
            for newlist in os.listdir(full_filename):
                itemChild1 = QTreeWidgetItem(itemTop2)
                itemChild1.setText(0,newlist)
        else:
            itemTop1 = QTreeWidgetItem(self.treeWidget_dir)
            itemTop1.setText(0,filename)
@pyqtSlot(QTreeWidgetItem, int)
def onItemClicked(self, it, col):
    print(it.parent().text(col))
    print(it, col, it.text(col))
