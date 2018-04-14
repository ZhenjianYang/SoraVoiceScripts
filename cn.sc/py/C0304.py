from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C0304   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0304.x',
        MapIndex            = 19,
        MapDefaultBGM       = "ed60125",
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
        '临时',                                 # 9
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


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 3480,
        TriggerZ            = -170,
        TriggerY            = 2770,
        TriggerRange        = 1000,
        ActorX              = 3450,
        ActorZ              = 800,
        ActorY              = 3430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_EE",           # 00, 0
        "Function_1_12C",          # 01, 1
        "Function_2_196",          # 02, 2
        "Function_3_2AD",          # 03, 3
        "Function_4_74A",          # 04, 4
        "Function_5_92F",          # 05, 5
        "Function_6_C0A",          # 06, 6
        "Function_7_1126",         # 07, 7
        "Function_8_1226",         # 08, 8
        "Function_9_1261",         # 09, 9
        "Function_10_12FD",        # 0A, 10
        "Function_11_134F",        # 0B, 11
    )


    def Function_0_EE(): pass

    label("Function_0_EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_108")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 3)
    Jump("loc_12B")

    label("loc_108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_119")
    OP_A3(0x10F1)
    Event(0, 7)
    Jump("loc_12B")

    label("loc_119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 7)), scpexpr(EXPR_END)), "loc_127")
    Event(0, 8)
    Jump("loc_12B")

    label("loc_127")

    Event(0, 4)

    label("loc_12B")

    Return()

    # Function_0_EE end

    def Function_1_12C(): pass

    label("Function_1_12C")

    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xD6D8, 0x0)
    OP_43(0x8, 0x0, 0x0, 0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A")
    OP_6F(0x0, 0)
    Jump("loc_161")

    label("loc_15A")

    OP_6F(0x0, 60)

    label("loc_161")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_187")
    OP_65(0x0, 0x1)
    OP_72(0x0, 0x0)
    OP_72(0x0, 0x4)
    Jump("loc_195")

    label("loc_187")

    OP_64(0x0, 0x1)
    OP_71(0x0, 0x0)
    OP_71(0x0, 0x4)

    label("loc_195")

    Return()

    # Function_1_12C end

    def Function_2_196(): pass

    label("Function_2_196")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x276, 1)"), scpexpr(EXPR_END)), "loc_205")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x76\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1968)
    Jump("loc_26B")

    label("loc_205")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x76\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x76\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_26B")

    Jump("loc_29F")

    label("loc_26E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_29F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_196 end

    def Function_3_2AD(): pass

    label("Function_3_2AD")

    EventBegin(0x4)
    FadeToDark(0, 16777215, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D7")
    Call(0, 9)
    FadeToBright(0, 0)
    Call(0, 10)

    label("loc_2D7")

    SetChrPos(0x101, 3980, -160, 2990, 0)
    SetChrPos(0x103, 2730, -180, 2840, 0)
    SetChrPos(0xF8, 4260, -180, 1570, 0)
    SetChrPos(0xF9, 2840, -170, 1480, 0)
    OP_6D(3720, -160, 2770, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(3000, 16777215)
    OP_0D()
    Sleep(500)

    ChrTalk(    #3
        0x101,
        "#1007F#5P刚、刚才那是什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x103,
        (
            "#522F#6P铃声响起的同时，\x01",
            "就被浓雾包围了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x103, 270, 400)
    Sleep(500)

    ChrTalk(    #5
        0x103,
        "#023F#5P这、这里是……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #6
        0x101,
        "#1004F#5P咦……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_1D(0x7D)
    OP_1F(0x50, 0x64)
    Sleep(300)
    StopSound(0x64, 0x186A0, 0x1388)

    def lambda_440():
        OP_6B(6000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_440)
    Sleep(1000)

    def lambda_455():
        OP_6C(135000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_455)
    OP_8C(0x101, 90, 400)
    Sleep(100)
    OP_8C(0xF8, 90, 400)
    Sleep(100)
    OP_8C(0xF9, 180, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #7
        0x101,
        (
            "#1020F#5P！？\x02\x03",

            "这，这……是哪里！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(3630, -150, 1970, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    StopSound(0x64, 0xD6D8, 0x0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54C")

    ChrTalk(    #8
        0x107,
        (
            "#065F#5P不、不知不觉\x01",
            "景色就变了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BD")

    label("loc_54C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_586")

    ChrTalk(    #9
        0x106,
        (
            "#552F#5P哼，不知不觉\x01",
            "景色就变了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BD")

    label("loc_586")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BD")

    ChrTalk(    #10
        0x105,
        (
            "#042F#5P……不知不觉\x01",
            "景色就变了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FD")

    ChrTalk(    #11
        0x108,
        (
            "#072F#5P难不成……\x01",
            "是奇门遁甲之类的东西？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_636")

    label("loc_5FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_636")

    ChrTalk(    #12
        0x104,
        (
            "#032F#5P唔，是被抛到\x01",
            "别的地方了吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_636")

    OP_8C(0x101, 270, 400)

    ChrTalk(    #13
        0x101,
        (
            "#1020F#5P雪拉姐……\x01",
            "怎、怎么办？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_669():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_669)
    Sleep(100)

    def lambda_67C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_67C)
    Sleep(100)
    OP_8C(0x103, 90, 400)

    ChrTalk(    #14
        0x103,
        (
            "#026F#6P镇定下来，艾丝蒂尔。\x02\x03",

            "#022F如果这是敌人做的手脚……\x01",
            "必定会有逃脱的方法。\x02\x03",

            "先试着找找看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        "#1002F#5P嗯、嗯……\x02",
    )

    CloseMessageWindow()
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x1825)
    OP_28(0x92, 0x1, 0x4)
    EventEnd(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_2AD end

    def Function_4_74A(): pass

    label("Function_4_74A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_762"),
        (105, "loc_78C"),
        (107, "loc_7B6"),
        (106, "loc_7E0"),
        (SWITCH_DEFAULT, "loc_80A"),
    )


    label("loc_762")

    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_789")
    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_789")

    Jump("loc_80A")

    label("loc_78C")

    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7B3")
    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7B3")

    Jump("loc_80A")

    label("loc_7B6")

    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7DD")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7DD")

    Jump("loc_80A")

    label("loc_7E0")

    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_807")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_807")

    Jump("loc_80A")

    label("loc_80A")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_820")
    OP_A2(0x1842)
    Call(0, 6)
    Jump("loc_92E")

    label("loc_820")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_83C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_849")

    label("loc_83C")

    RunExpression(0x2, (scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_849")

    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_865")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_872")

    label("loc_865")

    RunExpression(0x3, (scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_872")

    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_892")
    Call(0, 6)
    Jump("loc_92E")

    label("loc_892")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8AB")
    Call(0, 5)
    Jump("loc_92E")

    label("loc_8AB")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_8E3"),
        (1, "loc_8EB"),
        (2, "loc_8F3"),
        (3, "loc_8FB"),
        (4, "loc_903"),
        (5, "loc_90B"),
        (6, "loc_913"),
        (7, "loc_91B"),
        (8, "loc_923"),
        (SWITCH_DEFAULT, "loc_92B"),
    )


    label("loc_8E3")

    OP_22(0x118, 0x0, 0x64)
    Jump("loc_92B")

    label("loc_8EB")

    OP_22(0x118, 0x0, 0x5A)
    Jump("loc_92B")

    label("loc_8F3")

    OP_22(0x118, 0x0, 0x50)
    Jump("loc_92B")

    label("loc_8FB")

    OP_22(0x118, 0x0, 0x46)
    Jump("loc_92B")

    label("loc_903")

    OP_22(0x118, 0x0, 0x3C)
    Jump("loc_92B")

    label("loc_90B")

    OP_22(0x118, 0x0, 0x32)
    Jump("loc_92B")

    label("loc_913")

    OP_22(0x118, 0x0, 0x28)
    Jump("loc_92B")

    label("loc_91B")

    OP_22(0x118, 0x0, 0x1E)
    Jump("loc_92B")

    label("loc_923")

    OP_22(0x118, 0x0, 0x14)
    Jump("loc_92B")

    label("loc_92B")

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_92E")

    Return()

    # Function_4_74A end

    def Function_5_92F(): pass

    label("Function_5_92F")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94F")
    Call(0, 9)
    FadeToBright(0, 0)
    Call(0, 10)

    label("loc_94F")

    FadeToDark(0, 0, -1)
    OP_0D()
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_972"),
        (105, "loc_9ED"),
        (107, "loc_A68"),
        (106, "loc_AE3"),
        (SWITCH_DEFAULT, "loc_AE3"),
    )


    label("loc_972")

    SetChrPos(0x101, -21430, 10, 3270, 0)
    SetChrPos(0x103, -22780, -10, 3150, 0)
    SetChrPos(0xF8, -21320, 0, 1950, 0)
    SetChrPos(0xF9, -22600, 0, 1850, 0)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jump("loc_B5E")

    label("loc_9ED")

    SetChrPos(0x101, -22600, 0, 1850, 180)
    SetChrPos(0x103, -21320, 0, 1950, 180)
    SetChrPos(0xF8, -22780, -10, 3150, 180)
    SetChrPos(0xF9, -21430, 10, 3270, 180)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jump("loc_B5E")

    label("loc_A68")

    SetChrPos(0x101, -21430, 10, 3270, 90)
    SetChrPos(0x103, -21320, 0, 1950, 90)
    SetChrPos(0xF8, -22780, -10, 3150, 90)
    SetChrPos(0xF9, -22600, 0, 1850, 90)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jump("loc_B5E")

    label("loc_AE3")

    SetChrPos(0x101, -22780, -10, 3150, 270)
    SetChrPos(0x103, -22600, 0, 1850, 270)
    SetChrPos(0xF8, -21430, 10, 3270, 270)
    SetChrPos(0xF9, -21320, 0, 1950, 270)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jump("loc_B5E")

    label("loc_B5E")

    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x118, 0x0, 0x50)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)

    ChrTalk(    #16
        0x101,
        (
            "#1015F对了，雪拉姐……\x02\x03",

            "觉不觉得从刚才开始\x01",
            "铃声就变大了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x103,
        (
            "#022F嗯嗯，没错。\x02\x03",

            "说不定……\x01",
            "线索就藏在铃声之中。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1826)
    OP_28(0x92, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_5_92F end

    def Function_6_C0A(): pass

    label("Function_6_C0A")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x308, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C19")
    OP_2B(0x92, 0x3)

    label("loc_C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C37")
    Call(0, 9)
    FadeToBright(0, 0)
    Call(0, 10)

    label("loc_C37")

    FadeToDark(0, 0, -1)
    OP_0D()
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_C5A"),
        (105, "loc_CD5"),
        (107, "loc_D50"),
        (106, "loc_DCB"),
        (SWITCH_DEFAULT, "loc_DCB"),
    )


    label("loc_C5A")

    SetChrPos(0x101, -21430, 10, 3270, 0)
    SetChrPos(0x103, -22780, -10, 3150, 0)
    SetChrPos(0xF8, -21320, 0, 1950, 0)
    SetChrPos(0xF9, -22600, 0, 1850, 0)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jump("loc_E46")

    label("loc_CD5")

    SetChrPos(0x101, -22600, 0, 1850, 180)
    SetChrPos(0x103, -21320, 0, 1950, 180)
    SetChrPos(0xF8, -22780, -10, 3150, 180)
    SetChrPos(0xF9, -21430, 10, 3270, 180)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jump("loc_E46")

    label("loc_D50")

    SetChrPos(0x101, -21430, 10, 3270, 90)
    SetChrPos(0x103, -21320, 0, 1950, 90)
    SetChrPos(0xF8, -22780, -10, 3150, 90)
    SetChrPos(0xF9, -22600, 0, 1850, 90)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jump("loc_E46")

    label("loc_DCB")

    SetChrPos(0x101, -22780, -10, 3150, 270)
    SetChrPos(0x103, -22600, 0, 1850, 270)
    SetChrPos(0xF8, -21430, 10, 3270, 270)
    SetChrPos(0xF9, -21320, 0, 1950, 270)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jump("loc_E46")

    label("loc_E46")

    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x308, 2)), scpexpr(EXPR_END)), "loc_1014")
    Sleep(500)

    ChrTalk(    #18
        0x101,
        (
            "#1007F从刚才开始就感觉\x01",
            "一直在同一个地方绕……\x02\x03",

            "#1015F怎么办好呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x103,
        (
            "#522F……是啊………\x02\x03",

            "#022F不过，可以肯定，\x01",
            "线索一定就是铃声的大小。\x02\x03",

            "只要能抓住这个法则就一定……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x118, 0x0, 0x64)
    OP_20(0xBB8)
    StopSound(0x64, 0x2710, 0x1770)
    Sleep(3000)

    ChrTalk(    #20
        0x101,
        "#1020F又来了……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F69")

    ChrTalk(    #21
        0x107,
        "#065F啊哇哇……\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF0")

    label("loc_F69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F8B")

    ChrTalk(    #22
        0x105,
        "#043F啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF0")

    label("loc_F8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FAD")

    ChrTalk(    #23
        0x104,
        "#033F噢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF0")

    label("loc_FAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FD1")

    ChrTalk(    #24
        0x106,
        "#057F可恶……\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF0")

    label("loc_FD1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FF0")

    ChrTalk(    #25
        0x108,
        "#072F呼……\x02",
    )

    CloseMessageWindow()

    label("loc_FF0")


    ChrTalk(    #26
        0x103,
        "#025F……似乎到时间了………\x02",
    )

    CloseMessageWindow()
    Jump("loc_1114")

    label("loc_1014")

    OP_22(0x118, 0x0, 0x64)
    OP_20(0xBB8)
    StopSound(0x64, 0x2710, 0x1770)
    Sleep(3000)

    ChrTalk(    #27
        0x101,
        "#1005F又来了……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_106C")

    ChrTalk(    #28
        0x107,
        "#065F啊哇哇……\x02",
    )

    CloseMessageWindow()
    Jump("loc_10F3")

    label("loc_106C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_108E")

    ChrTalk(    #29
        0x105,
        "#043F啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_10F3")

    label("loc_108E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10B0")

    ChrTalk(    #30
        0x104,
        "#033F噢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_10F3")

    label("loc_10B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10D4")

    ChrTalk(    #31
        0x106,
        "#057F可恶……\x02",
    )

    CloseMessageWindow()
    Jump("loc_10F3")

    label("loc_10D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F3")

    ChrTalk(    #32
        0x108,
        "#072F呼……\x02",
    )

    CloseMessageWindow()

    label("loc_10F3")


    ChrTalk(    #33
        0x103,
        "#022F……似乎走出来了………\x02",
    )

    CloseMessageWindow()

    label("loc_1114")

    Sleep(2000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C0303   ._SN", 100, 20, 0)
    IdleLoop()
    Return()

    # Function_6_C0A end

    def Function_7_1126(): pass

    label("Function_7_1126")

    EventBegin(0x0)
    SetChrPos(0x101, 8300, 0, 5920, 0)
    OP_6D(8300, 0, 5920, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(148000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #34
        0x101,
        "#1000F咦……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    OP_8C(0x101, 270, 400)
    Sleep(500)
    OP_8C(0x101, 180, 400)
    Sleep(1000)

    ChrTalk(    #35
        0x101,
        (
            "#1000F这，是哪里……？\x02\x03",

            "雪拉姐，大家……\x02\x03",

            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x1828)
    OP_28(0x92, 0x1, 0x20)
    OP_28(0x92, 0x1, 0x40)
    OP_28(0x92, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_7_1126 end

    def Function_8_1226(): pass

    label("Function_8_1226")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_123B")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_123B")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1260")
    EventBegin(0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T0300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1260")

    Return()

    # Function_8_1226 end

    def Function_9_1261(): pass

    label("Function_9_1261")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_12DE"),
        (1, "loc_12E4"),
        (SWITCH_DEFAULT, "loc_12EA"),
    )


    label("loc_12DE")

    OP_A2(0x1200)
    Jump("loc_12EA")

    label("loc_12E4")

    OP_A2(0x1201)
    Jump("loc_12EA")

    label("loc_12EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_12F8")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_12FC")

    label("loc_12F8")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_12FC")

    Return()

    # Function_9_1261 end

    def Function_10_12FD(): pass

    label("Function_10_12FD")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_10_12FD end

    def Function_11_134F(): pass

    label("Function_11_134F")

    OP_1F(0x50, 0xC8)
    Return()

    # Function_11_134F end

    SaveToFile()

Try(main)
