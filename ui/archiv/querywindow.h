#ifndef QUERYWINDOW_H
#define QUERYWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui {
class QueryWindow;
}
QT_END_NAMESPACE

class QueryWindow : public QMainWindow
{
    Q_OBJECT

public:
    QueryWindow(QWidget *parent = nullptr);
    ~QueryWindow();

private:
    Ui::QueryWindow *ui;
};
#endif // QUERYWINDOW_H
