from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'P7000   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'P7000.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60211",
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
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 250,
        TriggerY            = 8380,
        TriggerRange        = 800,
        ActorX              = 0,
        ActorZ              = 1250,
        ActorY              = 8380,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5940,
        TriggerZ            = 250,
        TriggerY            = 13900,
        TriggerRange        = 800,
        ActorX              = -5940,
        ActorZ              = 1250,
        ActorY              = 13900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 15830,
        TriggerZ            = 0,
        TriggerY            = 15070,
        TriggerRange        = 1600,
        ActorX              = 15830,
        ActorZ              = 1000,
        ActorY              = 15070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_116",          # 00, 0
        "Function_1_190",          # 01, 1
        "Function_2_223",          # 02, 2
        "Function_3_22F",          # 03, 3
        "Function_4_134B",         # 04, 4
        "Function_5_2A2F",         # 05, 5
        "Function_6_2CDB",         # 06, 6
        "Function_7_3206",         # 07, 7
        "Function_8_3506",         # 08, 8
        "Function_9_48CF",         # 09, 9
        "Function_10_48E4",        # 0A, 10
        "Function_11_48F9",        # 0B, 11
        "Function_12_4922",        # 0C, 12
        "Function_13_494B",        # 0D, 13
        "Function_14_5841",        # 0E, 14
        "Function_15_599A",        # 0F, 15
        "Function_16_59DA",        # 10, 16
        "Function_17_5A1A",        # 11, 17
        "Function_18_5A5A",        # 12, 18
        "Function_19_5A9A",        # 13, 19
    )


    def Function_0_116(): pass

    label("Function_0_116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_135")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)
    Jump("loc_153")

    label("loc_135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_153")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_153")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18F")
    Event(0, 8)

    label("loc_18F")

    Return()

    # Function_0_116 end

    def Function_1_190(): pass

    label("Function_1_190")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDFC60, 0x23007C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BB")

    OP_1B(0x0, 0x0, 0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 7)), scpexpr(EXPR_END)), "loc_1D9")
    OP_64(0x0, 0x1)
    OP_71(0x1000, 0x0)
    ExitThread()
    OP_1C(0x0, 0x0, 0x2)
    Jump("loc_1DF")

    label("loc_1D9")

    OP_72(0x1000, 0x0)
    ExitThread()

    label("loc_1DF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F8")
    OP_64(0x1, 0x1)
    OP_71(0x1003, 0x0)
    ExitThread()
    Jump("loc_1FE")

    label("loc_1F8")

    OP_72(0x1003, 0x0)
    ExitThread()

    label("loc_1FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 6)), scpexpr(EXPR_END)), "loc_215")
    OP_72(0x1004, 0x0)
    ExitThread()
    OP_6F(0x4, 15)
    Jump("loc_222")

    label("loc_215")

    OP_72(0x1004, 0x0)
    ExitThread()
    OP_6F(0x4, 0)

    label("loc_222")

    Return()

    # Function_1_190 end

    def Function_2_223(): pass

    label("Function_2_223")

    TalkBegin(0xFF)
    Sleep(500)
    TalkEnd(0xFF)
    Return()

    # Function_2_223 end

    def Function_3_22F(): pass

    label("Function_3_22F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(500, -250, -38000, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(44000, 0)
    OP_6E(304, 0)
    SetChrPos(0x109, -680, -250, -37490, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CD")
    SetChrPos(0xEF, 700, -250, -37780, 0)
    SetChrPos(0xF0, -640, -250, -39170, 0)
    SetChrPos(0xF1, 960, -250, -39410, 0)
    Jump("loc_352")

    label("loc_2CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_311")
    SetChrPos(0xF0, 700, -250, -37780, 0)
    SetChrPos(0xEF, -640, -250, -39170, 0)
    SetChrPos(0xF1, 960, -250, -39410, 0)
    Jump("loc_352")

    label("loc_311")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_352")
    SetChrPos(0xF1, 700, -250, -37780, 0)
    SetChrPos(0xEF, -640, -250, -39170, 0)
    SetChrPos(0xF0, 960, -250, -39410, 0)

    label("loc_352")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_393():
        OP_6D(800, -250, -29760, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_393)

    def lambda_3AB():
        OP_67(0, 6800, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_3AB)

    def lambda_3C3():
        OP_6B(2660, 4000)
        ExitThread()

    QueueWorkItem(0xF0, 2, lambda_3C3)

    def lambda_3D3():
        OP_6E(294, 4000)
        ExitThread()

    QueueWorkItem(0xF1, 2, lambda_3D3)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3ED():
        OP_8E(0xFE, 0xFFFFFC90, 0xFFFFFF06, 0xFFFF8A1C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3ED)

    def lambda_408():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_408)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BB")

    def lambda_42D():
        OP_8E(0xFE, 0x1E0, 0xFFFFFF06, 0xFFFF89E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_42D)

    def lambda_448():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_448)
    Sleep(100)

    def lambda_45F():
        OP_8E(0xFE, 0xFFFFFB32, 0xFFFFFF06, 0xFFFF83AA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_45F)

    def lambda_47A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_47A)
    Sleep(100)

    def lambda_491():
        OP_8E(0xFE, 0x154, 0xFFFFFF06, 0xFFFF831E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_491)

    def lambda_4AC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_4AC)
    Jump("loc_5FC")

    label("loc_4BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55D")

    def lambda_4CF():
        OP_8E(0xFE, 0x1E0, 0xFFFFFF06, 0xFFFF89E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_4CF)

    def lambda_4EA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_4EA)
    Sleep(100)

    def lambda_501():
        OP_8E(0xFE, 0xFFFFFB32, 0xFFFFFF06, 0xFFFF83AA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_501)

    def lambda_51C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_51C)
    Sleep(100)

    def lambda_533():
        OP_8E(0xFE, 0x154, 0xFFFFFF06, 0xFFFF831E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_533)

    def lambda_54E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_54E)
    Jump("loc_5FC")

    label("loc_55D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FC")

    def lambda_571():
        OP_8E(0xFE, 0x1E0, 0xFFFFFF06, 0xFFFF89E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_571)

    def lambda_58C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_58C)
    Sleep(100)

    def lambda_5A3():
        OP_8E(0xFE, 0xFFFFFB32, 0xFFFFFF06, 0xFFFF83AA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_5A3)

    def lambda_5BE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_5BE)
    Sleep(100)

    def lambda_5D5():
        OP_8E(0xFE, 0x154, 0xFFFFFF06, 0xFFFF831E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_5D5)

    def lambda_5F0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_5F0)

    label("loc_5FC")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x2)
    Sleep(500)

    ChrTalk(    #0
        0x10F,
        "#1444F#11P咦………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x109,
        "#1065F#5P……果然。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B3")
    OP_A2(0x0)

    ChrTalk(    #2
        0x101,
        (
            "#1004F#6P这里……\x02\x03",

            "看起来好像\x01",
            "不是艾尔贝离宫啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF6")

    label("loc_6B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_711")
    OP_A2(0x2)

    ChrTalk(    #3
        0x102,
        (
            "#1502F#6P这里……\x02\x03",

            "好像不是\x01",
            "艾尔贝离宫啊。\x02",
        )
    )

    Jump("loc_70D")

    label("loc_70D")

    CloseMessageWindow()
    Jump("loc_AF6")

    label("loc_711")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_767")
    OP_A2(0x5)

    ChrTalk(    #4
        0x110,
        (
            "#1306F#6P哎呀……\x02\x03",

            "好像来到了\x01",
            "另外一个地方呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF6")

    label("loc_767")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7CA")
    OP_A2(0x1)

    ChrTalk(    #5
        0x107,
        (
            "#065F#6P这、这里……\x02\x03",

            "好像不是\x01",
            "艾尔贝离宫啊……\x02",
        )
    )

    Jump("loc_7C6")

    label("loc_7C6")

    CloseMessageWindow()
    Jump("loc_AF6")

    label("loc_7CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81F")
    OP_A2(0x3)

    ChrTalk(    #6
        0x10A,
        (
            "#814F#6P咦……\x02\x03",

            "艾尔贝离宫\x01",
            "是这样一种地方吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF6")

    label("loc_81F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_87A")

    ChrTalk(    #7
        0x105,
        (
            "#1162F#6P这里……\x02\x03",

            "好像不是\x01",
            "艾尔贝离宫啊。\x02",
        )
    )

    Jump("loc_876")

    label("loc_876")

    CloseMessageWindow()
    Jump("loc_AF6")

    label("loc_87A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8D5")

    ChrTalk(    #8
        0x103,
        (
            "#1522F#6P这里……\x02\x03",

            "好像不是\x01",
            "艾尔贝离宫啊。\x02",
        )
    )

    Jump("loc_8D1")

    label("loc_8D1")

    CloseMessageWindow()
    Jump("loc_AF6")

    label("loc_8D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_92F")

    ChrTalk(    #9
        0x106,
        (
            "#555F#6P这里……\x02\x03",

            "好像不是\x01",
            "艾尔贝离宫啊。\x02",
        )
    )

    Jump("loc_92B")

    label("loc_92B")

    CloseMessageWindow()
    Jump("loc_AF6")

    label("loc_92F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_989")

    ChrTalk(    #10
        0x108,
        (
            "#072F#6P这里……\x02\x03",

            "好像不是\x01",
            "艾尔贝离宫啊。\x02",
        )
    )

    Jump("loc_985")

    label("loc_985")

    CloseMessageWindow()
    Jump("loc_AF6")

    label("loc_989")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E3")

    ChrTalk(    #11
        0x10E,
        (
            "#178F#6P这里……\x02\x03",

            "好像不是\x01",
            "艾尔贝离宫啊。\x02",
        )
    )

    Jump("loc_9DF")

    label("loc_9DF")

    CloseMessageWindow()
    Jump("loc_AF6")

    label("loc_9E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A3E")

    ChrTalk(    #12
        0x104,
        (
            "#1542F#6P这里……\x02\x03",

            "好像不是\x01",
            "艾尔贝离宫啊。\x02",
        )
    )

    Jump("loc_A3A")

    label("loc_A3A")

    CloseMessageWindow()
    Jump("loc_AF6")

    label("loc_A3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A98")

    ChrTalk(    #13
        0x10C,
        (
            "#112F#6P这里……\x02\x03",

            "好像不是\x01",
            "艾尔贝离宫啊。\x02",
        )
    )

    Jump("loc_A94")

    label("loc_A94")

    CloseMessageWindow()
    Jump("loc_AF6")

    label("loc_A98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF6")
    OP_A2(0x4)

    ChrTalk(    #14
        0x10B,
        (
            "#216F#6P这、这里……\x02\x03",

            "好像和刚才的地方\x01",
            "气氛明显不一样……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B32")

    ChrTalk(    #15
        0x109,
        "#1840F#5P是啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_B50")

    label("loc_B32")


    ChrTalk(    #16
        0x109,
        "#1840F#5P是啊……\x02",
    )

    CloseMessageWindow()

    label("loc_B50")

    OP_1D(0xB2)

    def lambda_B58():
        OP_6D(0, 8000, -26000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_B58)

    def lambda_B70():
        OP_67(0, 3800, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_B70)

    def lambda_B88():
        OP_6B(2670, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_B88)

    def lambda_B98():
        OP_6C(0, 6000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_B98)

    def lambda_BA8():
        OP_6E(335, 6000)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_BA8)
    Sleep(1000)

    def lambda_BBD():
        OP_8F(0xFE, 0x0, 0xFFFFFF06, 0xFFFF9DC2, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BBD)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0x109, 0x0)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2C")
    SetChrPos(0xEF, 780, -250, -29300, 0)
    SetChrPos(0xF0, -650, -250, -31120, 0)
    SetChrPos(0xF1, 1260, -250, -31070, 0)
    Jump("loc_CB1")

    label("loc_C2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C70")
    SetChrPos(0xF0, 780, -250, -29300, 0)
    SetChrPos(0xEF, -650, -250, -31120, 0)
    SetChrPos(0xF1, 1260, -250, -31070, 0)
    Jump("loc_CB1")

    label("loc_C70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB1")
    SetChrPos(0xF1, 780, -250, -29300, 0)
    SetChrPos(0xEF, -650, -250, -31120, 0)
    SetChrPos(0xF0, 1260, -250, -31070, 0)

    label("loc_CB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC2")
    Jump("loc_CE1")

    label("loc_CC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD3")
    Jump("loc_CE1")

    label("loc_CD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE1")

    label("loc_CE1")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D1E")

    ChrTalk(    #17
        0x10D,
        "#273F#5P星杯的纹章……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF8")

    label("loc_D1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D56")

    ChrTalk(    #18
        0x10B,
        "#213F#5P星杯的标记……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF8")

    label("loc_D56")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D8E")

    ChrTalk(    #19
        0x10C,
        "#113F#5P星杯的纹章……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF8")

    label("loc_D8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DC7")

    ChrTalk(    #20
        0x104,
        "#1543F#5P星杯的纹章……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF8")

    label("loc_DC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DFF")

    ChrTalk(    #21
        0x10E,
        "#173F#5P星杯的纹章……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF8")

    label("loc_DFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E37")

    ChrTalk(    #22
        0x108,
        "#073F#5P星杯的纹章……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF8")

    label("loc_E37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E6F")

    ChrTalk(    #23
        0x106,
        "#052F#5P星杯的纹章……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF8")

    label("loc_E6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EA8")

    ChrTalk(    #24
        0x103,
        "#1523F#5P星杯的纹章……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF8")

    label("loc_EA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE1")

    ChrTalk(    #25
        0x105,
        "#1164F#5P星杯的纹章……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF8")

    label("loc_EE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F19")

    ChrTalk(    #26
        0x10A,
        "#814F#5P星杯的纹章……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF8")

    label("loc_F19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F51")

    ChrTalk(    #27
        0x107,
        "#064F#5P星杯的纹章……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF8")

    label("loc_F51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F89")

    ChrTalk(    #28
        0x110,
        "#264F#5P星杯的纹章……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF8")

    label("loc_F89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FC2")

    ChrTalk(    #29
        0x102,
        "#1504F#5P星杯的纹章……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF8")

    label("loc_FC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FF8")

    ChrTalk(    #30
        0x101,
        "#1004F#5P星杯的纹章……！？\x02",
    )

    CloseMessageWindow()

    label("loc_FF8")


    ChrTalk(    #31
        0x10F,
        "#1802F#5P凯文……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x109,
        "#1067F#5P………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_104A():
        OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFA434, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_104A)
    Sleep(500)
    Fade(1000)
    OP_6D(0, 600, -23500, 0)
    OP_67(0, 3160, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(345, 0)

    def lambda_10AC():
        OP_6D(0, 300, -23500, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_10AC)

    def lambda_10C4():
        OP_67(0, 3220, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_10C4)

    def lambda_10DC():
        OP_6B(3000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_10DC)

    def lambda_10EC():
        OP_6E(312, 6000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_10EC)
    WaitChrThread(0x109, 0x0)
    Sleep(1000)
    OP_22(0x176, 0x0, 0x64)
    OP_B0(0x4, 0x5)
    OP_6F(0x4, 0)
    OP_70(0x4, 0xF)
    OP_73(0x4)
    WaitChrThread(0xEE, 0x1)
    OP_8C(0x109, 180, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11F4")

    ChrTalk(    #33
        0x109,
        (
            "#1075F#5P──这里是『紫苑之家』。\x02\x03",

            "#1840F是我和莉丝，\x01",
            "以及露菲娜姐姐\x01",
            "一起生活过的地方。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125F")

    label("loc_11F4")


    ChrTalk(    #34
        0x109,
        (
            "#1075F#5P──这里是『紫苑之家』。\x02\x03",

            "#1840F是我和莉丝，\x01",
            "以及露菲娜姐姐\x01",
            "一起生活过的地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_125F")


    def lambda_1265():
        OP_6B(2500, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1265)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0xEE, 0x0)
    Sleep(2000)
    OP_A2(0x2B2E)
    OP_AD(0x2400F2, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x2582)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x15B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存】\x01",              # 0
            "【继续下面剧情】\x01",      # 1
        )
    )

    Jump("loc_12EE")

    label("loc_12EE")

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1302")
    ShowSaveMenu()

    label("loc_1302")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_20(0x7D0)
    OP_21()
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_A3(0x2582)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2504)
    NewScene("ED6_DT21/P7000   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_3_22F end

    def Function_4_134B(): pass

    label("Function_4_134B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(2000)
    OP_AD(0x2400E9, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x109, -320, -250, -22480, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AF")
    SetChrPos(0xEF, -600, -250, -25060, 0)
    SetChrPos(0xF0, -1000, -250, -27000, 0)
    SetChrPos(0xF1, 470, -250, -27430, 0)
    Jump("loc_1534")

    label("loc_14AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F3")
    SetChrPos(0xF0, -600, -250, -25060, 0)
    SetChrPos(0xEF, -1000, -250, -27000, 0)
    SetChrPos(0xF1, 470, -250, -27430, 0)
    Jump("loc_1534")

    label("loc_14F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1534")
    SetChrPos(0xF1, -600, -250, -25060, 0)
    SetChrPos(0xEF, -1000, -250, -27000, 0)
    SetChrPos(0xF0, 470, -250, -27430, 0)

    label("loc_1534")

    OP_6D(-2170, -450, -17930, 0)
    OP_67(0, 8520, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(315000, 0)
    OP_6E(422, 0)
    OP_1D(0xD3)

    def lambda_1579():
        OP_8E(0xFE, 0x82, 0xFFFFFF06, 0x6FE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1579)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15FF")

    def lambda_15A7():
        OP_8E(0xFE, 0xFFFFFFF6, 0xFFFFFF06, 0x118, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_15A7)
    Sleep(100)

    def lambda_15C7():
        OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFF06, 0xFFFFFB00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_15C7)
    Sleep(100)

    def lambda_15E7():
        OP_8E(0xFE, 0x384, 0xFFFFFF06, 0xFFFFFABA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_15E7)
    Jump("loc_16D4")

    label("loc_15FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_166B")

    def lambda_1613():
        OP_8E(0xFE, 0xFFFFFFF6, 0xFFFFFF06, 0x118, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1613)
    Sleep(100)

    def lambda_1633():
        OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFF06, 0xFFFFFB00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1633)
    Sleep(100)

    def lambda_1653():
        OP_8E(0xFE, 0x384, 0xFFFFFF06, 0xFFFFFABA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1653)
    Jump("loc_16D4")

    label("loc_166B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16D4")

    def lambda_167F():
        OP_8E(0xFE, 0xFFFFFFF6, 0xFFFFFF06, 0x118, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_167F)
    Sleep(100)

    def lambda_169F():
        OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFF06, 0xFFFFFB00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_169F)
    Sleep(100)

    def lambda_16BF():
        OP_8E(0xFE, 0x384, 0xFFFFFF06, 0xFFFFFABA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_16BF)

    label("loc_16D4")


    def lambda_16DA():
        OP_6B(3400, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_16DA)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2000)
    Fade(1000)
    OP_44(0xEE, 0x1)
    OP_6D(-14220, 150, 2220, 0)
    OP_67(0, 6850, -10000, 0)
    OP_6B(3820, 0)
    OP_6C(315000, 0)
    OP_6E(439, 0)

    def lambda_173F():
        OP_6D(-14220, 150, -3430, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_173F)

    def lambda_1757():
        OP_8E(0xFE, 0x82, 0xFFFFFF06, 0x6FE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1757)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17CE")

    def lambda_1780():
        OP_8E(0xFE, 0xFFFFFFF6, 0xFFFFFF06, 0x118, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1780)

    def lambda_179B():
        OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFF06, 0xFFFFFB00, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_179B)

    def lambda_17B6():
        OP_8E(0xFE, 0x384, 0xFFFFFF06, 0xFFFFFABA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_17B6)
    Jump("loc_188F")

    label("loc_17CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1830")

    def lambda_17E2():
        OP_8E(0xFE, 0xFFFFFFF6, 0xFFFFFF06, 0x118, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_17E2)

    def lambda_17FD():
        OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFF06, 0xFFFFFB00, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_17FD)

    def lambda_1818():
        OP_8E(0xFE, 0x384, 0xFFFFFF06, 0xFFFFFABA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1818)
    Jump("loc_188F")

    label("loc_1830")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_188F")

    def lambda_1844():
        OP_8E(0xFE, 0xFFFFFFF6, 0xFFFFFF06, 0x118, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1844)

    def lambda_185F():
        OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFF06, 0xFFFFFB00, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_185F)

    def lambda_187A():
        OP_8E(0xFE, 0x384, 0xFFFFFF06, 0xFFFFFABA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_187A)

    label("loc_188F")

    OP_0D()
    Sleep(3000)
    Fade(1000)
    OP_44(0xEE, 0x1)
    OP_6D(11330, -1100, 5620, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3840, 0)
    OP_6C(315000, 0)
    OP_6E(400, 0)

    def lambda_18E1():
        OP_6B(3500, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_18E1)
    OP_0D()
    Sleep(3000)
    Fade(1000)
    OP_44(0xEE, 0x1)
    OP_6D(-3520, -250, 15320, 0)
    OP_67(0, 8220, -10000, 0)
    OP_6B(4250, 0)
    OP_6C(315000, 0)
    OP_6E(398, 0)

    def lambda_193D():
        OP_6D(-3070, -250, 6170, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_193D)

    def lambda_1955():
        OP_8E(0xFE, 0x82, 0xFFFFFF06, 0x6FE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1955)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19CC")

    def lambda_197E():
        OP_8E(0xFE, 0xFFFFFFF6, 0xFFFFFF06, 0x118, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_197E)

    def lambda_1999():
        OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFF06, 0xFFFFFB00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1999)

    def lambda_19B4():
        OP_8E(0xFE, 0x384, 0xFFFFFF06, 0xFFFFFABA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_19B4)
    Jump("loc_1A8D")

    label("loc_19CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A2E")

    def lambda_19E0():
        OP_8E(0xFE, 0xFFFFFFF6, 0xFFFFFF06, 0x118, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_19E0)

    def lambda_19FB():
        OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFF06, 0xFFFFFB00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_19FB)

    def lambda_1A16():
        OP_8E(0xFE, 0x384, 0xFFFFFF06, 0xFFFFFABA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1A16)
    Jump("loc_1A8D")

    label("loc_1A2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A8D")

    def lambda_1A42():
        OP_8E(0xFE, 0xFFFFFFF6, 0xFFFFFF06, 0x118, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1A42)

    def lambda_1A5D():
        OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFF06, 0xFFFFFB00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1A5D)

    def lambda_1A78():
        OP_8E(0xFE, 0x384, 0xFFFFFF06, 0xFFFFFABA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1A78)

    label("loc_1A8D")

    OP_C8(0x80, 0x46, "C_PLAC36._CH", 0x1, 0x3E8)
    OP_0D()
    Sleep(1000)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Sleep(1000)
    Fade(1000)
    OP_44(0xEE, 0x1)
    OP_6D(-1600, -250, 3200, 0)
    OP_67(0, 4920, -10000, 0)
    OP_6B(3130, 0)
    OP_6C(315000, 0)
    OP_6E(270, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #35
        0x10F,
        (
            "#1802F#6P………怎么会………………\x02\x03",

            "这、这是……\x01",
            "只是再现出来的伪造场景……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x109,
        (
            "#1065F#5P啊啊……\x01",
            "简直要让人以为这就是真的了。\x02\x03",

            "#1840F怎么说呢……\x01",
            "连空气的味道都一模一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10F,
        "#1445F#6P……嗯。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C38")

    ChrTalk(    #38
        0x110,
        "#1300F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_1C38")

    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    OP_A3(0x3)
    OP_A3(0x4)
    OP_A3(0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CA9")

    ChrTalk(    #39
        0x103,
        (
            "#1522F#6P『紫苑之家』……\x02\x03",

            "好像是和七耀教会\x01",
            "有关的建筑吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2196")

    label("loc_1CA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D0A")

    ChrTalk(    #40
        0x105,
        (
            "#1163F#6P『紫苑之家』……\x02\x03",

            "看起来像是和\x01",
            "七耀教会有关的建筑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2196")

    label("loc_1D0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D7C")
    OP_A2(0x0)

    ChrTalk(    #41
        0x101,
        (
            "#1002F#6P哎……\x02\x03",

            "这里叫做『紫苑之家』吗……\x01",
            "是教会的建筑还是别的什么……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2196")

    label("loc_1D7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DE8")
    OP_A2(0x2)

    ChrTalk(    #42
        0x102,
        (
            "#1505F#6P『紫苑之家』……\x02\x03",

            "#1502F总之，\x01",
            "这里应该是七耀教会的设施吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2196")

    label("loc_1DE8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E5F")
    OP_A2(0x3)

    ChrTalk(    #43
        0x10A,
        (
            "#812F#6P哎，这个……\x02\x03",

            "这里叫做『紫苑之家』吗……\x01",
            "是教会的建筑还是别的什么……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2196")

    label("loc_1E5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EC6")

    ChrTalk(    #44
        0x106,
        (
            "#053F#6P『紫苑之家』……\x02\x03",

            "#050F看来应该是\x01",
            "跟七耀教会相关的建筑了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2196")

    label("loc_1EC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F29")

    ChrTalk(    #45
        0x108,
        (
            "#074F#6P『紫苑之家』……\x02\x03",

            "#072F看来是和七耀教会\x01",
            "相关的建筑了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2196")

    label("loc_1F29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F90")

    ChrTalk(    #46
        0x10E,
        (
            "#176F#6P『紫苑之家』……\x02\x03",

            "#178F总之，\x01",
            "这里应该是七耀教会的设施吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2196")

    label("loc_1F90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FF9")

    ChrTalk(    #47
        0x104,
        (
            "#1545F#6P『紫苑之家』……\x02\x03",

            "#1540F总之，\x01",
            "这里应该是七耀教会的设施吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2196")

    label("loc_1FF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2060")

    ChrTalk(    #48
        0x10D,
        (
            "#272F#6P『紫苑之家』……\x02\x03",

            "#270F总之，\x01",
            "这里应该是七耀教会的设施吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2196")

    label("loc_2060")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20C7")

    ChrTalk(    #49
        0x10C,
        (
            "#115F#6P『紫苑之家』……\x02\x03",

            "#112F总之，\x01",
            "这里应该是七耀教会的设施吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2196")

    label("loc_20C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2134")
    OP_A2(0x1)

    ChrTalk(    #50
        0x107,
        (
            "#062F#6P哎，这个……\x02\x03",

            "这里叫做『紫苑之家』吧，\x01",
            "果然还是教会的设施吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2196")

    label("loc_2134")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2196")
    OP_A2(0x4)

    ChrTalk(    #51
        0x10B,
        (
            "#212F#6P哎……\x02\x03",

            "这里叫做『紫苑之家』吧，\x01",
            "是七耀教会的设施吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2225")

    ChrTalk(    #52
        0x109,
        (
            "#1075F#5P嗯，\x01",
            "是教会运营的『福音设施』……\x02\x03",

            "#1840F总之，就是近似于修道院的，\x01",
            "孤儿院之类的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_229A")

    label("loc_2225")


    ChrTalk(    #53
        0x109,
        (
            "#1075F#5P嗯，\x01",
            "是教会运营的『福音设施』……\x02\x03",

            "#1840F总之，就是近似于修道院的，\x01",
            "孤儿院之类的地方吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_229A")

    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    OP_A3(0x3)
    OP_A3(0x4)
    OP_A3(0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_232E")

    ChrTalk(    #54
        0x103,
        (
            "#1525F#6P这样啊……\x02\x03",

            "#1532F…………………………………\x02\x03",

            "#1534F就是说……\x01",
            "难道你也是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2780")

    label("loc_232E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_238B")

    ChrTalk(    #55
        0x105,
        (
            "#1169F#6P是这样啊……\x02\x03",

            "#1382F那么，\x01",
            "难道凯文先生也是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2780")

    label("loc_238B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23F1")
    OP_A2(0x0)

    ChrTalk(    #56
        0x101,
        (
            "#1003F#6P是这样啊……\x02\x03",

            "#1025F那就是说……\x01",
            "难道凯文先生也是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2780")

    label("loc_23F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_244D")
    OP_A2(0x2)

    ChrTalk(    #57
        0x102,
        (
            "#1503F#6P果然……\x02\x03",

            "#1500F那么……\x01",
            "难道凯文先生也是？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2780")

    label("loc_244D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24B0")
    OP_A2(0x3)

    ChrTalk(    #58
        0x10A,
        (
            "#1316F#6P是这样啊……\x02\x03",

            "#810F那就是说……\x01",
            "难道凯文先生也是？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2780")

    label("loc_24B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_250B")

    ChrTalk(    #59
        0x106,
        (
            "#551F#6P是这样啊……\x02\x03",

            "#555F那就是说，\x01",
            "难不成你也是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2780")

    label("loc_250B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2564")

    ChrTalk(    #60
        0x108,
        (
            "#572F#6P是这样啊。\x02\x03",

            "#070F那就是说，\x01",
            "难不成你也是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2780")

    label("loc_2564")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25BF")

    ChrTalk(    #61
        0x10E,
        (
            "#175F#6P是这样啊……\x02\x03",

            "#170F那么……\x01",
            "难道凯文先生也……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2780")

    label("loc_25BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2615")

    ChrTalk(    #62
        0x104,
        (
            "#1540F#6P唔，原来如此。\x02\x03",

            "也就是说，你果然也是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2780")

    label("loc_2615")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2666")

    ChrTalk(    #63
        0x10D,
        (
            "#270F#6P原来如此。\x02\x03",

            "那么，神父先生果然也……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2780")

    label("loc_2666")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26BB")

    ChrTalk(    #64
        0x10C,
        (
            "#110F#6P是这样啊……\x02\x03",

            "可是，这样一来你不就是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2780")

    label("loc_26BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2723")
    OP_A2(0x1)

    ChrTalk(    #65
        0x107,
        (
            "#561F#6P是、是这样啊……\x02\x03",

            "#560F那就是说……\x01",
            "凯文哥哥难道也是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2780")

    label("loc_2723")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2780")
    OP_A2(0x4)

    ChrTalk(    #66
        0x10B,
        (
            "#215F#6P……是这样啊。\x02\x03",

            "#210F那就是说，\x01",
            "难不成你也是……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2833")

    ChrTalk(    #67
        0x109,
        (
            "#1075F#5P嗯，就是所谓的孤儿吧。\x02\x03",

            "#1840F因为一些事情，\x01",
            "在这里得到了照顾。\x02\x03",

            "#1067F算起来……\x01",
            "已经大概有五年\x01",
            "没有回到这里来了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28CC")

    label("loc_2833")


    ChrTalk(    #68
        0x109,
        (
            "#1075F#5P嗯，就是所谓的孤儿吧。\x02\x03",

            "#1840F因为一些事情，\x01",
            "在这里得到了照顾。\x02\x03",

            "#1067F算起来……\x01",
            "已经大概有五年\x01",
            "没有回到这里来了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28CC")


    ChrTalk(    #69
        0x10F,
        "#1445F#6P凯文……\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)

    def lambda_290A():
        OP_6D(-1600, -250, 2000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_290A)
    OP_8C(0x109, 180, 400)
    WaitChrThread(0x0, 0x1)
    Sleep(300)

    ChrTalk(    #70
        0x109,
        (
            "#1078F#11P总之……\x01",
            "前往『第七星层』的线索\x01",
            "一定就在这里面。\x02\x03",

            "首先，我们在这里\x01",
            "仔细调查一遍吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10F,
        "#1806F#6P嗯……是啊。\x02",
    )

    CloseMessageWindow()
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_A2(0x2C00)
    OP_28(0x37, 0x4, 0x10)
    OP_28(0x37, 0x4, 0x20)
    OP_28(0x38, 0x4, 0x10)
    OP_28(0x38, 0x4, 0x20)
    OP_28(0x39, 0x4, 0x10)
    OP_28(0x39, 0x4, 0x20)
    OP_28(0x3A, 0x4, 0x10)
    OP_28(0x3A, 0x4, 0x20)
    OP_28(0x3B, 0x4, 0x10)
    OP_28(0x3B, 0x4, 0x20)
    OP_28(0x3C, 0x4, 0x4)
    OP_28(0x3C, 0x4, 0x8)
    OP_28(0x3C, 0x1, 0x1)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_4_134B end

    def Function_5_2A2F(): pass

    label("Function_5_2A2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 2)), scpexpr(EXPR_END)), "loc_2A3E")
    Call(0, 13)
    Return()

    label("loc_2A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C8D")
    EventBegin(0x0)
    Fade(500)
    OP_6D(-520, 250, 7630, 0)
    OP_67(0, 5530, -10000, 0)
    OP_6B(3570, 0)
    OP_6C(315000, 0)
    OP_6E(225, 0)
    SetChrPos(0x109, 240, 250, 7560, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ADF")
    SetChrPos(0xEF, 280, -250, 6090, 0)
    SetChrPos(0xF0, -190, -250, 4650, 0)
    SetChrPos(0xF1, 1320, -250, 4570, 0)
    Jump("loc_2B64")

    label("loc_2ADF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B23")
    SetChrPos(0xF0, 280, -250, 6090, 0)
    SetChrPos(0xEF, -190, -250, 4650, 0)
    SetChrPos(0xF1, 1320, -250, 4570, 0)
    Jump("loc_2B64")

    label("loc_2B23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B64")
    SetChrPos(0xF1, 280, -250, 6090, 0)
    SetChrPos(0xEF, -190, -250, 4650, 0)
    SetChrPos(0xF0, 1320, -250, 4570, 0)

    label("loc_2B64")

    OP_0D()
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #72
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #73
        0x109,
        "#1067F#5P……果然。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10F,
        "#1802F#6P好像上着锁。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x109,
        (
            "#1840F#5P是啊……\x02\x03",

            "#1065F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #76
        0x109,
        "#1078F#11P算了，先到别的地方调查吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2C01)
    OP_28(0x3C, 0x1, 0x2)
    Sleep(300)
    EventEnd(0x0)
    Jump("loc_2CDA")

    label("loc_2C8D")

    TalkBegin(0xFF)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #77
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_2CDA")

    Return()

    # Function_5_2A2F end

    def Function_6_2CDB(): pass

    label("Function_6_2CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_319A")
    EventBegin(0x0)
    Fade(500)
    OP_6D(-6360, 250, 15270, 0)
    OP_67(0, 6870, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(248, 0)
    SetChrPos(0x109, -6690, 250, 13820, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D7C")
    SetChrPos(0xEF, -8390, 250, 13620, 90)
    SetChrPos(0xF0, -9870, 250, 14040, 90)
    SetChrPos(0xF1, -9820, 250, 12750, 90)
    Jump("loc_2E01")

    label("loc_2D7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DC0")
    SetChrPos(0xF0, -8390, 250, 13620, 90)
    SetChrPos(0xEF, -9870, 250, 14040, 90)
    SetChrPos(0xF1, -9820, 250, 12750, 90)
    Jump("loc_2E01")

    label("loc_2DC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E01")
    SetChrPos(0xF1, -8390, 250, 13620, 90)
    SetChrPos(0xEF, -9870, 250, 14040, 90)
    SetChrPos(0xF0, -9820, 250, 12750, 90)

    label("loc_2E01")

    OP_0D()
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #78
        (
            "\x07\x05门打不开。\x01",
            "而且上面并没有钥匙孔。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E9C")

    ChrTalk(    #79
        0x10C,
        "#112F#6P唔，这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30F2")

    label("loc_2E9C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2ECA")

    ChrTalk(    #80
        0x10D,
        "#270F#6P这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30F2")

    label("loc_2ECA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EFD")

    ChrTalk(    #81
        0x104,
        "#1543F#6P唔，这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30F2")

    label("loc_2EFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F2D")

    ChrTalk(    #82
        0x10E,
        "#178F#6P这是……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_30F2")

    label("loc_2F2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F59")

    ChrTalk(    #83
        0x108,
        "#073F#6P这是？\x02",
    )

    CloseMessageWindow()
    Jump("loc_30F2")

    label("loc_2F59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F89")

    ChrTalk(    #84
        0x106,
        "#555F#6P怎么回事？\x02",
    )

    CloseMessageWindow()
    Jump("loc_30F2")

    label("loc_2F89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FC4")

    ChrTalk(    #85
        0x10A,
        (
            "#814F#6P咦……\x01",
            "为什么打不开？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30F2")

    label("loc_2FC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FF2")

    ChrTalk(    #86
        0x107,
        "#064F#6P咦……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_30F2")

    label("loc_2FF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3026")

    ChrTalk(    #87
        0x110,
        "#267F#6P为什么打不开？\x02",
    )

    CloseMessageWindow()
    Jump("loc_30F2")

    label("loc_3026")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3057")

    ChrTalk(    #88
        0x102,
        "#1504F#6P这是……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_30F2")

    label("loc_3057")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3093")

    ChrTalk(    #89
        0x101,
        (
            "#1004F#6P咦……\x01",
            "到底怎么回事？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30F2")

    label("loc_3093")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30C4")

    ChrTalk(    #90
        0x103,
        "#1522F#6P怎么回事？\x02",
    )

    CloseMessageWindow()
    Jump("loc_30F2")

    label("loc_30C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30F2")

    ChrTalk(    #91
        0x105,
        "#1164F#6P这是……？\x02",
    )

    CloseMessageWindow()

    label("loc_30F2")


    def lambda_30F8():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_30F8)
    Sleep(100)
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #92
        0x10F,
        (
            "#1448F#11P……这是侧面的小门，\x01",
            "只有从里面才可以上锁和开锁。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x109,
        (
            "#1840F#11P要进入礼拜堂\x01",
            "只能走正面的门。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C02)
    Sleep(300)
    EventEnd(0x0)
    Jump("loc_3205")

    label("loc_319A")

    TalkBegin(0xFF)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #94
        (
            "\x07\x05门打不开。\x01",
            "而且上面并没有钥匙孔。\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)

    label("loc_3205")

    Return()

    # Function_6_2CDB end

    def Function_7_3206(): pass

    label("Function_7_3206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34B9")
    EventBegin(0x0)
    Fade(500)
    OP_6D(15000, 0, 15010, 0)
    OP_67(0, 6990, -10000, 0)
    OP_6B(3280, 0)
    OP_6C(0, 0)
    OP_6E(221, 0)
    SetChrPos(0x109, 14490, 0, 13580, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32A7")
    SetChrPos(0xEF, 15370, 0, 12430, 0)
    SetChrPos(0xF0, 13290, 0, 12680, 45)
    SetChrPos(0xF1, 14210, 0, 11570, 45)
    Jump("loc_332C")

    label("loc_32A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32EB")
    SetChrPos(0xF0, 15370, 0, 12430, 0)
    SetChrPos(0xEF, 13290, 0, 12680, 45)
    SetChrPos(0xF1, 14210, 0, 11570, 45)
    Jump("loc_332C")

    label("loc_32EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_332C")
    SetChrPos(0xF1, 15370, 0, 12430, 0)
    SetChrPos(0xEF, 13290, 0, 12680, 45)
    SetChrPos(0xF0, 14210, 0, 11570, 45)

    label("loc_332C")

    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #95
        (
            "\x07\x05有一口井。\x01",
            "看来水并没有干涸。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #96
        0x109,
        (
            "#1060F#5P这里是……\x01",
            "汲取饮用水的井。\x02\x03",

            "#1068F当时并没有导力泵，\x01",
            "只能用绳子和木桶来打水，\x01",
            "实在是很辛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x10F,
        (
            "#1446F#6P嗯……\x01",
            "确实很辛苦。\x02\x03",

            "冬天的早晨来打水的话，\x01",
            "手就会冻得通红……\x02\x03",

            "#1806F不过现在回想起来……\x01",
            "也挺有趣的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x109,
        "#1066F#5P哈哈，没错。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2C03)
    OP_28(0x3C, 0x1, 0x100)
    Sleep(300)
    EventEnd(0x0)
    Jump("loc_3505")

    label("loc_34B9")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #99
        (
            "\x07\x05有一口井。\x01",
            "看来水并没有干涸。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_3505")

    Return()

    # Function_7_3206 end

    def Function_8_3506(): pass

    label("Function_8_3506")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -13380, 250, -9700, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3567")
    SetChrPos(0xEF, -13380, 250, -9700, 90)
    SetChrPos(0xF0, -13380, 250, -9700, 90)
    SetChrPos(0xF1, -13380, 250, -9700, 90)
    Jump("loc_35EC")

    label("loc_3567")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35AB")
    SetChrPos(0xF0, -13380, 250, -9700, 90)
    SetChrPos(0xEF, -13380, 250, -9700, 90)
    SetChrPos(0xF1, -13380, 250, -9700, 90)
    Jump("loc_35EC")

    label("loc_35AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35EC")
    SetChrPos(0xF1, -13380, 250, -9700, 90)
    SetChrPos(0xEF, -13380, 250, -9700, 90)
    SetChrPos(0xF0, -13380, 250, -9700, 90)

    label("loc_35EC")

    OP_6D(-12370, 250, -8380, 0)
    OP_67(0, 6070, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(314000, 0)
    OP_6E(245, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_6F(0x1, 0)
    OP_70(0x1, 0xF)
    OP_73(0x1)
    Sleep(300)

    def lambda_365A():
        OP_6D(-7600, -250, -8460, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_365A)

    def lambda_3672():
        OP_67(0, 5330, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3672)
    OP_43(0x109, 0x0, 0x0, 0x9)
    Sleep(700)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36C0")
    OP_43(0xEF, 0x0, 0x0, 0xA)
    Sleep(600)
    OP_43(0xF0, 0x0, 0x0, 0xB)
    Sleep(700)
    OP_43(0xF1, 0x0, 0x0, 0xC)
    Jump("loc_371D")

    label("loc_36C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36F0")
    OP_43(0xF0, 0x0, 0x0, 0xA)
    Sleep(600)
    OP_43(0xEF, 0x0, 0x0, 0xB)
    Sleep(700)
    OP_43(0xF1, 0x0, 0x0, 0xC)
    Jump("loc_371D")

    label("loc_36F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_371D")
    OP_43(0xF1, 0x0, 0x0, 0xA)
    Sleep(600)
    OP_43(0xEF, 0x0, 0x0, 0xB)
    Sleep(700)
    OP_43(0xF0, 0x0, 0x0, 0xC)

    label("loc_371D")

    Sleep(1000)
    OP_6F(0x1, 15)
    OP_70(0x1, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x1)
    OP_71(0x1001, 0x0)
    ExitThread()
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x1)

    ChrTalk(    #100
        0x10F,
        (
            "#1445F#5P……什么也没找到。\x02\x03",

            "#1443F如果真的存在线索的话，\x01",
            "还应该是在礼拜堂里吧……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x109,
        (
            "#1067F#5P是啊……\x02\x03",

            "#1065F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #102
        0x10F,
        "#1802F#5P凯文……？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #103
        0x109,
        (
            "#1840F#6P……对了，莉丝。\x02\x03",

            "那一天……\x01",
            "担任礼拜堂值日生的\x01",
            "是不是你？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x10F,
        "#1444F#5P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x109,
        (
            "#1067F#6P这个『紫苑之家』最后的日子……\x02\x03",

            "#1065F五年前露菲娜姐姐\x01",
            "死去的那一天。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3947")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_39AE")

    label("loc_3947")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_396F")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_39AE")

    label("loc_396F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3997")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_39AE")

    label("loc_3997")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_39AE")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39DB")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3A42")

    label("loc_39DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A03")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3A42")

    label("loc_3A03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A2B")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3A42")

    label("loc_3A2B")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3A42")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A6F")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3AD6")

    label("loc_3A6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A97")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3AD6")

    label("loc_3A97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ABF")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3AD6")

    label("loc_3ABF")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3AD6")

    Sleep(1000)

    ChrTalk(    #106
        0x10F,
        "#1445F#5P………呜…………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B3C")

    ChrTalk(    #107
        0x101,
        "#1020F#5P凯、凯文先生？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BD9")

    label("loc_3B3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B70")

    ChrTalk(    #108
        0x107,
        "#065F#5P凯、凯文哥哥？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BD9")

    label("loc_3B70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BA5")

    ChrTalk(    #109
        0x10A,
        "#1317F#5P凯、凯文先生？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BD9")

    label("loc_3BA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BD9")

    ChrTalk(    #110
        0x105,
        "#1163F#5P凯文先生……！？\x02",
    )

    CloseMessageWindow()

    label("loc_3BD9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C08")

    ChrTalk(    #111
        0x110,
        "#1305F#5P嗯……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C62")

    label("loc_3C08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C36")

    ChrTalk(    #112
        0x10C,
        "#112F#5P唔……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C62")

    label("loc_3C36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C62")

    ChrTalk(    #113
        0x104,
        "#1542F#5P哦……？\x02",
    )

    CloseMessageWindow()

    label("loc_3C62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C9A")

    ChrTalk(    #114
        0x102,
        "#1502F#5P………难道……………\x02",
    )

    CloseMessageWindow()

    label("loc_3C9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CCE")

    ChrTalk(    #115
        0x10B,
        "#212F#5P你、你说什么？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DC4")

    label("loc_3CCE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CFF")

    ChrTalk(    #116
        0x103,
        "#1522F#5P什么……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DC4")

    label("loc_3CFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D2F")

    ChrTalk(    #117
        0x106,
        "#057F#5P什么……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DC4")

    label("loc_3D2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D5F")

    ChrTalk(    #118
        0x108,
        "#072F#5P什么……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DC4")

    label("loc_3D5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D8F")

    ChrTalk(    #119
        0x10E,
        "#178F#5P什么……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DC4")

    label("loc_3D8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DC4")

    ChrTalk(    #120
        0x10D,
        "#270F#5P……什么…………？\x02",
    )

    CloseMessageWindow()

    label("loc_3DC4")


    ChrTalk(    #121
        0x109,
        (
            "#1063F#6P在那个事件之后，\x01",
            "我拜访院长老师的时候\x01",
            "是这么听说的……\x02\x03",

            "怎么样……没错吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x10F,
        (
            "#1445F#5P……嗯、嗯…………\x02\x03",

            "#1802F你说的……没错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x109,
        (
            "#1075F#6P是吗……\x02\x03",

            "#1840F那么……莉丝。\x01",
            "你在怀里或者口袋里找一下。\x02\x03",

            "应该能找到礼拜堂的钥匙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x10F,
        "#1444F#5P咦……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #125
        (
            "\x07\x05莉丝在修道服中找了找。\x02\x03",

            "从胸前的口袋中\x01",
            "找到了一把老旧的黄铜钥匙。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #126
        "\x07\x00得到了\x1F\x38\x03\x07\x00。\x02",
    )

    Jump("loc_3FA2")

    label("loc_3FA2")

    CloseMessageWindow()
    OP_3E(0x338, 1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FE4")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_404B")

    label("loc_3FE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_400C")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_404B")

    label("loc_400C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4034")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_404B")

    label("loc_4034")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_404B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4078")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_40DF")

    label("loc_4078")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40A0")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_40DF")

    label("loc_40A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40C8")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_40DF")

    label("loc_40C8")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_40DF")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_410C")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4173")

    label("loc_410C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4134")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4173")

    label("loc_4134")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_415C")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4173")

    label("loc_415C")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4173")

    Sleep(1000)

    ChrTalk(    #127
        0x10F,
        "#1802F#5P啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41CA")

    ChrTalk(    #128
        0x101,
        "#1004F#5P不、不会吧……！？\x02",
    )

    CloseMessageWindow()

    label("loc_41CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41F8")

    ChrTalk(    #129
        0x105,
        "#1164F#5P那是……！\x02",
    )

    CloseMessageWindow()

    label("loc_41F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_422F")

    ChrTalk(    #130
        0x10B,
        "#216F#5P开、开玩笑的吧……？\x02",
    )

    CloseMessageWindow()

    label("loc_422F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_425E")

    ChrTalk(    #131
        0x106,
        "#055F#5P骗人的吧……\x02",
    )

    CloseMessageWindow()

    label("loc_425E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4290")

    ChrTalk(    #132
        0x103,
        "#1525F#5P真让人吃惊……\x02",
    )

    CloseMessageWindow()

    label("loc_4290")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42BB")

    ChrTalk(    #133
        0x10E,
        "#173F#5P什么……\x02",
    )

    CloseMessageWindow()

    label("loc_42BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42F0")

    ChrTalk(    #134
        0x10A,
        "#814F#5P为、为什么……！？\x02",
    )

    CloseMessageWindow()

    label("loc_42F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4319")

    ChrTalk(    #135
        0x10D,
        "#276F#5P唔……\x02",
    )

    CloseMessageWindow()

    label("loc_4319")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4348")

    ChrTalk(    #136
        0x108,
        "#074F#5P是这样啊……\x02",
    )

    CloseMessageWindow()

    label("loc_4348")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4477")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4381")

    ChrTalk(    #137
        0x10C,
        "#115F#5P是吗……\x02",
    )

    CloseMessageWindow()

    label("loc_4381")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43AD")

    ChrTalk(    #138
        0x110,
        "#1306F#5P哎呀……\x02",
    )

    CloseMessageWindow()

    label("loc_43AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43D7")

    ChrTalk(    #139
        0x102,
        "#1504F#5P啊……\x02",
    )

    CloseMessageWindow()

    label("loc_43D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4404")

    ChrTalk(    #140
        0x107,
        "#065F#5P咦……！？\x02",
    )

    CloseMessageWindow()

    label("loc_4404")


    ChrTalk(    #141
        0x104,
        (
            "#1545F#5P这还真是让人吃惊……\x02\x03",

            "#1540F是因为有这个规则吗……\x01",
            "在这个世界中可以将意念变为现实。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4746")

    label("loc_4477")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_456D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44B1")

    ChrTalk(    #142
        0x110,
        "#1306F#5P哎呀……\x02",
    )

    CloseMessageWindow()

    label("loc_44B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44DB")

    ChrTalk(    #143
        0x102,
        "#1504F#5P啊……\x02",
    )

    CloseMessageWindow()

    label("loc_44DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4508")

    ChrTalk(    #144
        0x107,
        "#065F#5P咦……！？\x02",
    )

    CloseMessageWindow()

    label("loc_4508")


    ChrTalk(    #145
        0x10C,
        (
            "#115F#5P原来如此……\x02\x03",

            "#112F可将意念变为现实的世界……\x01",
            "是按照这个规则运行的吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4746")

    label("loc_456D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_463C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45A5")

    ChrTalk(    #146
        0x102,
        "#1504F#5P啊……\x02",
    )

    CloseMessageWindow()

    label("loc_45A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45D2")

    ChrTalk(    #147
        0x107,
        "#065F#5P咦……！？\x02",
    )

    CloseMessageWindow()

    label("loc_45D2")


    ChrTalk(    #148
        0x110,
        (
            "#263F#5P嘻嘻，原来如此。\x02\x03",

            "#1306F可将意念变为现实的世界……\x01",
            "是按照这个规则运行的呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4746")

    label("loc_463C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46D8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4674")

    ChrTalk(    #149
        0x102,
        "#1504F#5P啊……\x02",
    )

    CloseMessageWindow()

    label("loc_4674")


    ChrTalk(    #150
        0x107,
        (
            "#062F#5P难、难道……\x02\x03",

            "是因为有这个规则吗……\x01",
            "这个世界可以把意念变为现实……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4746")

    label("loc_46D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4746")

    ChrTalk(    #151
        0x102,
        (
            "#1503F#5P对了……\x02\x03",

            "#1502F可将意念变为现实的世界……\x01",
            "是按照这个规则运行的呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4746")


    ChrTalk(    #152
        0x109,
        (
            "#1841F#6P呵呵，\x01",
            "其实我也没什么自信……\x02\x03",

            "#1840F不过之前所有的领域\x01",
            "都选择了一位特定的人物。\x02\x03",

            "从这点来说，莉丝。\x01",
            "你会来到这里\x01",
            "也是理所当然的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x10F,
        (
            "#1445F#5P怎么会……可是……\x02\x03",

            "………………………………\x02\x03",

            "#1443F虽然难以置信，\x01",
            "可这的确是礼拜堂的钥匙……\x02\x03",

            "总之，\x01",
            "我们用这个进礼拜堂吧。\x02",
        )
    )

    Jump("loc_489F")

    label("loc_489F")

    CloseMessageWindow()

    ChrTalk(    #154
        0x109,
        "#1067F#6P……嗯。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2C0A)
    OP_28(0x3C, 0x1, 0x200)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_8_3506 end

    def Function_9_48CF(): pass

    label("Function_9_48CF")

    OP_8F(0xFE, 0xFFFFEC64, 0xFFFFFF1A, 0xFFFFD9C2, 0x7D0, 0x0)
    Return()

    # Function_9_48CF end

    def Function_10_48E4(): pass

    label("Function_10_48E4")

    OP_8F(0xFE, 0xFFFFE5DE, 0xFFFFFF06, 0xFFFFD9A4, 0x7D0, 0x0)
    Return()

    # Function_10_48E4 end

    def Function_11_48F9(): pass

    label("Function_11_48F9")

    OP_8F(0xFE, 0xFFFFD490, 0xFA, 0xFFFFDA12, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFFE214, 0xFFFFFF06, 0xFFFFD6B6, 0x7D0, 0x0)
    Return()

    # Function_11_48F9 end

    def Function_12_4922(): pass

    label("Function_12_4922")

    OP_8F(0xFE, 0xFFFFD490, 0xFA, 0xFFFFDA12, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFFE02A, 0xFFFFFF06, 0xFFFFDC74, 0x7D0, 0x0)
    Return()

    # Function_12_4922 end

    def Function_13_494B(): pass

    label("Function_13_494B")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-800, 250, 7630, 0)
    OP_67(0, 4880, -10000, 0)
    OP_6B(3460, 0)
    OP_6C(315000, 0)
    OP_6E(231, 0)
    OP_6D(-800, 250, 7630, 0)
    OP_67(0, 5600, -10000, 0)
    OP_6B(3270, 0)
    OP_6C(315000, 0)
    OP_6E(231, 0)
    SetChrPos(0x109, 0, -250, 6090, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A21")
    SetChrPos(0xEF, 240, 250, 7560, 0)
    SetChrPos(0xF0, -470, -250, 4550, 0)
    SetChrPos(0xF1, 1040, -250, 4470, 0)
    Jump("loc_4AA6")

    label("loc_4A21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A65")
    SetChrPos(0xF0, 240, 250, 7560, 0)
    SetChrPos(0xEF, -190, -250, 4550, 0)
    SetChrPos(0xF1, 1320, -250, 4470, 0)
    Jump("loc_4AA6")

    label("loc_4A65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AA6")
    SetChrPos(0xF1, 240, 250, 7560, 0)
    SetChrPos(0xEF, -190, -250, 4550, 0)
    SetChrPos(0xF0, 1320, -250, 4470, 0)

    label("loc_4AA6")

    OP_0D()
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #155
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x582, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C38")
    OP_A2(0x2C10)

    ChrTalk(    #156
        0x109,
        (
            "#1065F#6P莉丝，我事先说好。\x02\x03",

            "#1063F一旦打开了这道门……\x01",
            "就再也无法回头了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10F, 180, 400)
    Sleep(300)

    ChrTalk(    #157
        0x10F,
        "#1444F#11P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x109,
        (
            "#1840F#6P你会知道那一天\x01",
            "发生的所有事情的真相。\x02\x03",

            "……你有这样的心理准备吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x10F,
        "#1802F#11P…………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D09")

    label("loc_4C38")


    ChrTalk(    #160
        0x109,
        (
            "#1065F#6P一旦打开了这道门……\x01",
            "就再也无法回头了。\x02\x03",

            "#1840F你会知道那一天\x01",
            "发生的所有事情的真相。\x02\x03",

            "……你有这样的心理准备吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 180, 400)
    Sleep(300)

    ChrTalk(    #161
        0x10F,
        "#1802F#11P…………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_4D09")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_583E")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【使用钥匙】\x01",      # 0
            "【不使用】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4D7A"),
        (SWITCH_DEFAULT, "loc_582E"),
    )


    label("loc_4D7A")

    Sleep(300)

    ChrTalk(    #162
        0x10F,
        (
            "#1443F#11P……求之不得。\x02\x03",

            "#1445F这五年来……\x01",
            "我一直都无法接受。\x02\x03",

            "在那之后，包括我在内的所有人\x01",
            "都被转到了其它设施……\x02\x03",

            "在开始随从骑士的修行以前\x01",
            "我来过这里一次，\x01",
            "但已经全被毁了……\x02\x03",

            "#1446F所以……\x01",
            "我早就有所觉悟了。\x02\x03",

            "#1806F我比任何人……\x01",
            "都更想接近姐姐和凯文。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x109,
        (
            "#1067F#6P是吗……\x02\x03",

            "#1840F我明白了。\x01",
            "那就赶快进去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x10F,
        "#1448F#11P嗯……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10F, 0, 400)
    Sleep(500)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 0)
    OP_70(0x0, 0xF)
    OP_73(0x0)
    Sleep(500)

    ChrTalk(    #165
        0x10F,
        "#1445F#5P……………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FDA")
    OP_A2(0x0)

    ChrTalk(    #166
        0x101,
        (
            "#1007F#6P那、那个……\x02\x03",

            "#1025F我们是不是\x01",
            "在外面等比较好呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_545E")

    label("loc_4FDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_503C")
    OP_A2(0x2)

    ChrTalk(    #167
        0x102,
        (
            "#1505F#6P……凯文先生。\x02\x03",

            "#1502F我们是不是\x01",
            "在外面等比较好？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_545E")

    label("loc_503C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50B6")

    ChrTalk(    #168
        0x104,
        (
            "#1545F#6P唔，凯文君。\x02\x03",

            "#1540F虽然我有浓厚的兴趣，\x01",
            "不过我们是不是\x01",
            "留在外面等比较好呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_545E")

    label("loc_50B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5117")
    OP_A2(0x5)

    ChrTalk(    #169
        0x110,
        (
            "#267F#6P喂，教会的哥哥。\x02\x03",

            "我们是不是\x01",
            "待在外面等比较好呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_545E")

    label("loc_5117")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_517B")
    OP_A2(0x1)

    ChrTalk(    #170
        0x107,
        (
            "#065F#6P那、那个……\x02\x03",

            "#067F我们……\x01",
            "是不是在外面等比较好呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_545E")

    label("loc_517B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51D8")

    ChrTalk(    #171
        0x10E,
        (
            "#176F#6P……凯文先生。\x02\x03",

            "#178F我们是不是\x01",
            "在外面等比较好？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_545E")

    label("loc_51D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_523B")

    ChrTalk(    #172
        0x105,
        (
            "#1169F#6P那个……凯文先生。\x02\x03",

            "#1382F我们是不是\x01",
            "在外面等比较好？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_545E")

    label("loc_523B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5296")

    ChrTalk(    #173
        0x103,
        (
            "#1526F#6P喂……\x02\x03",

            "#1534F我们是不是\x01",
            "待在外面等比较好呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_545E")

    label("loc_5296")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52EB")

    ChrTalk(    #174
        0x106,
        (
            "#053F#6P喂……\x02\x03",

            "#050F我们是不是\x01",
            "在外面等比较好？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_545E")

    label("loc_52EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_534B")
    OP_A2(0x4)

    ChrTalk(    #175
        0x10B,
        (
            "#215F#6P哎，那个……\x02\x03",

            "#212F我们是不是\x01",
            "在外面等比较好呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_545E")

    label("loc_534B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53AD")
    OP_A2(0x3)

    ChrTalk(    #176
        0x10A,
        (
            "#813F#6P呃，这个……\x02\x03",

            "#810F我们是不是\x01",
            "在外面等比较好……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_545E")

    label("loc_53AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5402")

    ChrTalk(    #177
        0x108,
        (
            "#074F#6P唔……\x02\x03",

            "#070F我们是不是\x01",
            "在外面等比较好？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_545E")

    label("loc_5402")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_545E")

    ChrTalk(    #178
        0x10C,
        (
            "#115F#6P……凯文神父。\x02\x03",

            "#110F我们是不是\x01",
            "在外面等比较好呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_545E")


    def lambda_5464():
        OP_6D(-800, 250, 7000, 800)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_5464)
    OP_8C(0x109, 180, 400)
    WaitChrThread(0x109, 0x0)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5519")

    ChrTalk(    #179
        0x109,
        (
            "#1075F#11P没什么……\x01",
            "你们愿意的话可以一起来。\x02\x03",

            "#1840F因为从某种意义上说，\x01",
            "这也是和你们有关的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_558D")

    label("loc_5519")


    ChrTalk(    #180
        0x109,
        (
            "#1075F#11P没什么……\x01",
            "你们愿意的话可以一起来。\x02\x03",

            "#1840F因为从某种意义上说，\x01",
            "这也是和你们有关的事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_558D")

    Sleep(300)
    Fade(500)
    OP_6D(0, 2500, 7460, 0)
    OP_67(0, 3900, -10000, 0)
    OP_6B(3360, 0)
    OP_6C(0, 0)
    OP_6E(291, 0)
    SetChrPos(0x109, 40, -250, 5730, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5629")
    SetChrPos(0xEF, 0, 250, 7770, 0)
    SetChrPos(0xF0, -570, -250, 4050, 0)
    SetChrPos(0xF1, 770, -250, 4000, 0)
    Jump("loc_56AE")

    label("loc_5629")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_566D")
    SetChrPos(0xF0, 0, 250, 7770, 0)
    SetChrPos(0xEF, -570, -250, 4050, 0)
    SetChrPos(0xF1, 770, -250, 4000, 0)
    Jump("loc_56AE")

    label("loc_566D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56AE")
    SetChrPos(0xF1, 0, 250, 7770, 0)
    SetChrPos(0xEF, -570, -250, 4050, 0)
    SetChrPos(0xF0, 770, -250, 4000, 0)

    label("loc_56AE")

    OP_0D()
    OP_8C(0x109, 0, 400)

    def lambda_56BC():
        OP_6D(0, 2250, 7460, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_56BC)

    def lambda_56D4():
        OP_67(0, 3420, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_56D4)

    def lambda_56EC():
        OP_6B(2730, 6000)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_56EC)

    def lambda_56FC():
        OP_6E(302, 6000)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_56FC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5742")
    OP_43(0xEF, 0x0, 0x0, 0xF)
    Sleep(200)
    OP_43(0x109, 0x0, 0x0, 0x10)
    Sleep(300)
    OP_43(0xF0, 0x0, 0x0, 0x11)
    Sleep(600)
    OP_43(0xF1, 0x0, 0x0, 0x12)
    Jump("loc_57B7")

    label("loc_5742")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_577E")
    OP_43(0xF0, 0x0, 0x0, 0xF)
    Sleep(100)
    OP_43(0x109, 0x0, 0x0, 0x10)
    Sleep(300)
    OP_43(0xEF, 0x0, 0x0, 0x11)
    Sleep(600)
    OP_43(0xF1, 0x0, 0x0, 0x12)
    Jump("loc_57B7")

    label("loc_577E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57B7")
    OP_43(0xF1, 0x0, 0x0, 0xF)
    Sleep(100)
    OP_43(0x109, 0x0, 0x0, 0x10)
    Sleep(300)
    OP_43(0xEF, 0x0, 0x0, 0x11)
    Sleep(600)
    OP_43(0xF0, 0x0, 0x0, 0x12)

    label("loc_57B7")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_22(0x178, 0x0, 0x64)
    OP_23(0x177)
    OP_B0(0x0, 0x8)
    OP_6F(0x0, 15)
    OP_70(0x0, 0x0)
    OP_23(0x177)
    OP_73(0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    OP_44(0xEE, 0x3)
    OP_44(0xEF, 0x3)
    OP_44(0xF0, 0x3)
    OP_44(0xF1, 0x3)
    Call(0, 14)
    OP_A2(0x2504)
    NewScene("ED6_DT21/P7010   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_583B")

    label("loc_582E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_583B")

    label("loc_583B")

    Jump("loc_4D26")

    label("loc_583E")

    EventEnd(0x0)
    Return()

    # Function_13_494B end

    def Function_14_5841(): pass

    label("Function_14_5841")

    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5864")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5999")

    label("loc_5864")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_587E")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5999")

    label("loc_587E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5898")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5999")

    label("loc_5898")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58B2")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5999")

    label("loc_58B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58CC")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5999")

    label("loc_58CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58E6")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5999")

    label("loc_58E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5900")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5999")

    label("loc_5900")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_591A")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5999")

    label("loc_591A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5934")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5999")

    label("loc_5934")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_594E")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5999")

    label("loc_594E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5968")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5999")

    label("loc_5968")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5982")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5999")

    label("loc_5982")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5999")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5999")

    Return()

    # Function_14_5841 end

    def Function_15_599A(): pass

    label("Function_15_599A")

    OP_8F(0xFE, 0x0, 0xFA, 0x24AE, 0x7D0, 0x0)

    def lambda_59B4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_59B4)
    SetChrFlags(0xFE, 0x4)
    OP_8F(0xFE, 0x0, 0xFA, 0x2A8A, 0x7D0, 0x0)
    Return()

    # Function_15_599A end

    def Function_16_59DA(): pass

    label("Function_16_59DA")

    OP_8F(0xFE, 0x0, 0xFA, 0x24AE, 0x7D0, 0x0)

    def lambda_59F4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_59F4)
    SetChrFlags(0xFE, 0x4)
    OP_8F(0xFE, 0x0, 0xFA, 0x2A8A, 0x7D0, 0x0)
    Return()

    # Function_16_59DA end

    def Function_17_5A1A(): pass

    label("Function_17_5A1A")

    OP_8F(0xFE, 0x0, 0xFA, 0x24AE, 0x7D0, 0x0)

    def lambda_5A34():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5A34)
    SetChrFlags(0xFE, 0x4)
    OP_8F(0xFE, 0x0, 0xFA, 0x2A8A, 0x7D0, 0x0)
    Return()

    # Function_17_5A1A end

    def Function_18_5A5A(): pass

    label("Function_18_5A5A")

    OP_8F(0xFE, 0x0, 0xFA, 0x24AE, 0x7D0, 0x0)

    def lambda_5A74():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5A74)
    SetChrFlags(0xFE, 0x4)
    OP_8F(0xFE, 0x0, 0xFA, 0x2A8A, 0x7D0, 0x0)
    Return()

    # Function_18_5A5A end

    def Function_19_5A9A(): pass

    label("Function_19_5A9A")

    EventBegin(0x1)
    SetMapFlags(0x80)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(1000, 16777215, -1)

    def lambda_5ABA():
        OP_90(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_5ABA)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_0D()
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    NewScene("ED6_DT21/M4111   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_19_5A9A end

    SaveToFile()

Try(main)
