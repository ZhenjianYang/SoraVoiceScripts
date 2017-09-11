from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4311   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4311.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60089",
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
        'Chamberlain Raymond',                  # 9
        'Special Ops Soldier',                  # 10
        'Special Ops Soldier',                  # 11
        'Special Ops Soldier',                  # 12
        'Special Ops Soldier',                  # 13
        'Special Ops Soldier',                  # 14
        'Kloe',                                 # 15
        'Olivier',                              # 16
        'Scherazard',                           # 17
        '1st Lieutenant Schwarz',               # 18
        'Sieg',                                 # 19
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


    AddCharChip(
        'ED6_DT07/CH00100 ._CH',             # 00
        'ED6_DT07/CH00101 ._CH',             # 01
        'ED6_DT07/CH00110 ._CH',             # 02
        'ED6_DT07/CH00111 ._CH',             # 03
        'ED6_DT07/CH00170 ._CH',             # 04
        'ED6_DT07/CH00171 ._CH',             # 05
        'ED6_DT07/CH01570 ._CH',             # 06
        'ED6_DT07/CH01330 ._CH',             # 07
        'ED6_DT06/CH20143 ._CH',             # 08
        'ED6_DT07/CH00030 ._CH',             # 09
        'ED6_DT07/CH00020 ._CH',             # 0A
        'ED6_DT07/CH02090 ._CH',             # 0B
        'ED6_DT07/CH02320 ._CH',             # 0C
        'ED6_DT06/CH20042 ._CH',             # 0D
        'ED6_DT06/CH20113 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH00100P._CP',             # 00
        'ED6_DT07/CH00101P._CP',             # 01
        'ED6_DT07/CH00110P._CP',             # 02
        'ED6_DT07/CH00111P._CP',             # 03
        'ED6_DT07/CH00170P._CP',             # 04
        'ED6_DT07/CH00171P._CP',             # 05
        'ED6_DT07/CH01570P._CP',             # 06
        'ED6_DT07/CH01330P._CP',             # 07
        'ED6_DT06/CH20143P._CP',             # 08
        'ED6_DT07/CH00030P._CP',             # 09
        'ED6_DT07/CH00020P._CP',             # 0A
        'ED6_DT07/CH02090P._CP',             # 0B
        'ED6_DT07/CH02320P._CP',             # 0C
        'ED6_DT06/CH20042P._CP',             # 0D
        'ED6_DT06/CH20113P._CP',             # 0E
    )

    DeclNpc(
        X                   = -11850,
        Z                   = 0,
        Y                   = 20220,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 25980,
        TriggerZ            = 0,
        TriggerY            = 50580,
        TriggerRange        = 800,
        ActorX              = 25690,
        ActorZ              = 1500,
        ActorY              = 51500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22140,
        TriggerZ            = 0,
        TriggerY            = 50600,
        TriggerRange        = 800,
        ActorX              = 21830,
        ActorZ              = 890,
        ActorY              = 51760,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 18200,
        TriggerZ            = 0,
        TriggerY            = 51350,
        TriggerRange        = 800,
        ActorX              = 18200,
        ActorZ              = 1800,
        ActorY              = 51350,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 14200,
        TriggerZ            = 0,
        TriggerY            = 51310,
        TriggerRange        = 800,
        ActorX              = 14200,
        ActorZ              = 2000,
        ActorY              = 51310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 10220,
        TriggerZ            = 0,
        TriggerY            = 51150,
        TriggerRange        = 800,
        ActorX              = 10220,
        ActorZ              = 1200,
        ActorY              = 51150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 24340,
        TriggerZ            = 0,
        TriggerY            = 45480,
        TriggerRange        = 800,
        ActorX              = 24340,
        ActorZ              = 500,
        ActorY              = 45480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -13210,
        TriggerZ            = 0,
        TriggerY            = 18820,
        TriggerRange        = 800,
        ActorX              = -11850,
        ActorZ              = 1500,
        ActorY              = 20220,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_37E",          # 00, 0
        "Function_1_450",          # 01, 1
        "Function_2_451",          # 02, 2
        "Function_3_467",          # 03, 3
        "Function_4_46C",          # 04, 4
        "Function_5_958",          # 05, 5
        "Function_6_1996",         # 06, 6
        "Function_7_1B1A",         # 07, 7
        "Function_8_1BF0",         # 08, 8
        "Function_9_1CDC",         # 09, 9
        "Function_10_1DCA",        # 0A, 10
        "Function_11_1ECC",        # 0B, 11
        "Function_12_3057",        # 0C, 12
    )


    def Function_0_37E(): pass

    label("Function_0_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_395")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 11)

    label("loc_395")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_3A1"),
        (SWITCH_DEFAULT, "loc_3B4"),
    )


    label("loc_3A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B1")
    Event(0, 5)

    label("loc_3B1")

    Jump("loc_3B4")

    label("loc_3B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 6)), scpexpr(EXPR_END)), "loc_44F")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    SetChrFlags(0x9, 0x800)
    SetChrFlags(0xA, 0x800)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xC, 0x800)
    SetChrPos(0x9, -11150, 0, 15510, 315)
    SetChrPos(0xA, -11000, 0, 17300, 0)
    SetChrPos(0xB, -12500, 0, 17280, 270)
    SetChrPos(0xC, -13000, 0, 16040, 225)
    SetChrChipByIndex(0x9, 13)
    SetChrChipByIndex(0xA, 13)
    SetChrChipByIndex(0xB, 13)
    SetChrChipByIndex(0xC, 13)

    label("loc_44F")

    Return()

    # Function_0_37E end

    def Function_1_450(): pass

    label("Function_1_450")

    Return()

    # Function_1_450 end

    def Function_2_451(): pass

    label("Function_2_451")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_466")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_451")

    label("loc_466")

    Return()

    # Function_2_451 end

    def Function_3_467(): pass

    label("Function_3_467")

    Call(0, 4)
    Return()

    # Function_3_467 end

    def Function_4_46C(): pass

    label("Function_4_46C")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Rest\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_511")
    OP_20(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    Sleep(3500)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_511")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52B")
    FadeToBright(300, 0)
    TalkEnd(0x8)
    Return()

    label("loc_52B")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 7)), scpexpr(EXPR_END)), "loc_596")

    ChrTalk(    #0
        0x8,
        "Ahh, yes. That key...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "You should be able to use that\x01",
            "to enter the Crest Room.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_954")

    label("loc_596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_END)), "loc_627")

    ChrTalk(    #2
        0x8,
        (
            "There's a spare key to that\x01",
            "door. It's here somewhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "If memory serves, I believe\x01",
            "it's hidden somewhere in the\x01",
            "Gallery...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_954")

    label("loc_627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8CD")
    OP_A2(0x679)
    OP_28(0x4C, 0x1, 0x10)
    EventBegin(0x0)
    OP_69(0x8, 0x3E8)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05Estelle explained that the door was locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #5
        0x8,
        "Ahh...so it is locked, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "The key is normally in the\x01",
            "possession of the Intelligence\x01",
            "Division company commander...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "I believe he left when the\x01",
            "terrorists showed up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#580FHuh...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#013FWhich means that it was taken\x01",
            "by the ones who ambushed Lt.\x01",
            "Schwarz and her men...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x108,
        (
            "#074FNot good.\x01",
            "There's no time to go back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        "Just a moment...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "There's a spare key to that\x01",
            "door. It's here somewhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "If memory serves, I believe\x01",
            "it's hidden somewhere in the\x01",
            "Gallery...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#005FRoger that. Gallery!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x102,
        "#012FLet's hurry.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_954")

    label("loc_8CD")


    ChrTalk(    #16
        0x8,
        "Thank you for helping me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "Ah, yes. If you get tired, feel\x01",
            "free to come back here to rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        "I can get you some beverages.\x02",
    )

    CloseMessageWindow()

    label("loc_954")

    TalkEnd(0x8)
    Return()

    # Function_4_46C end

    def Function_5_958(): pass

    label("Function_5_958")

    EventBegin(0x0)
    OP_6D(-11300, 0, 20870, 0)
    OP_67(0, 6220, -10000, 0)
    OP_6B(1820, 0)
    OP_6C(45000, 0)
    OP_6E(487, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0x8, -11780, 0, 20150, 225)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, -16850, 0, 13660, 45)
    SetChrPos(0x108, -18160, 0, 13760, 45)
    SetChrPos(0x102, -16690, 0, 12820, 45)
    SetChrPos(0x9, -10960, 0, 18200, 0)
    SetChrPos(0xA, -12000, 0, 18190, 0)
    SetChrPos(0xB, -14950, 0, 18980, 90)
    SetChrPos(0xC, -13770, 0, 18980, 270)
    FadeToBright(1000, 0)
    OP_6D(-14900, 0, 16920, 2000)
    OP_4A(0x8, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #19
        0x8,
        "Who...who are you people...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#004FCrap... We totally picked\x01",
            "the wrong room!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)

    def lambda_B09():
        TurnDirection(0xFE, 0x101, 250)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B09)

    def lambda_B17():
        TurnDirection(0xFE, 0x101, 200)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B17)

    def lambda_B25():
        TurnDirection(0xFE, 0x101, 150)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_B25)
    TurnDirection(0xB, 0x101, 200)

    ChrTalk(    #21
        0xB,
        (
            "#3PHmmm...\x01",
            "What are you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xA,
        (
            "#4P*hic*...\x01",
            "Ain't seen you before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#019FGood evening.\x01",
            "We're with the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xC,
        "#6PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x108,
        (
            "#070FNo need to get up. Just enjoy\x01",
            "yourselves and rest well.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C13():
        OP_92(0xFE, 0x8, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C13)
    Sleep(50)

    def lambda_C2D():
        OP_92(0xFE, 0xA, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C2D)
    Sleep(50)

    def lambda_C47():
        OP_92(0xFE, 0xC, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_C47)
    OP_6D(-13120, 0, 18720, 500)
    OP_44(0x101, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x102, 0xFF)
    Battle(0x3AF, 0x0, 0x2, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_C8C"),
        (SWITCH_DEFAULT, "loc_C8F"),
    )


    label("loc_C8C")

    OP_B4(0x0)
    Return()

    label("loc_C8F")

    EventBegin(0x0)
    OP_6D(-13760, 0, 18120, 0)
    SetChrFlags(0x9, 0x800)
    SetChrFlags(0xA, 0x800)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xC, 0x800)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0x9, -11150, 0, 15510, 315)
    SetChrPos(0xA, -11000, 0, 17300, 0)
    SetChrPos(0xB, -12500, 0, 17280, 270)
    SetChrPos(0xC, -13000, 0, 16040, 225)
    SetChrChipByIndex(0x9, 13)
    SetChrChipByIndex(0xA, 13)
    SetChrChipByIndex(0xB, 13)
    SetChrChipByIndex(0xC, 13)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    SetChrPos(0x101, -15250, 0, 17530, 90)
    SetChrPos(0x108, -15870, 0, 15890, 90)
    SetChrPos(0x102, -14310, 0, 16540, 90)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, -12050, -600, 20370, 225)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #26
        0x101,
        (
            "#006FWhew...\x01",
            "Well, that's taken care of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x108,
        (
            "#071FThey're too drunk to really\x01",
            "know what's going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        (
            "#010FIt's like some kind of bar,\x01",
            "same as the one in the castle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        "P-Please...don't kill me...!\x02",
    )

    CloseMessageWindow()

    def lambda_E5D():
        OP_6D(-12770, 0, 19310, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E5D)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)

    def lambda_E84():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E84)
    Sleep(200)

    def lambda_E97():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E97)
    Sleep(200)

    def lambda_EAA():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_EAA)
    WaitChrThread(0x101, 0x2)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_ECF():
        OP_8F(0xFE, 0xFFFFD0EE, 0x0, 0x4F92, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_ECF)

    def lambda_EEA():

        label("loc_EEA")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_EEA")

    QueueWorkItem2(0x108, 1, lambda_EEA)

    def lambda_EFB():

        label("loc_EFB")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_EFB")

    QueueWorkItem2(0x101, 1, lambda_EFB)

    def lambda_F0C():

        label("loc_F0C")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_F0C")

    QueueWorkItem2(0x102, 1, lambda_F0C)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #30
        0x8,
        "I-I-I'm not with them!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#007FWe know that. You work\x01",
            "at the villa, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x102,
        (
            "#010FWe've come to help, at the request\x01",
            "of Her Majesty the Queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        "Wha... R-Really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        "You're honestly here to save us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#006FYes, so would you calm down,\x01",
            "already?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1028():
        OP_6D(-15830, 0, 17600, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1028)
    OP_8E(0x8, 0xFFFFCD7E, 0x0, 0x538E, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFFC22A, 0x0, 0x51EA, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFFC054, 0x0, 0x46BE, 0xBB8, 0x0)
    OP_44(0x101, 0x1)
    OP_8C(0x101, 270, 0)

    ChrTalk(    #36
        0x8,
        "#3PWhew... Aidios be praised...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "#3PI thought I was done for\x01",
            "when my reporter friend\x01",
            "was taken away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        "#3PI hope he's all right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#505FReporter friend...?\x02\x03",

            "#004FYou must mean Nial!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        "#3P...You know him?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #41
        "\x07\x05Estelle explained that Nial had gone missing and was still unaccounted for.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #42
        0x8,
        (
            "#3PAhh, I see. Yes, I'm the\x01",
            "one who contacted him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        (
            "#3PHe came to get an interview\x01",
            "with the princess, who is being\x01",
            "guarded here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "#3PHis passion for his work is hard to\x01",
            "argue with, so I wound up sneaking\x01",
            "him in and showing him the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x108,
        (
            "#070FBut he was spotted, and\x01",
            "taken prisoner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "#3PYes...and much to my shame, it\x01",
            "was only then that I realized\x01",
            "the severity of the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "#3PI heard that Her Highness was being\x01",
            "kept here, to protect her from any\x01",
            "potential terrorist assault.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#3PBut the truth is that she's\x01",
            "being held prisoner by the\x01",
            "Intelligence Division...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "#3PI was so glad that she was \x01",
            "coming that it simply had \x01",
            "never occurred to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        "#3PI am truly unfit for my position...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#506FCome on...\x01",
            "No need to be so depressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x102,
        (
            "#012FWould you happen to have any\x01",
            "idea where the prisoners are\x01",
            "being held?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "#3PYes... They've all been gathered\x01",
            "in the Crest Room, which is the\x01",
            "innermost chamber.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "#3PIt's a large banquet hall,\x01",
            "used for events like the\x01",
            "formal signing of treaties.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4C, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_163D")

    ChrTalk(    #55
        0x101,
        "#006FGot it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x108,
        "#070FAll right, let's go check it out.\x02",
    )

    CloseMessageWindow()
    OP_28(0x4C, 0x1, 0x4)
    Jump("loc_18E8")

    label("loc_163D")

    OP_A2(0x679)
    OP_28(0x4C, 0x1, 0x10)

    ChrTalk(    #57
        0x101,
        (
            "#004FA big hall inside...\x01",
            "Maybe over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x108,
        (
            "#072FYes...the room behind the big,\x01",
            "locked door.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        "#3PAhh...so it is locked, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        (
            "#3PThe key is normally in the\x01",
            "possession of the Intelligence\x01",
            "Division company commander...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "#3PI believe he left when the\x01",
            "terrorists showed up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#580FHuh...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x102,
        (
            "#013FWhich means that it was taken\x01",
            "by the ones who ambushed Lt.\x01",
            "Schwarz and her men...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x108,
        (
            "#074FNot good.\x01",
            "There's no time to go back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        "#3PJust a moment...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "#3PThere's a spare key to that\x01",
            "door. It's here somewhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "#3PIf memory serves, I believe\x01",
            "it's hidden somewhere in the\x01",
            "Gallery...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#005FRoger that. Gallery!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x102,
        "#012FLet's hurry.\x02",
    )

    CloseMessageWindow()

    label("loc_18E8")

    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrPos(0x8, -11850, 0, 20220, 225)
    SetChrPos(0x101, -16149, 0, 17150, 180)
    SetChrPos(0x102, -16149, 0, 17150, 180)
    SetChrPos(0x108, -16149, 0, 17150, 180)
    OP_6D(-16149, 0, 17150, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_A2(0x656)
    EventEnd(0x0)
    Return()

    # Function_5_958 end

    def Function_6_1996(): pass

    label("Function_6_1996")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AC4")
    EventBegin(0x0)
    OP_A2(0x657)
    OP_28(0x4C, 0x1, 0x20)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #70
        "\x07\x05There's a large, scarlet vase here.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #71
        (
            "\x07\x05Estelle and company found something \x01",
            "attached to its underside.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(400)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #72
        "\x07\x00Found \x07\x02Spare Key\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3E(0x36F, 1)

    ChrTalk(    #73
        0x101,
        "#006FThis is it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x102,
        (
            "#010FNow, we should be able to\x01",
            "open that inner door.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_1B19")

    label("loc_1AC4")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #75
        "\x07\x05There's a large, scarlet vase here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_1B19")

    Return()

    # Function_6_1996 end

    def Function_7_1B1A(): pass

    label("Function_7_1B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BA4")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #76
        "\x07\x05There's a red plate here.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #77
        "\x07\x05There appears to be nothing special about it.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_1BEC")

    label("loc_1BA4")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #78
        "\x07\x05There's a red plate here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_1BEC")

    TalkEnd(0xFF)
    Return()

    # Function_7_1B1A end

    def Function_8_1BF0(): pass

    label("Function_8_1BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C85")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #79
        "\x07\x05There is an Eastern-style vase here.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #80
        "\x07\x05There appears to be nothing special about it.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_1CD8")

    label("loc_1C85")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #81
        "\x07\x05There is an Eastern-style vase here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_1CD8")

    TalkEnd(0xFF)
    Return()

    # Function_8_1BF0 end

    def Function_9_1CDC(): pass

    label("Function_9_1CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D72")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #82
        "\x07\x05There is an Imperial-style vase here.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #83
        "\x07\x05There appears to be nothing special about it.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_1DC6")

    label("loc_1D72")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #84
        "\x07\x05There is an Imperial-style vase here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_1DC6")

    TalkEnd(0xFF)
    Return()

    # Function_9_1CDC end

    def Function_10_1DCA(): pass

    label("Function_10_1DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E6B")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #85
        (
            "\x07\x05There are rows of art catalogues\x01",
            "on the shelf.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #86
        "\x07\x05There appears to be nothing special about them.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_1EC8")

    label("loc_1E6B")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #87
        (
            "\x07\x05There are rows of art catalogues\x01",
            "on the shelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_1EC8")

    TalkEnd(0xFF)
    Return()

    # Function_10_1DCA end

    def Function_11_1ECC(): pass

    label("Function_11_1ECC")

    SetMapFlags(0x2000000)
    EventBegin(0x0)
    OP_6D(17870, 0, -11650, 0)
    OP_67(0, 4740, -10000, 0)
    OP_6B(3019, 0)
    OP_6C(315000, 0)
    OP_6E(261, 0)
    SetChrPos(0xE, 11330, 0, -10500, 135)
    SetChrPos(0x12, 12980, 0, -9840, 225)
    SetChrPos(0x11, 12980, 0, -9840, 270)
    SetChrPos(0x10, 12140, 0, -12950, 0)
    SetChrPos(0xF, 10420, 0, -12050, 90)
    SetChrPos(0x108, 11130, 0, -13550, 0)
    SetChrPos(0x101, 13440, 0, -12780, 315)
    SetChrPos(0x102, 14010, 0, -11910, 315)
    TurnDirection(0xE, 0x11, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x108, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 14)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x12, 0x80)
    OP_6D(11600, 0, -10880, 3000)

    ChrTalk(    #88
        0x11,
        (
            "#175FWords cannot express my shame.\x02\x03",

            "If not for my ineptitude, none of\x01",
            "this would have come to pass...\x02\x03",

            "I am so ashamed I could take my own life,\x01",
            "were it something to be permitted.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #89
        0xE,
        "Princess Klaudia",
        (
            "#401FPlease do not say such things.\x02\x03",

            "I'm just happy to see\x01",
            "you alive and unharmed.\x02\x03",

            "Thank you for coming to save me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x11,
        "#171FYour Highness...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x12, 400)

    ChrTalk(    #91
        0x101,
        (
            "#6P#506FNot that I'm not moved by all\x01",
            "this, but I have to ask...\x02\x03",

            "#505FWhy is Sieg still here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x12,
        "#310FScree?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x101, 400)

    ChrTalk(    #93
        0x11,
        (
            "#170FHa ha. He is Her Highness's\x01",
            "escort, as well as a messenger\x01",
            "for the Royal Guardsmen.\x02\x03",

            "After all, did he not deliver\x01",
            "the letter to your hotel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        "#6P#004FOH! Th-That night!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x102,
        (
            "#4P#010FI thought it might've been him.\x02\x03",

            "That must also be how you learned\x01",
            "of Her Majesty's request...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x11,
        (
            "#176FYes, I heard of it from Sieg.\x01",
            "Her Majesty sent word through\x01",
            "him from the Royal Keep.\x02\x03",

            "#175FBut the Crest Room in which Princess\x01",
            "Klaudia was held had no windows for\x01",
            "Sieg to use...\x02\x03",

            "I was very worried when I was\x01",
            "unable to make contact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#6P#007FYou just about gave me a heart\x01",
            "attack, though, when you sent\x01",
            "that message to us.\x02\x03",

            "#509FSieg, that was just plain mean\x01",
            "of you to leave that letter and\x01",
            "not let us know it was you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x12,
        "#310FScree...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    NpcTalk(    #99
        0xE,
        "Princess Klaudia",
        (
            "#408FHa ha...\x01",
            "He says he's sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#6P#001FHa ha ha... It's okay.\x02\x03",

            "#006FBy the way, have all the Special\x01",
            "Ops troops been dealt with?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_255F():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_255F)

    ChrTalk(    #101
        0x11,
        (
            "#178FAlmost all of the soldiers in\x01",
            "the villa have been restrained.\x02\x03",

            "However, there are quite a\x01",
            "few left in Grancel Castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x10,
        (
            "#3P#026FMuch of the Royal Army is under \x01",
            "Intelligence Division control,\x01",
            "even outside of Grancel.\x02\x03",

            "#022FIf we're not careful, we run the risk of them\x01",
            "seizing control of this building and branding\x01",
            "us all as rebels.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #103
        0x101,
        (
            "#6P#580FWhoa... I hadn't even thought\x01",
            "about that.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)

    ChrTalk(    #104
        0x102,
        (
            "#4P#012FIt's a good point...\x02\x03",

            "I think it would be best if we were to get Kloe\x01",
            "to a safer location, at the very least.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #105
        0xE,
        "Princess Klaudia",
        "#404F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xF,
        (
            "#030FPerhaps we could seek asylum at the Erebonian\x01",
            "or Republic embassies?\x02\x03",

            "#035FSince they're considered foreign territory,\x01",
            "it would make it very difficult for them to\x01",
            "lay a hand on her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x108,
        (
            "#070FThere's also that Special Ops ship that we\x01",
            "seized nearby. We could use that to allow her\x01",
            "to flee the country for the time being.\x02\x03",

            "It wouldn't solve the whole problem, but it\x01",
            "would buy us some time to find a better\x01",
            "solution, at the very least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x11,
        (
            "#176FI agree... Regardless, we need to find some way\x01",
            "to get her to safety.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #109
        0xE,
        "Princess Klaudia",
        (
            "#406F...\x02\x03",

            "#402FUm...everyone...?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x108, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2A5B():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A5B)

    def lambda_2A69():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A69)

    def lambda_2A77():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2A77)

    def lambda_2A85():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2A85)

    def lambda_2A93():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2A93)

    def lambda_2AA1():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2AA1)

    NpcTalk(    #110
        0xE,
        "Princess Klaudia",
        (
            "#402FI understand the difficulties of the current\x01",
            "situation, but would it be possible to\x01",
            "make an official request of the bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        "#6P#004FWha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        (
            "#4P#010FThe hostages have been rescued,\x01",
            "so I think it'll be all right.\x02\x03",

            "Of course, it depends on what\x01",
            "the contents of the request are.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #113
        0xE,
        "Princess Klaudia",
        (
            "#406FIf so...I must ask you to\x01",
            "do the impossible.\x02\x03",

            "#403FWill you help in retaking the royal\x01",
            "castle and rescuing Her Majesty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x11,
        "#173FY-Your Highness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        (
            "#6P#006FI see... That's right.\x02\x03",

            "This time we have to help\x01",
            "the queen!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x108,
        (
            "#074FTo be honest, I consider the\x01",
            "question to be ridiculous,\x01",
            "because the answer is obvious.\x02\x03",

            "#072FBut, Your Highness...this is no\x01",
            "small thing you're asking for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x10,
        (
            "#3P#025FQuite right...\x02\x03",

            "There's no chance that a frontal\x01",
            "assault would work, even with the\x01",
            "capabilities of everyone here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x102,
        (
            "#4P#013FI think that captured Special\x01",
            "Ops ship has potential...\x02\x03",

            "But we're going to need some\x01",
            "kind of seriously clever trick.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #119
        0xE,
        "Princess Klaudia",
        (
            "#406F...I have an idea.\x02\x03",

            "#402FIf everyone will please look at this...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #120
        "\x07\x05Princess Klaudia produced a very old-looking map.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x357, 1)
    OP_AD(0x40026, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #121
        "#004FHmm... What's this map of?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 300, -1, -1)
    SetChrName("Princess Klaudia")

    AnonymousTalk(    #122
        (
            "#402FIt's an ancient diagram of the\x01",
            "sewers below Grancel.\x02\x03",

            "One of the things it lays out\x01",
            "is the path that leads to the\x01",
            "Castle Cellar.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(0, 0, -1)
    OP_AE(0x1F4)
    OP_20(0x5DC)
    OP_21()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4260   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_1ECC end

    def Function_12_3057(): pass

    label("Function_12_3057")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #123
        (
            "\x07\x05'The King's Throne' - The favorite seat\x01",
            "of the late King Edgar III when staying\x01",
            "in the Erbe Royal Villa.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_12_3057 end

    SaveToFile()

Try(main)
