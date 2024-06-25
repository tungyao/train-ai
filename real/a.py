import random

# 假设的属性集合，您可以根据需要添加或修改
voltage_values = ["16V", "25V", "50V", "6.3V", "10V", "20V", "30V", "35V", "40V", "5V", "63V", "75V", "80V", "100V", "1kV", "16V2200μF"]
capacitance_values = ["100NF", "220uF", "100uF", "470uF", "1μF", "10nF", "47PF", "2200μF", "56uF", "33uF"]
inductance_values = ["2.2UH", "10μH", "22μH", "100UH"]
resistance_values = ["1K", "22R", "10kΩ", "100kΩ"]
precision_values = ["±1%", "±5%", "±10%", "±20%", "3%", "5%"]
electricity_values = ["1A", "2.8A", "20mA", "1.1A", "270mA", "2.35A", "2.1A", "1.516A", "2.7A"]

# 封装类型和元件类型
package_types = ["0603", "0805", "1206", "1210", "2512", "0402", "SMD", "D10xL10mm", "SOT-23", "TO-3", "DFN1006-2L"]
component_types = ["贴片电容", "贴片电阻", "贴片电感", "稳压二极管", "场效应管(MOSFET)", "三极管(BJT)", "肖特基二极管", "通用二极管", "静电和浪涌保护(TVS/ESD)"]

# 随机生成数据
def generate_random_data(count=50):
    for _ in range(count):
        component_type = random.choice(component_types)
        package_type = random.choice(package_types)
        properties = {
            "Model": f"{component_type}_{random.choice(voltage_values)}_random",
            "Package": package_type,
            "Type": component_type,
            "Voltage": random.choice(voltage_values) if component_type != "贴片电阻" else "",
            "Cap": random.choice(capacitance_values) if component_type == "贴片电容" else "",
            "Inductance": random.choice(inductance_values) if component_type == "贴片电感" else "",
            "Resistance": random.choice(resistance_values) if component_type == "贴片电阻" else "",
            "Precision": random.choice(precision_values),
            "Watt": "", # 根据具体元件类型决定是否添加
            "Electricity": random.choice(electricity_values) if component_type in ["场效应管(MOSFET)", "三极管(BJT)"] else ""
        }

        # 根据元件类型添加特定属性
        if component_type == "贴片电阻":
            properties["Watt"] = random.choice(["1/8W", "1/10W", "125mW", "100mW", "62.5mW"])

        data_tuple = (f"{component_type} 示例 {random.randint(1000, 9999)}", [(key, value) for key, value in properties.items() if value])
        print(data_tuple)

# 调用函数生成50条随机数据
generate_random_data(50)