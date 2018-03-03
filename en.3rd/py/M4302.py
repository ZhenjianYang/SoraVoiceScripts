from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M4302   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M4302.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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


    DeclEvent(
        X                   = 0,
        Y                   = -5000,
        Z                   = -62000,
        Range               = 3000,
        Unknown_10          = 0x5DC,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = 6830,
        TriggerZ            = 0,
        TriggerY            = 38980,
        TriggerRange        = 1000,
        ActorX              = 6830,
        ActorZ              = 2000,
        ActorY              = 38980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_EE",           # 00, 0
        "Function_1_11B",          # 01, 1
        "Function_2_133",          # 02, 2
        "Function_3_584",          # 03, 3
        "Function_4_806",          # 04, 4
        "Function_5_895",          # 05, 5
    )


    def Function_0_EE(): pass

    label("Function_0_EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_109")
    OP_A3(0x2504)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_105")
    SetMapFlags(0x10000000)

    label("loc_105")

    Event(0, 5)

    label("loc_109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11A")
    SetMapFlags(0x10000000)

    label("loc_11A")

    Return()

    # Function_0_EE end

    def Function_1_11B(): pass

    label("Function_1_11B")

    OP_10(0x0, 0x0)
    OP_10(0x2, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_132")

    Return()

    # Function_1_11B end

    def Function_2_133(): pass

    label("Function_2_133")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6F(0x0, 1100)
    OP_70(0x0, 0x44C)
    OP_48()
    OP_89(0x0, 800, 40000, -61200, 0)
    OP_89(0x1, -800, 40000, -61200, 0)
    OP_89(0x2, -800, 40000, -62800, 0)
    OP_89(0x3, 800, 40000, -62800, 0)
    OP_6D(630, 12220, -60170, 0)
    OP_67(0, 13130, -10000, 0)
    OP_6B(3540, 0)
    OP_6C(21000, 0)
    OP_6E(322, 0)
    Sleep(1000)

    def lambda_1DA():
        OP_6D(550, -3980, -61520, 7500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1DA)

    def lambda_1F2():
        OP_67(0, 9260, -10000, 7500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1F2)

    def lambda_20A():
        OP_6B(2930, 7500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_20A)

    def lambda_21A():
        OP_6C(45000, 7500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_21A)

    def lambda_22A():
        OP_6E(290, 7500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_22A)
    OP_6F(0x0, 1150)
    OP_70(0x0, 0x640)
    FadeToBright(2000, 0)
    Sleep(1000)
    SetPlaceName(0xE3)
    ClearMapFlags(0x10000000)
    SetPlaceName(0xE3)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_73(0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x10E,
        (
            "#178F#6PThis just isn't possible...\x02\x03",

            "How are we on the lowest floor of the ruin\x01",
            "already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10F,
        "#1802F#6PCould the space we're in be distorted?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1065F#5PNah. That alone wouldn't explain how the\x01",
            "entire layout of the place has changed.\x02\x03",

            "#1063FLet's just keep up the pace.\x02\x03",

            "I've got a feeling there's gonna be something--\x01",
            "or someone--waiting for us not far ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10F,
        "#1443F#6P...All right.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43D")

    ChrTalk(    #4
        0x102,
        "#1502F#6PLet's just be sure we're ready.\x02",
    )

    CloseMessageWindow()
    Jump("loc_524")

    label("loc_43D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_489")

    ChrTalk(    #5
        0x107,
        (
            "#062F#6PLet's just make sure we're ready first,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_524")

    label("loc_489")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E2")

    ChrTalk(    #6
        0x10B,
        (
            "#212F#6PWell, if you say so...but we'd better be sure\x01",
            "we're ready.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_524")

    label("loc_4E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_524")

    ChrTalk(    #7
        0x10D,
        "#272F#6PHmm... I just hope we're ready for it.\x02",
    )

    CloseMessageWindow()

    label("loc_524")

    Sleep(300)
    OP_A2(0x271F)
    OP_28(0x2E, 0x1, 0x8)
    OP_28(0x2E, 0x1, 0x10)
    Fade(1000)
    SetChrPos(0x0, 0, -4000, -58600, 0)
    SetChrPos(0x1, 0, -4000, -58600, 0)
    SetChrPos(0x2, 0, -4000, -58600, 0)
    SetChrPos(0x3, 0, -4000, -58600, 0)
    EventEnd(0x0)
    Return()

    # Function_2_133 end

    def Function_3_584(): pass

    label("Function_3_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_653")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(1536)
    Sleep(500)
    Jump("loc_656")

    label("loc_653")

    TalkBegin(0xFF)

    label("loc_656")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #8
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_692")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7D5")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Restore HP/EP\x01",          # 0
            "Shop\x01",                   # 1
            "Synthesize Quartz\x01",      # 2
            "End\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6EE"),
        (1, "loc_769"),
        (2, "loc_797"),
        (SWITCH_DEFAULT, "loc_7C5"),
    )


    label("loc_6EE")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xDD)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7D2")

    label("loc_769")

    OP_A9(0x18)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #9
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_7D2")

    label("loc_797")

    OP_A9(0x3)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #10
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_7D2")

    label("loc_7C5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7D2")

    label("loc_7D2")

    Jump("loc_692")

    label("loc_7D5")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_802")
    OP_A2(0x2589)
    EventEnd(0x1)
    Jump("loc_805")

    label("loc_802")

    TalkEnd(0xFF)

    label("loc_805")

    Return()

    # Function_3_584 end

    def Function_4_806(): pass

    label("Function_4_806")

    EventBegin(0x0)
    Fade(1000)
    OP_89(0x0, -800, 20000, -62800, 180)
    OP_89(0x1, 800, 20000, -62800, 180)
    OP_89(0x2, 800, 20000, -61200, 180)
    OP_89(0x3, -800, 20000, -61200, 180)
    OP_6D(0, -4000, -62000, 1500)
    Sleep(100)
    OP_B0(0x0, 0x5A)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x0, 1600)
    OP_70(0x0, 0x3E8)
    Sleep(2000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M4308   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_806 end

    def Function_5_895(): pass

    label("Function_5_895")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A6")
    Call(0, 2)
    Return()

    label("loc_8A6")

    EventBegin(0x0)
    SetPlaceName(0xE3)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x0, 1300)
    OP_70(0x0, 0x640)
    OP_48()
    OP_89(0x0, 800, 20000, -61200, 0)
    OP_89(0x1, -800, 20000, -61200, 0)
    OP_89(0x2, -800, 20000, -62800, 0)
    OP_89(0x3, 800, 20000, -62800, 0)
    OP_6D(0, -4000, -62000, 0)
    OP_73(0x0)
    Sleep(100)
    Fade(1000)
    SetChrPos(0x0, 0, -4000, -58600, 0)
    SetChrPos(0x1, 0, -4000, -58600, 0)
    SetChrPos(0x2, 0, -4000, -58600, 0)
    SetChrPos(0x3, 0, -4000, -58600, 0)
    EventEnd(0x0)
    Return()

    # Function_5_895 end

    SaveToFile()

Try(main)
