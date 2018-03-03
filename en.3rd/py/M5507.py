from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M5507   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5507.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60231",
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
        TriggerX            = 5300,
        TriggerZ            = 0,
        TriggerY            = 9990,
        TriggerRange        = 800,
        ActorX              = 5670,
        ActorZ              = 1500,
        ActorY              = 10510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_CE",           # 00, 0
        "Function_1_DF",           # 01, 1
        "Function_2_F7",           # 02, 2
        "Function_3_B03",          # 03, 3
        "Function_4_1073",         # 04, 4
    )


    def Function_0_CE(): pass

    label("Function_0_CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE")
    Event(0, 2)

    label("loc_DE")

    Return()

    # Function_0_CE end

    def Function_1_DF(): pass

    label("Function_1_DF")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE2758, 0x2300A4)
    OP_1B(0x1, 0x0, 0x3)
    Return()

    # Function_1_DF end

    def Function_2_F7(): pass

    label("Function_2_F7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 950, 0, 25250, 180)
    SetChrPos(0x102, 2360, 0, 25120, 180)
    SetChrPos(0xF0, 1230, 0, 26610, 180)
    SetChrPos(0xF1, 2670, 0, 26530, 180)
    OP_6D(2700, 3000, -24000, 0)
    OP_67(0, 14750, -10000, 0)
    OP_6B(2930, 0)
    OP_6C(89000, 0)
    OP_6E(428, 0)

    def lambda_18A():
        OP_6D(2700, 3000, 13000, 12000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_18A)

    def lambda_1A2():
        OP_67(0, 12710, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1A2)

    def lambda_1BA():
        OP_6B(2930, 9000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1BA)

    def lambda_1CA():
        OP_6E(428, 9000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1CA)
    StopSound(0x88B8, 0x27100, 0x0)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_1F1():
        OP_8E(0xFE, 0xFFFFFA1A, 0x0, 0x339A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1F1)
    Sleep(200)

    def lambda_211():
        OP_8E(0xFE, 0xFFFFFFF6, 0x0, 0x32E6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_211)
    Sleep(130)

    def lambda_231():
        OP_8E(0xFE, 0xFFFFFA6A, 0x0, 0x3994, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_231)
    Sleep(150)

    def lambda_251():
        OP_8E(0xFE, 0x122, 0x0, 0x389A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_251)
    Sleep(1000)
    Fade(1000)
    StopSound(0x88B8, 0x30D40, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    OP_44(0x102, 0x2)
    OP_6D(1500, 0, -2430, 0)
    OP_67(0, 12990, -10000, 0)
    OP_6B(3480, 0)
    OP_6C(45000, 0)
    OP_6E(427, 0)

    def lambda_2D0():
        OP_6D(-350, 2000, 10660, 5500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2D0)

    def lambda_2E8():
        OP_6B(3800, 5500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2E8)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x102, 0x1)
    Sleep(1000)
    Fade(1000)
    StopSound(0x88B8, 0x1FBD0, 0x0)
    OP_6D(520, 0, 15250, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(2540, 0)
    OP_6C(45000, 0)
    OP_6E(337, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_417")

    ChrTalk(    #0
        0x10A,
        (
            "#1310F#5POh, wow! Look at how pretty the trees are!\x02\x03",

            "#819FThey were still green when Estelle and I were\x01",
            "here. It's like a whole different forest now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_595")

    label("loc_417")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_457")

    ChrTalk(    #1
        0x107,
        "#560F#5PLook at all this! It's so pretty!\x02",
    )

    CloseMessageWindow()
    Jump("loc_595")

    label("loc_457")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49A")

    ChrTalk(    #2
        0x105,
        "#1168F#5PWow... This forest is so beautiful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_595")

    label("loc_49A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4DC")

    ChrTalk(    #3
        0x10B,
        "#415F#5PWow... This forest is so beautiful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_595")

    label("loc_4DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51C")

    ChrTalk(    #4
        0x104,
        "#1540F#5POh, my... This is just stunning.\x02",
    )

    CloseMessageWindow()
    Jump("loc_595")

    label("loc_51C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54E")

    ChrTalk(    #5
        0x10E,
        "#171F#5PMy... How stunning.\x02",
    )

    CloseMessageWindow()
    Jump("loc_595")

    label("loc_54E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_595")

    ChrTalk(    #6
        0x108,
        "#070F#5PWow... Now, this is a real sight to behold.\x02",
    )

    CloseMessageWindow()

    label("loc_595")


    ChrTalk(    #7
        0x102,
        (
            "#1504F#5P...\x02\x03",

            "#1502FIt certainly is pretty...but don't you think it's odd?\x02\x03",

            "The leaves of coniferous trees don't usually turn\x01",
            "orange like this, do they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x109,
        (
            "#1065F#6PMost don't, but there are some varieties that lose\x01",
            "their leaves in the fall, for sure.\x02\x03",

            "#1067FCan't remember their names, though. Ries would\x01",
            "know better than me, but, well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#1500F#5PI see. Don't mind me, then.\x02\x03",

            "#1503FActually, wait. The trees near the lodge are\x01",
            "the same variety as these, aren't they?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BB")
    OP_A2(0x2)

    ChrTalk(    #10
        0x10D,
        "#270F#5PHmm... Those were still green, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9C0")

    label("loc_7BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_800")
    OP_A2(0x7)

    ChrTalk(    #11
        0x108,
        "#072F#5PHmm... Those were still green, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9C0")

    label("loc_800")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_845")
    OP_A2(0x1)

    ChrTalk(    #12
        0x10E,
        "#178F#5PHmm... Those were still green, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9C0")

    label("loc_845")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88B")
    OP_A2(0x6)

    ChrTalk(    #13
        0x104,
        "#1542F#5PHmm... Those were still green, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9C0")

    label("loc_88B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F5")
    OP_A2(0x3)

    ChrTalk(    #14
        0x10B,
        (
            "#212F#5PThose weren't showing any signs of losing their\x01",
            "leaves at all, either...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C0")

    label("loc_8F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_960")
    OP_A2(0x5)

    ChrTalk(    #15
        0x105,
        (
            "#1162F#5PThose weren't showing any signs of losing their\x01",
            "leaves at all, either...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C0")

    label("loc_960")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9C0")
    OP_A2(0x0)

    ChrTalk(    #16
        0x107,
        (
            "#062F#5PThose weren't showing any signs of losing their\x01",
            "leaves, either...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A63")

    ChrTalk(    #17
        0x109,
        (
            "#1065F#6PYeah... So your first guess might've been wrong,\x01",
            "but there's definitely SOMETHING off here.\x02\x03",

            "#1063FWe'd better be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AEC")

    label("loc_A63")


    ChrTalk(    #18
        0x109,
        (
            "#1065F#6PYeah... So your first guess might've been wrong,\x01",
            "but there's definitely SOMETHING off here.\x02\x03",

            "#1063FWe'd better be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AEC")

    OP_A2(0x2906)
    OP_28(0x33, 0x1, 0x1)
    OP_28(0x33, 0x1, 0x2)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_F7 end

    def Function_3_B03(): pass

    label("Function_3_B03")

    ClearMapFlags(0x2000000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_B26")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B37")

    label("loc_B26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_B37")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B37")

    SetMapFlags(0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_B5C"),
        (1, "loc_B8B"),
        (2, "loc_BBA"),
        (SWITCH_DEFAULT, "loc_BE9"),
    )


    label("loc_B5C")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP001._CH")
    Jump("loc_BE9")

    label("loc_B8B")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP002._CH")
    Jump("loc_BE9")

    label("loc_BBA")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP003._CH")
    Jump("loc_BE9")

    label("loc_BE9")

    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C1E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F23")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_C49"),
        (1, "loc_C75"),
        (2, "loc_CB6"),
        (SWITCH_DEFAULT, "loc_D0A"),
    )


    label("loc_C49")


    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",          # 0
            "[Balstar Channel]\x01",      # 1
        )
    )

    Jump("loc_D0A")

    label("loc_C75")


    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",             # 0
            "[Balstar Channel]\x01",         # 1
            "[Saint-Croix Forest]\x01",      # 2
        )
    )

    Jump("loc_D0A")

    label("loc_CB6")


    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",             # 0
            "[Balstar Channel]\x01",         # 1
            "[Saint-Croix Forest]\x01",      # 2
            "[Grimsel Fortress]\x01",        # 3
        )
    )

    Jump("loc_D0A")

    label("loc_D0A")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D34"),
        (1, "loc_DAB"),
        (2, "loc_E26"),
        (3, "loc_EA4"),
        (SWITCH_DEFAULT, "loc_F20"),
    )


    label("loc_D34")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #19
        "\x07\x05Travel to [Guild Lodge]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D98"),
        (1, "loc_DA5"),
        (SWITCH_DEFAULT, "loc_DA8"),
    )


    label("loc_D98")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DA8")

    label("loc_DA5")

    Jump("loc_DA8")

    label("loc_DA8")

    Jump("loc_F20")

    label("loc_DAB")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #20
        "\x07\x05Travel to [Balstar Channel]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E13"),
        (1, "loc_E20"),
        (SWITCH_DEFAULT, "loc_E23"),
    )


    label("loc_E13")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E23")

    label("loc_E20")

    Jump("loc_E23")

    label("loc_E23")

    Jump("loc_F20")

    label("loc_E26")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #21
        "\x07\x05Travel to [Saint-Croix Forest]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E91"),
        (1, "loc_E9E"),
        (SWITCH_DEFAULT, "loc_EA1"),
    )


    label("loc_E91")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EA1")

    label("loc_E9E")

    Jump("loc_EA1")

    label("loc_EA1")

    Jump("loc_F20")

    label("loc_EA4")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #22
        "\x07\x05Travel to [Grimsel Fortress]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F0D"),
        (1, "loc_F1A"),
        (SWITCH_DEFAULT, "loc_F1D"),
    )


    label("loc_F0D")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F1D")

    label("loc_F1A")

    Jump("loc_F1D")

    label("loc_F1D")

    Jump("loc_F20")

    label("loc_F20")

    Jump("loc_C1E")

    label("loc_F23")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_F3C"),
        (1, "loc_F70"),
        (2, "loc_FA4"),
        (3, "loc_FD8"),
        (SWITCH_DEFAULT, "loc_100C"),
    )


    label("loc_F3C")

    OP_C6(0x0, 0x0, -640000, 0, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_100C")

    label("loc_F70")

    OP_C6(0x0, 0x0, -358000, -37000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_100C")

    label("loc_FA4")

    OP_C6(0x0, 0x0, -362000, -266000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_100C")

    label("loc_FD8")

    OP_C6(0x0, 0x0, -64000, -340000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_100C")

    label("loc_100C")

    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_102E"),
        (1, "loc_104E"),
        (2, "loc_105A"),
        (3, "loc_1066"),
        (SWITCH_DEFAULT, "loc_1072"),
    )


    label("loc_102E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1042")
    NewScene("ED6_DT21/U5100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_104B")

    label("loc_1042")

    NewScene("ED6_DT21/U5102   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_104B")

    Jump("loc_1072")

    label("loc_104E")

    NewScene("ED6_DT21/M5503   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1072")

    label("loc_105A")

    NewScene("ED6_DT21/M5507   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_1072")

    label("loc_1066")

    NewScene("ED6_DT21/M5508   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_1072")

    label("loc_1072")

    Return()

    # Function_3_B03 end

    def Function_4_1073(): pass

    label("Function_4_1073")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #23
        "\x07\x05Saint-Croix Forest\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #24
        (
            "\x07\x05Recommended for ranger training and other\x01",
            "survival lessons.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_4_1073 end

    SaveToFile()

Try(main)
