def chai_list():
    return ["chai", "chai latte", "chai tea", "masala chai"];

function_wla_Chail = chai_list()
print(function_wla_Chail)

def espresso_list():
    yield "espresso"
    yield "double espresso"
    yield "iced espresso"
    yield "espresso macchiato"
    yield "affogato" 

genrator = espresso_list();
print(next(genrator))
print(next(genrator))
print(next(genrator))
print(next(genrator))
print(next(genrator))
