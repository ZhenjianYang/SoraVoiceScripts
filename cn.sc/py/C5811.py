from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5811   ._SN',
        MapName             = 'Other',
        Location            = 'C5811.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60062",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    DeclActor(
        TriggerX            = -11900,
        TriggerZ            = 0,
        TriggerY            = -5480,
        TriggerRange        = 1500,
        ActorX              = -11900,
        ActorZ              = 1000,
        ActorY              = -5480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4730,
        TriggerZ            = 0,
        TriggerY            = 12330,
        TriggerRange        = 1000,
        ActorX              = 5090,
        ActorZ              = 1000,
        ActorY              = 12940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5410,
        TriggerZ            = 0,
        TriggerY            = 12060,
        TriggerRange        = 1000,
        ActorX              = -5740,
        ActorZ              = 1000,
        ActorY              = 12680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5160,
        TriggerZ            = 0,
        TriggerY            = -11960,
        TriggerRange        = 1000,
        ActorX              = 5370,
        ActorZ              = 1000,
        ActorY              = -12630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_13A",          # 00, 0
        "Function_1_13B",          # 01, 1
        "Function_2_187",          # 02, 2
        "Function_3_2AF",          # 03, 3
        "Function_4_3D7",          # 04, 4
        "Function_5_4DF",          # 05, 5
    )


    def Function_0_13A(): pass

    label("Function_0_13A")

    Return()

    # Function_0_13A end

    def Function_1_13B(): pass

    label("Function_1_13B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x474, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D")
    OP_6F(0x2, 0)
    Jump("loc_154")

    label("loc_14D")

    OP_6F(0x2, 60)

    label("loc_154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x474, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_166")
    OP_6F(0x3, 0)
    Jump("loc_16D")

    label("loc_166")

    OP_6F(0x3, 60)

    label("loc_16D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x474, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17F")
    OP_6F(0x4, 0)
    Jump("loc_186")

    label("loc_17F")

    OP_6F(0x4, 60)

    label("loc_186")

    Return()

    # Function_1_13B end

    def Function_2_187(): pass

    label("Function_2_187")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x474, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_283")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x1E)
    OP_73(0x2)
    OP_6F(0x2, 30)
    OP_3E(0x39F, 10)
    OP_3E(0x3A1, 10)
    OP_3E(0x3A7, 10)
    OP_3E(0x3A9, 10)
    OP_3E(0x3AB, 10)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "\x07\x00得到了\x07\x02#20I魔兽羽翼　　　×１０\x01",
            "\x07\x02#20I魔兽之骨　　　×１０\x01",
            "\x07\x02#20I魔兽鸟肉　　　×１０\x01",
            "\x07\x02#20I魔兽鸟蛋　　　×１０\x01",
            "\x07\x02#20I魔兽之种　　　×１０\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x23A0)
    Jump("loc_29D")

    label("loc_283")


    AnonymousTalk(    #1
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_29D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_187 end

    def Function_3_2AF(): pass

    label("Function_3_2AF")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x474, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x1E)
    OP_73(0x3)
    OP_6F(0x3, 30)
    OP_3E(0x39E, 10)
    OP_3E(0x3A0, 10)
    OP_3E(0x3A3, 10)
    OP_3E(0x3A4, 10)
    OP_3E(0x3A5, 10)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        (
            "\x07\x00得到了\x07\x02#20I魔兽之角　　　×１０\x01",
            "\x07\x02#20I魔兽尾巴　　　×１０\x01",
            "\x07\x02#20I魔兽之牙　　　×１０\x01",
            "\x07\x02#20I魔兽甲壳　　　×１０\x01",
            "\x07\x02#20I魔兽之肉　　　×１０\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x23A1)
    Jump("loc_3C5")

    label("loc_3AB")


    AnonymousTalk(    #3
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_3C5")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_2AF end

    def Function_4_3D7(): pass

    label("Function_4_3D7")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x474, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x1E)
    OP_73(0x4)
    OP_6F(0x4, 30)
    OP_3E(0x3A2, 10)
    OP_3E(0x3A6, 10)
    OP_3E(0x3A8, 10)
    OP_3E(0x3AA, 10)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #4
        (
            "\x07\x00得到了\x07\x02#20I魔兽眼珠　　　×１０\x01",
            "\x07\x02#20I魔兽鱼肉　　　×１０\x01",
            "\x07\x02#20I魔兽明胶　　　×１０\x01",
            "\x07\x02#20I魔兽鱼卵　　　×１０\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x23A2)
    Jump("loc_4CD")

    label("loc_4B3")


    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_4CD")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_3D7 end

    def Function_5_4DF(): pass

    label("Function_5_4DF")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05#1S欢迎光临。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #7
        (
            "\x07\x05#1S现在由于系统故障的影响，\x01",
            "可选择项目受到了一定的限制。\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        40,
        90,
        0,
        (
            "【领取随身行李】\x01",      # 0
            "【放弃使用】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_592"),
        (1, "loc_854"),
        (SWITCH_DEFAULT, "loc_857"),
    )


    label("loc_592")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x417, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x456, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_633")

    AnonymousTalk(    #8
        "\x07\x05#1S开始核对………………\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #9
        "\x07\x05#1S……………………………………\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #10
        "\x07\x05#1S………………侦测不到数据。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #11
        (
            "\x07\x05#1S现在这里没有\x01",
            "您所寄放的行李。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_851")

    label("loc_633")


    AnonymousTalk(    #12
        "\x07\x05#1S开始核对…………………\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #13
        "\x07\x05#1S………………………………………\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #14
        "\x07\x05#1S………确认特定周波模型。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #15
        "\x07\x05#1S确认为已登录的受托人。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #16
        "\x07\x05#1S保管物＃R-8834-0033开始转送。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #17
        "\x07\x05#1S数据接收中…………２０％………\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #18
        "\x07\x05#1S……４０％……………６０％………\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #19
        "\x07\x05#1S……８０％……………转送完成！\x02",
    )

    CloseMessageWindow()
    OP_5F(0x0)
    Sleep(200)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #20
        "\x07\x00得到了\x1F\x18\x04\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x418, 1)

    ChrTalk(    #21
        0x101,
        (
            "#1004F这、这个\x01",
            "是资料水晶吧？\x02\x03",

            "好像是从什么地方\x01",
            "运送过来的样子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        (
            "#1042F看来是对我们身上\x01",
            "携带的物品产生了反应呢。\x02\x03",

            "#1040F如果交给拉赛尔博士，\x01",
            "说不定就能明白它的内容了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22B0)

    label("loc_851")

    Jump("loc_857")

    label("loc_854")

    Jump("loc_857")

    label("loc_857")

    Sleep(200)
    FadeToBright(300, 0)
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    TalkEnd(0xFF)
    Return()

    # Function_5_4DF end

    SaveToFile()

Try(main)
