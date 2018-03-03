from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4165   ._SN',
        MapName             = 'gaiden2',
        Location            = 'U4165.x',
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


    DeclActor(
        TriggerX            = -84930,
        TriggerZ            = 0,
        TriggerY            = -60800,
        TriggerRange        = 1000,
        ActorX              = -84930,
        ActorZ              = 2000,
        ActorY              = -60800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 78570,
        TriggerZ            = 0,
        TriggerY            = -63260,
        TriggerRange        = 1000,
        ActorX              = 77000,
        ActorZ              = 3000,
        ActorY              = -63000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -11940,
        TriggerZ            = 0,
        TriggerY            = 6010,
        TriggerRange        = 1000,
        ActorX              = -11940,
        ActorZ              = 1000,
        ActorY              = 6010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 87000,
        TriggerZ            = 0,
        TriggerY            = 42860,
        TriggerRange        = 800,
        ActorX              = 87000,
        ActorZ              = 1000,
        ActorY              = 42860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -87000,
        TriggerZ            = 0,
        TriggerY            = 42860,
        TriggerRange        = 800,
        ActorX              = -87000,
        ActorZ              = 1000,
        ActorY              = 42860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_15E",          # 00, 0
        "Function_1_1A2",          # 01, 1
        "Function_2_1D5",          # 02, 2
        "Function_3_A22",          # 03, 3
        "Function_4_A49",          # 04, 4
        "Function_5_A70",          # 05, 5
        "Function_6_A97",          # 06, 6
        "Function_7_ABE",          # 07, 7
        "Function_8_B2B",          # 08, 8
        "Function_9_DAD",          # 09, 9
        "Function_10_E06",         # 0A, 10
        "Function_11_E84",         # 0B, 11
        "Function_12_12BB",        # 0C, 12
        "Function_13_1371",        # 0D, 13
        "Function_14_141C",        # 0E, 14
    )


    def Function_0_15E(): pass

    label("Function_0_15E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_174")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 13)
    Jump("loc_1A1")

    label("loc_174")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A1")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_1A1")

    Return()

    # Function_0_15E end

    def Function_1_1A2(): pass

    label("Function_1_1A2")

    OP_72(0x1001, 0x0)
    ExitThread()
    OP_1B(0x3, 0x0, 0x7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_1BE")

    OP_82(0x84, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1D1")
    OP_82(0x85, 0x0)
    Jump("loc_1D4")

    label("loc_1D1")

    OP_82(0x86, 0x0)

    label("loc_1D4")

    Return()

    # Function_1_1A2 end

    def Function_2_1D5(): pass

    label("Function_2_1D5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -410, 0, -2500, 0)
    SetChrPos(0x10F, 1030, 0, -2420, 0)
    SetChrPos(0xF0, -410, 0, -2500, 0)
    SetChrPos(0xF1, 1030, 0, -2420, 0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-1070, 0, 16059, 0)
    OP_67(0, 7910, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(315000, 0)
    OP_6E(322, 0)

    def lambda_294():
        OP_6D(-730, 0, 4500, 5500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_294)

    def lambda_2AC():
        OP_67(0, 6550, -10000, 5500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2AC)

    def lambda_2C4():
        OP_6B(2850, 5500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_2C4)

    def lambda_2D4():
        OP_6E(284, 5500)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_2D4)
    FadeToBright(1000, 0)
    Sleep(3000)
    OP_43(0x109, 0x0, 0x0, 0x3)
    Sleep(500)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    Sleep(400)
    OP_43(0xF0, 0x0, 0x0, 0x5)
    Sleep(600)
    OP_43(0xF1, 0x0, 0x0, 0x6)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x10F,
        "#1444F#6PWhere are we now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x109,
        (
            "#1060F#5PA hundred percent positive this is the Grand\x01",
            "Arena.\x02\x03",

            "It's used for all kinds of events in Liberl like\x01",
            "martial arts tournaments and stuff.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A5")

    ChrTalk(    #2
        0x10E,
        (
            "#170F#6PIndeed... Zin, Estelle, Olivier, and Joshua\x01",
            "won last year's.\x02\x03",

            "There's yet to be one held this year, though,\x01",
            "for a number of reasons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x109,
        "#1078F#5POh, really?\x02",
    )

    CloseMessageWindow()
    Jump("loc_695")

    label("loc_4A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BC")

    ChrTalk(    #4
        0x10D,
        (
            "#272F#6PI still despair of the fact that Olivier actually\x01",
            "entered.\x02\x03",

            "#276FIf I'd known he was going to, I could have stopped\x01",
            "him, but by the time I heard what was going on,\x01",
            "they had already won.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x109,
        "#1066F#5PHaha... Aren't you used to his surprises by now?\x02",
    )

    CloseMessageWindow()
    Jump("loc_695")

    label("loc_5BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_695")

    ChrTalk(    #6
        0x107,
        (
            "#560F#6PEstelle's team actually ended up winning the\x01",
            "big one held last year.\x02\x03",

            "Agate was pretty disappointed when he found\x01",
            "out about it. He wanted to enter, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x109,
        "#1066F#5PHaha. I'll bet he did.\x02",
    )

    CloseMessageWindow()

    label("loc_695")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_974")
    OP_62(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x109, 0x10B, 400)
    Sleep(300)

    ChrTalk(    #8
        0x109,
        (
            "#1060F#5POh, yeah. You and your brothers took part in\x01",
            "that tournament, too, right, Josie?\x02\x03",

            "Estelle and Joshua mentioned it a while back.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_75A():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_75A)

    def lambda_768():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_768)

    def lambda_776():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_776)
    TurnDirection(0x10B, 0x109, 400)
    Sleep(300)

    ChrTalk(    #9
        0x10B,
        (
            "#416F#6P...Yeah, we did.\x02\x03",

            "Can't say it was much fun. We were basically\x01",
            "just dragged into the arena as criminals.\x02\x03",

            "#216F...Wait, where did that Josie thing come from?\x02\x03",

            "Why am I the only one who gets a weird nickname?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x109,
        (
            "#1064F#5PHuh? Not a fan?\x02\x03",

            "#1068FIt just popped into my mind and I thought it\x01",
            "sounded cute.\x02\x03",

            "#1066FIt fits you perfectly, too, but if it bothers you\x01",
            "that much, I guess I could go with something\x01",
            "else... Jo?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10B,
        "#214F#6PJust call me Josette like everyone else does!\x02",
    )

    CloseMessageWindow()

    label("loc_974")


    ChrTalk(    #12
        0x10F,
        (
            "#1440F#5P...\x02\x03",

            "#1446F...Regardless, it feels as though something\x01",
            "is lying in wait for us in here.\x02\x03",

            "We should proceed with caution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x109,
        "#1060F#5PAgreed.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2712)
    OP_28(0x2C, 0x1, 0x200)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_1D5 end

    def Function_3_A22(): pass

    label("Function_3_A22")


    def lambda_A28():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A28)
    OP_8E(0xFE, 0xFFFFFD6C, 0x0, 0x105E, 0x7D0, 0x0)
    Return()

    # Function_3_A22 end

    def Function_4_A49(): pass

    label("Function_4_A49")


    def lambda_A4F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A4F)
    OP_8E(0xFE, 0x348, 0x0, 0xF64, 0x7D0, 0x0)
    Return()

    # Function_4_A49 end

    def Function_5_A70(): pass

    label("Function_5_A70")


    def lambda_A76():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A76)
    OP_8E(0xFE, 0xFFFFFD08, 0x0, 0xA50, 0x7D0, 0x0)
    Return()

    # Function_5_A70 end

    def Function_6_A97(): pass

    label("Function_6_A97")


    def lambda_A9D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A9D)
    OP_8E(0xFE, 0x406, 0x0, 0x8A2, 0x7D0, 0x0)
    Return()

    # Function_6_A97 end

    def Function_7_ABE(): pass

    label("Function_7_ABE")

    EventBegin(0x1)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05The doors are locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_7_ABE end

    def Function_8_B2B(): pass

    label("Function_8_B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFA")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(1024)
    Sleep(500)
    Jump("loc_BFD")

    label("loc_BFA")

    TalkBegin(0xFF)

    label("loc_BFD")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #15
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C39")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D7C")

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
        (0, "loc_C95"),
        (1, "loc_D10"),
        (2, "loc_D3E"),
        (SWITCH_DEFAULT, "loc_D6C"),
    )


    label("loc_C95")

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
    Jump("loc_D79")

    label("loc_D10")

    OP_A9(0x17)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #16
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_D79")

    label("loc_D3E")

    OP_A9(0x2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #17
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_D79")

    label("loc_D6C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D79")

    label("loc_D79")

    Jump("loc_C39")

    label("loc_D7C")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA9")
    OP_A2(0x2587)
    EventEnd(0x1)
    Jump("loc_DAC")

    label("loc_DA9")

    TalkEnd(0xFF)

    label("loc_DAC")

    Return()

    # Function_8_B2B end

    def Function_9_DAD(): pass

    label("Function_9_DAD")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05Open the Door?\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_9_DAD end

    def Function_10_E06(): pass

    label("Function_10_E06")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "\x1F\x3D\x03\x07\x00 shall be offered,\x01",
            "and the door shall be opened.\x18\x02",
        )
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_10_E06 end

    def Function_11_E84(): pass

    label("Function_11_E84")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, 79700, 0, -62570, 270)
    SetChrPos(0x1, 79520, 0, -63940, 270)
    SetChrPos(0x2, 81380, 0, -62830, 270)
    SetChrPos(0x3, 81460, 0, -64090, 270)
    OP_6D(78510, 0, -63230, 0)
    OP_67(0, 6170, -10000, 0)
    OP_6B(3190, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5A")
    OP_28(0x21, 0x4, 0x2)
    OP_82(0x85, 0x2)
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_F5A")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1086")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1029")

    AnonymousTalk(    #20
        (
            "\x07\x05#40WThe path has already been opened...\x01",
            "#500W \x01",
            "#40WOpen the door, and step inside,\x01",
            "proof of your right to challenge\x01",
            "the ordeals inside in hand.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1083")

    label("loc_1029")


    AnonymousTalk(    #21
        (
            "\x07\x05#40WThe path has already been opened...\x01",
            "#500W \x01",
            "#40WOpen the door, and step inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1083")

    Jump("loc_120E")

    label("loc_1086")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1192")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1135")

    AnonymousTalk(    #22
        (
            "\x07\x05#40WThe path has already been opened...\x01",
            "#500W \x01",
            "#40WOpen the door, and step inside,\x01",
            "proof of your right to challenge\x01",
            "the ordeals inside in hand.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_118F")

    label("loc_1135")


    AnonymousTalk(    #23
        (
            "\x07\x05#40WThe path has already been opened...\x01",
            "#500W \x01",
            "#40WOpen the door, and step inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_118F")

    Jump("loc_120E")

    label("loc_1192")


    AnonymousTalk(    #24
        (
            "\x07\x05#40WBring to me the fists of steel which\x01",
            "nothing in this world can move.\x01",
            "#500W \x01",
            "#40WOnly then shall the door open...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_120E")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1244")
    Call(0, 9)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1241")
    Call(0, 12)

    label("loc_1241")

    Jump("loc_12AF")

    label("loc_1244")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1266")
    Call(0, 9)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1263")
    Call(0, 12)

    label("loc_1263")

    Jump("loc_12AF")

    label("loc_1266")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1297")
    Call(0, 9)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1294")
    Call(0, 12)

    label("loc_1294")

    Jump("loc_1297")

    label("loc_1297")

    Jump("loc_12AF")

    label("loc_129A")

    Call(0, 9)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12AF")
    Call(0, 12)

    label("loc_12AF")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_11_E84 end

    def Function_12_12BB(): pass

    label("Function_12_12BB")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x8, 0)
    OP_70(0x8, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x8)
    Sleep(500)

    def lambda_1324():
        OP_6B(2750, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1324)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0x10, 0, 0x0)
    NewScene("ED6_DT21/P9002   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_12BB end

    def Function_13_1371(): pass

    label("Function_13_1371")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, 79700, 0, -62570, 270)
    SetChrPos(0x1, 79520, 0, -63940, 270)
    SetChrPos(0x2, 81380, 0, -62830, 270)
    SetChrPos(0x3, 81460, 0, -64090, 270)
    OP_6D(78510, 0, -63230, 0)
    OP_67(0, 6170, -10000, 0)
    OP_6B(3190, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_13_1371 end

    def Function_14_141C(): pass

    label("Function_14_141C")

    TalkBegin(0xFF)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05The doors are locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_14_141C end

    SaveToFile()

Try(main)
