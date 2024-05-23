def convert_seconds(seconds):
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    day_str = f"{days} день" if days == 1 else f"{days} днів"
    hour_str = str(hours).zfill(2)
    minute_str = str(minutes).zfill(2)
    second_str = str(seconds).zfill(2)

    return f"{day_str}, {hour_str}:{minute_str}:{second_str}"

input_seconds = int(input("ввод секунд (0-8639999): "))
if 0 <= input_seconds < 8640000:
    result = convert_seconds(input_seconds)
    print(result)
else:
    print("Число >= 0 и больше чем 8640000.")
