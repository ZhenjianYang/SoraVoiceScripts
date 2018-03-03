from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0110   ._SN',
        MapName             = 'event',
        Location            = 'E0110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
        'Josette',                              # 9
        'Kyle',                                 # 10
        'Don',                                  # 11
        'Lonnie',                               # 12
        'Aaron',                                # 13
        'Rosco',                                # 14
        'Ryan',                                 # 15
        'Lonnie',                               # 16
        'Lonnie',                               # 17
        "Crewman's Voice",                      # 18
        'Target Camera',                        # 19
        'Sealing Stone 4',                      # 20
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


    AddCharChip(
        'ED6_DT27/CH03100 ._CH',             # 00
        'ED6_DT26/CH20416 ._CH',             # 01
        'ED6_DT27/CH03760 ._CH',             # 02
        'ED6_DT07/CH01380 ._CH',             # 03
        'ED6_DT27/CH03761 ._CH',             # 04
        'ED6_DT27/CH03101 ._CH',             # 05
        'ED6_DT27/CH03771 ._CH',             # 06
        'ED6_DT26/CH20621 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT27/CH03100P._CP',             # 00
        'ED6_DT26/CH20416P._CP',             # 01
        'ED6_DT27/CH03760P._CP',             # 02
        'ED6_DT07/CH01380P._CP',             # 03
        'ED6_DT27/CH03761P._CP',             # 04
        'ED6_DT27/CH03101P._CP',             # 05
        'ED6_DT27/CH03771P._CP',             # 06
        'ED6_DT26/CH20621P._CP',             # 07
    )

    DeclNpc(
        X                   = 45640,
        Z                   = 0,
        Y                   = 6930,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -21870,
        Z                   = 850,
        Y                   = 4940,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 47460,
        Z                   = 0,
        Y                   = 76210,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -24300,
        Z                   = -1000,
        Y                   = 4970,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 45780,
        Z                   = 0,
        Y                   = 6950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 51430,
        Z                   = 0,
        Y                   = 2760,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -24200,
        Z                   = -250,
        Y                   = 4300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -24370,
        Z                   = -250,
        Y                   = 5510,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xCC,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -17680,
        TriggerZ            = 0,
        TriggerY            = 3110,
        TriggerRange        = 1500,
        ActorX              = -17800,
        ActorZ              = 4300,
        ActorY              = 4950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -22380,
        TriggerZ            = 650,
        TriggerY            = 5380,
        TriggerRange        = 1000,
        ActorX              = -22380,
        ActorZ              = 1650,
        ActorY              = 5380,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2B2",          # 00, 0
        "Function_1_34A",          # 01, 1
        "Function_2_558",          # 02, 2
        "Function_3_56E",          # 03, 3
        "Function_4_5EC",          # 04, 4
        "Function_5_5F3",          # 05, 5
        "Function_6_67F",          # 06, 6
        "Function_7_874",          # 07, 7
        "Function_8_A1B",          # 08, 8
        "Function_9_2FAD",         # 09, 9
        "Function_10_2FF9",        # 0A, 10
        "Function_11_303E",        # 0B, 11
        "Function_12_3357",        # 0C, 12
        "Function_13_362C",        # 0D, 13
        "Function_14_388E",        # 0E, 14
        "Function_15_4B50",        # 0F, 15
        "Function_16_51F1",        # 10, 16
    )


    def Function_0_2B2(): pass

    label("Function_0_2B2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BE")

    label("loc_2BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_349")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 0)), scpexpr(EXPR_END)), "loc_2E4")
    OP_A3(0x2508)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 14)
    Jump("loc_349")

    label("loc_2E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_2FE")
    OP_A3(0x2507)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 13)
    Jump("loc_349")

    label("loc_2FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_318")
    OP_A3(0x2506)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 12)
    Jump("loc_349")

    label("loc_318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_332")
    OP_A3(0x2505)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)
    Jump("loc_349")

    label("loc_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_349")
    OP_A3(0x2504)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)

    label("loc_349")

    Return()

    # Function_0_2B2 end

    def Function_1_34A(): pass

    label("Function_1_34A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_362")
    OP_B1("E0110_n")
    Jump("loc_37E")

    label("loc_362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_375")
    OP_B1("E0110_n")
    Jump("loc_37E")

    label("loc_375")

    OP_B1("E0110_y")

    label("loc_37E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_455")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_446")
    ClearChrFlags(0x1B, 0x80)
    OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x1B, -17800, 4300, 4950, 0)
    LoadEffect(0x7, "map\\mp253_00.eff")
    LoadEffect(0x6, "map\\mp253_01.eff")
    PlayEffect(0x7, 0x7, 0x1B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x1B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_44A")

    label("loc_446")

    OP_64(0x0, 0x1)

    label("loc_44A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_455")
    OP_64(0x1, 0x1)

    label("loc_455")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B4")
    OP_10(0x0, 0x0)
    OP_10(0x6, 0x1)
    OP_22(0x7A, 0x1, 0x50)
    OP_76(0x7, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0x7, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0x7, 0x2, 0x1, 0xFFFFFFFE, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_4D9")

    label("loc_4B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_4D3")
    OP_10(0x0, 0x0)
    OP_10(0x5, 0x1)
    OP_10(0x6, 0x0)
    Jump("loc_4D9")

    label("loc_4D3")

    OP_10(0x0, 0x1)
    OP_10(0x6, 0x0)

    label("loc_4D9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_529")
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x40A, 0x0)
    ExitThread()
    OP_71(0x40B, 0x0)
    ExitThread()
    OP_71(0x40C, 0x0)
    ExitThread()
    OP_76(0x4, 0x5, 0x2, 0x4, 0x8, 0x0, 0x0, 0x0)
    Jump("loc_557")

    label("loc_529")

    OP_71(0x40E, 0x0)
    ExitThread()
    OP_72(0x40B, 0x0)
    ExitThread()
    OP_64(0x0, 0x1)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x40C, 0x0)
    ExitThread()

    label("loc_557")

    Return()

    # Function_1_34A end

    def Function_2_558(): pass

    label("Function_2_558")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_558")

    label("loc_56D")

    Return()

    # Function_2_558 end

    def Function_3_56E(): pass

    label("Function_3_56E")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0x11,
        (
            "#200FSorry, but would you mind looking for Don for\x01",
            "me?\x02\x03",

            "I want to make sure we're going to the right\x01",
            "destination.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_56E end

    def Function_4_5EC(): pass

    label("Function_4_5EC")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_4_5EC end

    def Function_5_5F3(): pass

    label("Function_5_5F3")

    TalkBegin(0xFE)

    ChrTalk(    #1
        0xFE,
        "The boss was working like mad this morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "I'm guessing he's probably tired and taking a\x01",
            "nap right about now as a result.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_5F3 end

    def Function_6_67F(): pass

    label("Function_6_67F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76C")
    OP_A2(0x3)

    ChrTalk(    #3
        0xFE,
        "Hey there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "My mom was really happy when I told her that\x01",
            "we're operating a courier service instead of\x01",
            "being sky bandits now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Haha. Looks like I might actually be able to go\x01",
            "home and see everyone this year!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_870")

    label("loc_76C")


    ChrTalk(    #6
        0xFE,
        (
            "My mom was really happy when I told her that\x01",
            "we're operating a courier service instead of\x01",
            "being sky bandits now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Now I'm finally earning an honest living, it's\x01",
            "probably about time I started making up for all\x01",
            "the trouble I've caused everyone at home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_870")

    TalkEnd(0xFE)
    Return()

    # Function_6_67F end

    def Function_7_874(): pass

    label("Function_7_874")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97E")
    OP_A2(0x4)

    ChrTalk(    #8
        0xFE,
        "G-Good day, Josette...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "I still can't believe your brothers were good\x01",
            "enough to make me an employee of the company\x01",
            "after I ran away from being a bandit that time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "I'm really never going to be able to repay them\x01",
            "for their kindness...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A17")

    label("loc_97E")


    ChrTalk(    #11
        0xFE,
        (
            "Now we're earning an honest living, I'm gonna\x01",
            "really have to put my back into my work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "You're gonna see me work like I've never worked\x01",
            "before!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A17")

    TalkEnd(0xFE)
    Return()

    # Function_7_874 end

    def Function_8_A1B(): pass

    label("Function_8_A1B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-23640, 0, 7960, 0)
    OP_67(0, 5200, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(330000, 0)
    OP_6E(280, 0)
    OP_22(0x7A, 0x1, 0x50)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x10B, 0x40)
    SetChrPos(0x11, -24260, -1000, 4970, 270)
    SetChrPos(0x12, -21870, 650, 4940, 315)
    SetChrPos(0x10B, -18620, 3000, 4800, 270)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    OP_76(0xB, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x1, 0x1, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x2, 0x1, 0xFFFFFFFC, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(2000, 0)
    OP_6B(3000, 2000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #13
        0x10B,
        (
            "#210FValleria Lake's visible on the other side of the \x01",
            "mountain range.\x02\x03",

            "Which means we're almost at the border!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x12,
        (
            "#190F#0CRight on schedule, too.\x02\x03",

            "Reduce our speed to 60%, Kyle. Keep our course\x01",
            "and altitude the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        (
            "#200FYou got it. Reducing speed to 60%.\x02\x03",

            "Course and altitude're both good to go.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    Sleep(200)

    ChrTalk(    #16
        0x12,
        (
            "#490FAll right! We're lookin' good.\x02\x03",

            "Now all we need is to stay this course\x01",
            "and we'll be there in no time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        (
            "#203FWhew... Time for us to kick back and relax.\x01",
            "Finally.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D3E():
        OP_8F(0xFE, 0xFFFFB8D4, 0xBB8, 0x12C0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_D3E)
    WaitChrThread(0x10B, 0x1)
    Sleep(500)

    ChrTalk(    #18
        0x10B,
        (
            "#211FGood job, guys.\x02\x03",

            "Haha. It's good to know we should be able\x01",
            "to make this delivery on time, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x12,
        (
            "#191FYou're tellin' me!\x02\x03",

            "The Capua Delivery Service is all about trust, \x01",
            "reliability, and happy customers! Without those, \x01",
            "we've got nothing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        (
            "#202FI still can't believe this is actually our thing\x01",
            "now, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10B,
        (
            "#210FSame here... None of this would've been\x01",
            "possible if Queen Alicia hadn't pardoned\x01",
            "us, either.\x02\x03",

            "I don't think I've ever been as shocked as\x01",
            "I was when I found out we were off the\x01",
            "hook for EVERYTHING.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        (
            "#200FI know, right? And how she paid off our debts\x01",
            "with her own funds!\x02\x03",

            "She's the reason we can keep this baby here\x01",
            "an' keep on flying. No one can take the Bobcat\x01",
            "away from us now.\x02\x03",

            "And there's nothing in this world big enough to\x01",
            "pay off our debt to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x12,
        (
            "#490FDamn straight.\x02\x03",

            "Still, the least we can do is pay her back the \x01",
            "money she used on our behalf.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10B,
        (
            "#211FYeah. At the rate we're going, we should be\x01",
            "squared away on that front in no time.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    LoadEffect(0x1, "map\\\\mp001_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, -22580, 1700, 5540, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(500)
    OP_82(0x0, 0x0)
    OP_8C(0x12, 240, 500)
    Sleep(300)

    ChrTalk(    #25
        0x10B,
        (
            "#415FOh! Sounds like we've got ourselves a new\x01",
            "job to help with that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x12,
        "#198F*cough*\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0x83, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #27
        0x12,
        (
            "#190FHello! You've reached Capua Delivery Service!\x02\x03",

            "Yes... I see...\x02\x03",

            "...Tomorrow morning, then? Certainly.\x02\x03",

            "#198FAbsolutely. All right, we'll see you then.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0x83, 0x0, 0x64)
    Sleep(300)
    OP_8C(0x12, 315, 400)
    Sleep(300)

    ChrTalk(    #28
        0x10B,
        (
            "#415FSo I was right, then?\x01",
            "Where from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x12,
        (
            "#490FFrom Calvard, actually.\x02\x03",

            "Someone wants a small parcel delivered to Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x11,
        (
            "#200FIf it's Grancel, we can take care of that the day\x01",
            "after tomorrow.\x02\x03",

            "Man! Who would've guessed business would be\x01",
            "booming when we started the company up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10B,
        (
            "#211FIt makes sense, though. There aren't any other\x01",
            "delivery companies out there who can offer the\x01",
            "kinda flexibility we do.\x02\x03",

            "#213FOh, yeah. Speaking of the capital, I've been \x01",
            "meaning to ask...\x02\x03",

            "#210FWhat were you doing in the guild there this \x01",
            "morning, Don?\x02\x03",

            "I only just remembered it, but it did have me\x01",
            "wondering at the time.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #32
        0x12,
        (
            "#192FOh. Right.\x02\x03",

            "You've actually got a lil' something to do\x01",
            "with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10B,
        "#213FI do?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 100, 500)
    Sleep(300)

    ChrTalk(    #34
        0x12,
        (
            "#490FY'see, someone sent a letter to us from over\x01",
            "in the Empire.\x02\x03",

            "And here's the best part...\x02\x03",

            "#191FThat someone was none other than Joshua!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #35
        0x10B,
        "#414FR-Really?!\x02",
    )

    CloseMessageWindow()

    def lambda_16A0():
        OP_67(-23640, 0, 8150, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_16A0)

    def lambda_16B8():
        OP_67(0, 5050, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_16B8)

    def lambda_16D0():
        OP_8E(0xFE, 0xFFFFB9B0, 0xBB8, 0x10CC, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_16D0)
    WaitChrThread(0x10B, 0x1)
    OP_22(0xA3, 0x0, 0x50)

    def lambda_16F5():
        OP_96(0xFE, 0xFFFFBBA4, 0x0, 0xA50, 0xC8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_16F5)
    WaitChrThread(0x10B, 0x1)
    OP_23(0xA3)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_1720():
        OP_8E(0xFE, 0xFFFFB758, 0x0, 0xA50, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_1720)
    WaitChrThread(0x10B, 0x1)

    def lambda_1740():
        OP_8E(0xFE, 0xFFFFB758, 0x0, 0x12C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_1740)
    WaitChrThread(0x10B, 0x1)

    def lambda_1760():
        OP_8E(0xFE, 0xFFFFAF24, 0x0, 0x12C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_1760)
    WaitChrThread(0x10B, 0x1)
    Sleep(300)

    ChrTalk(    #36
        0x11,
        "#202FNow, there's someone we don't hear from often.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10B,
        (
            "#212FI can't believe you took this long to mention this!\x01",
            "I would've wanted to hear, like, RIGHT AWAY.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x12,
        (
            "#490F#5PMy bad! This morning was just so busy,\x01",
            "it slipped my mind.\x02\x03",

            "Anyway, why don't you do the honors for\x01",
            "us and read it out loud?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10B,
        "#415FWith pleasure!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x10B, 0x4)

    def lambda_18D1():
        OP_8E(0xFE, 0xFFFFAD6C, 0x28A, 0x1360, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_18D1)
    WaitChrThread(0x10B, 0x1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #40
        "\x07\x05Josette excitedly took the envelope from Don.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    def lambda_194B():
        OP_8F(0xFE, 0xFFFFAF24, 0x28A, 0x12C0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_194B)
    WaitChrThread(0x10B, 0x1)
    ClearChrFlags(0x10B, 0x4)
    Sleep(300)

    ChrTalk(    #41
        0x10B,
        "#415FOne second...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_8C(0x10B, 100, 500)
    Sleep(300)
    OP_62(0x10B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #42
        0x11,
        (
            "#200FI forgot how Joshua was going around the\x01",
            "Empire right now.\x02\x03",

            "I wonder what he's getting up to.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 270, 400)
    Sleep(300)

    ChrTalk(    #43
        0x12,
        (
            "#490F#5PYeah. Or where he is in the country.\x02\x03",

            "It's a damn big place, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        (
            "#202FWell, wherever he's at, I hope he's doing all right\x01",
            "for himself.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x11, 1)
    Sleep(500)

    ChrTalk(    #45
        0x11,
        (
            "#200FWhat's the hold up, Josette? You gonna read\x01",
            "that letter or not?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10B)
    Sleep(500)

    ChrTalk(    #46
        0x10B,
        "#416F#5P07:00 - Antique Artwork...\x02",
    )

    CloseMessageWindow()
    Sleep(800)
    OP_8C(0x12, 100, 500)
    Sleep(300)

    ChrTalk(    #47
        0x12,
        "#490F#5PHuh? What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x11,
        "#206F...That's not what it says, is it?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x10B, 270, 500)
    Sleep(300)

    ChrTalk(    #49
        0x10B,
        (
            "#212FYes, it is.\x02\x03",

            "Because this isn't a letter--this is the receipt\x01",
            "from this morning's delivery!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #50
        0x12,
        "#192F#5P#3SWhat?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #51
        0x11,
        "#206FNo way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10B,
        (
            "#212FIt's also the one that should have been given to\x01",
            "the person we delivered to for their records.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x12,
        "#192F#5PY-You're kiddin' me...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x11, 0)
    Sleep(500)

    ChrTalk(    #54
        0x11,
        "#203F*sigh* I've got a real bad feeling about this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10B,
        "#416F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x12,
        (
            "#190F#5PThe letter from Joshua was in an envelope from\x01",
            "the Empire...\x02\x03",

            "...and so was the receipt from this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x11,
        "#204FWhich means...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x12,
        (
            "#197F#5PI'm so sorry, Josette...\x02\x03",

            "I must've gone and attached the letter to the \x01",
            "parcel by mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10B,
        "#417F...!\x02",
    )

    CloseMessageWindow()

    def lambda_1E83():
        OP_9E(0xFE, 0x7, 0x0, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_1E83)
    Sleep(500)

    ChrTalk(    #60
        0x11,
        "#203FOhhh, boy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x12,
        (
            "#192F#5PA-Anyway, I'll get in touch with the client right\x01",
            "away!\x02\x03",

            "They should still have it, so if I let them know \x01",
            "it's ours, I should be able to get it back.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x10B, 0x2)
    Sleep(500)

    ChrTalk(    #62
        0x10B,
        "#418F#5SYou DUMMY!#2S\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x12C)
    CloseMessageWindow()

    ChrTalk(    #63
        0x11,
        "#205F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x12,
        "#192F#5P...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10B,
        (
            "#418FHow could you go and screw something this \x01",
            "important up?!\x02\x03",

            "HOW?!\x02\x03",

            "#417FDo you have any idea how happy I was when\x01",
            "I heard Joshua had sent us that letter?! And\x01",
            "then you...you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x11,
        "#207FJosette...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x12,
        (
            "#197F#5PI really am sorry...\x02\x03",

            "This one's completely on me. You've got every \x01",
            "right to be mad.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10B)
    Sleep(500)

    ChrTalk(    #68
        0x10B,
        (
            "#416FOh, it's ALWAYS on you.\x02\x03",

            "You've always been the sloppy one--the one who \x01",
            "makes stupid mistakes and screws everything up.\x02\x03",

            "#214FAnd it's always the rest of us who suffer for it!\x01",
            "You know that, don't you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x12,
        "#198F#5PY-Yeah, I do...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x11,
        (
            "#206FHold on a minute, Josette. We might still\x01",
            "be able to get that letter back, you know.\x02\x03",

            "There's no need to be that hard on him...\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    ChrTalk(    #71
        0x10B,
        "#214F#4SYOU stay out of this!#2S\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0xC8)
    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #72
        0x11,
        "#201F...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10B,
        (
            "#212FHell, we only became sky bandits in the first \x01",
            "place because of you screwing things up!\x02\x03",

            "#215FIf you hadn't gotten duped into signing that\x01",
            "contract, things would've been different!\x02\x03",

            "Do you have any idea how mu--\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    ChrTalk(    #74
        0x11,
        "#201F#4SJOSETTE!!#2S\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0xC8)
    CloseMessageWindow()
    OP_59()
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_240D():
        OP_8C(0xFE, 240, 500)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_240D)

    ChrTalk(    #75
        0x10B,
        "#216FAaah!\x02",
    )

    Sleep(1000)
    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x11, 1)
    Sleep(500)

    ChrTalk(    #76
        0x11,
        (
            "#204FI get that you're mad, but there's no need to\x01",
            "drag THAT up.\x02\x03",

            "Don regrets what happened enough as it is.\x02\x03",

            "#207FBesides...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x10B,
        "#213FBesides what?\x02",
    )

    CloseMessageWindow()
    OP_20(0xFA0)
    OP_8C(0x10B, 280, 400)
    Sleep(500)

    ChrTalk(    #78
        0x12,
        (
            "#198F#5P#40W...No, she's right. That was all my fault, just like\x01",
            "this is.\x02\x03",

            "If I'd been smarter instead of getting suckered in,\x01",
            "we would've never been driven from our home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10B,
        "#215F...Oh...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x11, 0)
    Sleep(500)

    ChrTalk(    #80
        0x11,
        (
            "#203F*sigh* Now look what you've done...\x02\x03",

            "Some things are best left undiscussed,\x01",
            "and that's definitely one of them.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x10B, 0x1, 0x0, 0x9)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()
    Sleep(500)
    OP_1D(0x53)
    OP_AD(0x240066, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetMessageWindowPos(250, 20, -1, -1)
    SetChrName("Don")

    AnonymousTalk(    #81
        (
            "\x07\x0C#40WIf it wasn't for me, we'd still be back in our \x01",
            "ancestral home living a life of luxury...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #82
        (
            "\x07\x0C#40WDrinking high-class tea, playing music, getting \x01",
            "called to fancy parties from time to time...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #83
        "\x07\x0C#40WBut nah. I had to go and ruin it all for us.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 250, -1, -1)
    SetChrName("Kyle")

    AnonymousTalk(    #84
        "\x07\x0CHey, now...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #85
        (
            "\x07\x0CWe've got no attachment to our old lives,\x01",
            "you know. It's all in the past.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 320, -1, -1)
    SetChrName("Josette")

    AnonymousTalk(    #86
        "\x07\x0C#40W...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    OP_AD(0x240067, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(120, 20, -1, -1)
    SetChrName("Don")

    AnonymousTalk(    #87
        (
            "\x07\x0C#40WI had to get greedy and fall for the obvious\x01",
            "trap right in front of me.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #88
        (
            "\x07\x0C#40WBecause of that, we lost everything we had\x01",
            "and ended up with nothing but a mountain of\x01",
            "debt in return.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #89
        (
            "\x07\x0C#40WI lost everything our ancestors had built up\x01",
            "just like that.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #90
        (
            "\x07\x0C#40WSo if there's a bigger idiot out there than me, \x01",
            "I've sure never met him.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 300, -1, -1)
    SetChrName("Kyle")

    AnonymousTalk(    #91
        "\x07\x0CIt's not like you deserve all the blame, Don.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #92
        (
            "\x07\x0CYou might've been partly responsible, but so\x01",
            "were we for being such naive kids.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    OP_43(0x10B, 0x1, 0x0, 0xA)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #93
        0x12,
        (
            "#198F#5P#40WThat's not the point, Kyle. It still comes down \x01",
            "to me at the end of the day.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x11, 1)
    Sleep(500)

    ChrTalk(    #94
        0x11,
        "#206FCome on! Back me up here, Josette.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x10B,
        "#215F#40W...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x11, 0)
    Sleep(500)

    ChrTalk(    #96
        0x11,
        "#203F*sigh*\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_20(0x0)
    PlayEffect(0x1, 0x0, 0xFF, -22600, 1700, 5520, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(300)
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(300)
    OP_1D(0x52)
    Sleep(500)
    OP_82(0x0, 0x0)

    ChrTalk(    #97
        0x11,
        "#201FWh-What's going on?!\x02",
    )

    CloseMessageWindow()

    def lambda_2BEB():
        OP_8C(0xFE, 240, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2BEB)
    Sleep(100)
    OP_8C(0x10B, 240, 500)
    Sleep(300)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -23300, 650, 4780, 0)

    ChrTalk(    #98
        0x19,
        "#5C#5PWe've got trouble, boss! ...Er, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x12,
        "#192F#0C#6PWhat is it?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x19,
        "#5C#5PWe've got one of those r-red ships on our tail!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x19,
        "#5C#5PThey were the society's, weren't they?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x10B,
        "#216F#0CNo way!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10B, 100, 600)

    def lambda_2CF6():
        OP_67(0, 4300, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2CF6)

    def lambda_2D0E():
        OP_6D(-23640, -300, 7960, 1000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_2D0E)

    def lambda_2D26():
        OP_6C(325000, 1000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_2D26)

    def lambda_2D36():
        OP_8E(0xFE, 0xFFFFB758, 0x0, 0x12C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_2D36)
    WaitChrThread(0x10B, 0x1)

    def lambda_2D56():
        OP_8E(0xFE, 0xFFFFB758, 0x0, 0xA50, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_2D56)
    WaitChrThread(0x10B, 0x1)

    def lambda_2D76():
        OP_8E(0xFE, 0xFFFFBBA4, 0x0, 0xA50, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_2D76)
    WaitChrThread(0x10B, 0x1)
    OP_8C(0x10B, 330, 600)

    def lambda_2D9D():
        OP_67(0, 5100, -10000, 500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2D9D)

    def lambda_2DB5():
        OP_6D(-23640, 0, 7960, 500)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_2DB5)

    def lambda_2DCD():
        OP_6C(330000, 500)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_2DCD)
    Fade(500)
    SetChrPos(0x10B, -18100, 3000, 4140, 330)
    OP_0D()
    OP_22(0xA4, 0x0, 0x64)

    def lambda_2DF9():
        OP_8E(0xFE, 0xFFFFB744, 0xBB8, 0x12C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_2DF9)
    WaitChrThread(0x10B, 0x1)
    OP_8C(0x10B, 270, 600)
    Sleep(300)

    ChrTalk(    #103
        0x12,
        "#197F#0C#5PBah... That's not good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x11,
        "#206F#0CDon!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x12,
        (
            "#198F#5PI got it. We can't afford to focus too much on 'em.\x02\x03",

            "#196FOur number one priority is protecting our cargo! \x01",
            "We need to focus on shaking them off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x11,
        "#201FYes, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x12,
        (
            "#196F#5PYou hear me, lads?! We've got ourselves an \x01",
            "emergency!\x02\x03",

            "Get ready for battle! You've all got jobs to do--\x01",
            "do 'em!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0610   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_A1B end

    def Function_9_2FAD(): pass

    label("Function_9_2FAD")

    OP_24(0x7A, 0x50)
    Sleep(100)
    OP_24(0x7A, 0x46)
    Sleep(100)
    OP_24(0x7A, 0x3C)
    Sleep(100)
    OP_24(0x7A, 0x32)
    Sleep(100)
    OP_24(0x7A, 0x28)
    Sleep(100)
    OP_24(0x7A, 0x1E)
    Sleep(100)
    OP_24(0x7A, 0x14)
    Sleep(100)
    OP_24(0x7A, 0xA)
    Sleep(100)
    OP_23(0x7A)
    Return()

    # Function_9_2FAD end

    def Function_10_2FF9(): pass

    label("Function_10_2FF9")

    OP_22(0x7A, 0x1, 0xA)
    Sleep(200)
    OP_24(0x7A, 0x14)
    Sleep(200)
    OP_24(0x7A, 0x1E)
    Sleep(200)
    OP_24(0x7A, 0x28)
    Sleep(200)
    OP_24(0x7A, 0x32)
    Sleep(200)
    OP_24(0x7A, 0x3C)
    Sleep(200)
    OP_24(0x7A, 0x46)
    Sleep(200)
    OP_24(0x7A, 0x50)
    Return()

    # Function_10_2FF9 end

    def Function_11_303E(): pass

    label("Function_11_303E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_6D(-23640, 0, 7960, 0)
    OP_67(0, 5100, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(330000, 0)
    OP_6E(280, 0)
    OP_22(0x7A, 0x1, 0x64)
    OP_76(0xB, 0x0, 0x1, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x1, 0x1, 0xFFFFFFFD, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x2, 0x1, 0xFFFFFFF8, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x10B, 0x40)
    SetChrPos(0x11, -24260, -1000, 4970, 270)
    SetChrPos(0x12, -21870, 650, 4940, 315)
    SetChrPos(0x10B, -18620, 3000, 4800, 270)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #108
        0x12,
        "#199FDid you see it, Josette?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x10B,
        "#212FY-Yeah. I saw it...but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x12,
        "#192FBut what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x10B,
        (
            "#214FIt's not alone... There're a bunch of weapons I've\x01",
            "never seen before with it, and they're coming this\x01",
            "way!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x12,
        (
            "#197FHeh. They really want a fight, huh?\x02\x03",

            "#199FFocus on firing at them from the rear to fight \x01",
            "them off, Josette!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x10B,
        "#212FGot it!\x02",
    )

    CloseMessageWindow()
    OP_22(0x9C, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #114
        0x12,
        (
            "#190FAll right! Machine gun mode enabled.\x02\x03",

            "Is everything in order?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x10B,
        (
            "#212FYep!\x02\x03",

            "I'll get right to work!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_6B(3500, 3000)
    OP_0D()
    OP_C0(0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_11_303E end

    def Function_12_3357(): pass

    label("Function_12_3357")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    OP_6D(-23640, 0, 7960, 0)
    OP_67(0, 5100, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(330000, 0)
    OP_6E(280, 0)
    OP_22(0x7A, 0x1, 0x5A)
    OP_76(0xB, 0x0, 0x1, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x1, 0x1, 0xFFFFFFFD, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x2, 0x1, 0xFFFFFFF8, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x10B, 0x40)
    SetChrPos(0x11, -24260, -1000, 4970, 270)
    SetChrPos(0x12, -21870, 650, 4940, 315)
    SetChrPos(0x10B, -18620, 3000, 4800, 270)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #116
        0x10B,
        "#212FWhew... Is that the last of them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x12,
        (
            "#190FI don't know... We can't let our guard down\x01",
            "just yet.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #118
        0x12,
        (
            "#192FJosette! Heat signal coming at 4 o'clock!\x02\x03",

            "Can you see what it is?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x10B,
        (
            "#213FI-I'll get right on it!\x02\x03",

            "What IS that? It looks like it's got a person in \x01",
            "it...\x02\x03",

            "#216FWh-Whatever it is, though, it's comin' this way!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_35D5():
        OP_6D(-38560, -2440, 14200, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_35D5)

    def lambda_35ED():
        OP_67(0, 3500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_35ED)

    def lambda_3605():
        OP_6C(304000, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_3605)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_3357 end

    def Function_13_362C(): pass

    label("Function_13_362C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_6D(-23640, 0, 7960, 0)
    OP_67(0, 5100, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(330000, 0)
    OP_6E(280, 0)
    OP_22(0x7A, 0x1, 0x5A)
    OP_76(0xB, 0x0, 0x1, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x1, 0x1, 0xFFFFFFFD, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x2, 0x1, 0xFFFFFFF8, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x10B, 0x40)
    SetChrPos(0x11, -24260, -1000, 4970, 270)
    SetChrPos(0x12, -21870, 650, 4940, 315)
    SetChrPos(0x10B, -18620, 3000, 4800, 270)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)

    def lambda_371E():

        label("loc_371E")

        OP_7C(0xF, 0xF, 0xBB8, 0x64)
        OP_48()
        Jump("loc_371E")

    QueueWorkItem2(0x11, 3, lambda_371E)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #120
        0x11,
        "#206F...Damn it. Can't shake him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x12,
        (
            "#197FUgh... He's small, but he's persistent!\x02\x03",

            "#196FWhatever you do, don't drop our speed, Kyle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x11,
        "#201FI know!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x12,
        (
            "#199FCan you try and make us an opening to escape, \x01",
            "Josette?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x10B,
        (
            "#212FI'll try.\x02\x03",

            "#214FNo. I'll DO it!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_C0(0x11, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_13_362C end

    def Function_14_388E(): pass

    label("Function_14_388E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-23640, 0, 7960, 0)
    OP_67(0, 5270, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(330000, 0)
    OP_6E(280, 0)
    OP_22(0x7A, 0x1, 0x50)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x10B, 0x40)
    SetChrPos(0x11, -24260, -1000, 4970, 270)
    SetChrPos(0x12, -21870, 650, 4940, 315)
    SetChrPos(0x10B, -18620, 3000, 4800, 270)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    OP_76(0xB, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x1, 0x1, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x2, 0x1, 0xFFFFFFFC, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #125
        0x10B,
        "#213FD-Did I get him?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x11,
        (
            "#204FI'll say!\x02\x03",

            "#200FBest of all, it looks like he fell into\x01",
            "Valleria Lake, so he'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x12,
        (
            "#490FThe society guys beat it, too.\x02\x03",

            "#191FDamn fine job you did, there, Josette!\x02\x03",

            "If not for you, we'd probably be the ones\x01",
            "swimmin' in the lake now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x11,
        "#202FYeah. You did great.\x02",
    )

    CloseMessageWindow()

    def lambda_3AD7():
        OP_8F(0xFE, 0xFFFFB8D4, 0xBB8, 0x12C0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_3AD7)
    WaitChrThread(0x10B, 0x1)
    Sleep(300)

    ChrTalk(    #129
        0x10B,
        (
            "#415FHeehee. Oh, there's no need to make that\x01",
            "big a deal out of it!\x02\x03",

            "You probably could've thrown them off\x01",
            "our tail even without my help if you'd had\x01",
            "a bit more time, Kyle.\x02\x03",

            "And besides, it was all possible because of\x01",
            "Don's leadership...\x02\x03",

            "#213F...Oh.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 100, 500)
    Sleep(300)

    ChrTalk(    #130
        0x12,
        (
            "#192FWh-What's wrong, Josette?!\x02\x03",

            "#198FOh, yeah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x11,
        (
            "#206FHuh?\x02\x03",

            "Are you two still stuck on that?\x02\x03",

            "#203F*sigh* There's really something to be said about\x01",
            "being honest with one another...\x02\x03",

            "#200FHop to it, Josette. If you've got somethin' you\x01",
            "want to say, spit it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x10B,
        (
            "#215FR-Right...\x02\x03",

            "...\x02\x03",

            "#413FI'm sorry, Don.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #133
        0x12,
        (
            "#192FB-But then...you'll forgive me?\x02\x03",

            "After how badly I messed up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x10B,
        (
            "#214FWh-Why else would I be saying sorry to you?\x02\x03",

            "#215FYou don't need to make me repeat myself!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #135
        0x12,
        "#192F#4SWaaaaaaaaah!\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x12C)
    CloseMessageWindow()

    ChrTalk(    #136
        0x10B,
        "#216FWh-What's up with YOU?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x12,
        (
            "#198FI really am the luckiest bastard alive!\x02\x03",

            "Who else can say they have a younger sister\x01",
            "as great as you? No one, that's who!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #138
        0x12,
        "#191F#4SWaaaaaaaaaaaah!\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x12C)
    CloseMessageWindow()

    ChrTalk(    #139
        0x10B,
        "#414FS-Stop that... Everyone can hear you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x12,
        "#198FS-Sorry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x10B,
        (
            "#413FOh, and sorry for all of that, too, Kyle...\x02\x03",

            "#415F...And thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x11,
        "#200FAww, forget it. That was all you.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x15, 0x80)
    OP_4A(0x15, 255)
    SetChrPos(0x15, -15500, 500, 4900, 270)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(    #143
        0x15,
        "Male Voice",
        "#1PIs Your Ladyship in here?\x02",
    )

    CloseMessageWindow()

    def lambda_4025():
        OP_67(0, 5480, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_4025)

    def lambda_403D():
        OP_6D(-21640, 0, 7960, 1500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_403D)

    def lambda_4055():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_4055)
    WaitChrThread(0x1A, 0x1)

    def lambda_4068():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_4068)

    def lambda_407A():
        OP_8E(0xFE, 0xFFFFBF28, 0xFA, 0x1324, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_407A)
    WaitChrThread(0x15, 0x1)
    Sleep(300)

    ChrTalk(    #144
        0x10B,
        "#213F#1PI am, but what is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x15,
        (
            "Well, when I was securing the cargo earlier\x01",
            "after we got attacked...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x15,
        (
            "...I found this envelope on the floor of the \x01",
            "storeroom. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x15,
        (
            "Was just wondering if you had any idea what\x01",
            "it could be.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #148
        0x10B,
        "#213F#1PWait...\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_41F3():
        OP_67(0, 4900, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_41F3)

    def lambda_420B():
        OP_8E(0xFE, 0xFFFFB9B0, 0xBB8, 0x10CC, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_420B)
    WaitChrThread(0x10B, 0x1)
    OP_22(0xA3, 0x0, 0x50)

    def lambda_4230():
        OP_96(0xFE, 0xFFFFBBA4, 0x0, 0xA50, 0xC8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_4230)
    WaitChrThread(0x10B, 0x1)
    OP_23(0xA3)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_425B():
        OP_8E(0xFE, 0xFFFFB758, 0x0, 0xA50, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_425B)
    WaitChrThread(0x10B, 0x1)

    def lambda_427B():
        OP_8E(0xFE, 0xFFFFB758, 0x0, 0x1388, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_427B)
    WaitChrThread(0x10B, 0x1)

    def lambda_429B():
        OP_8E(0xFE, 0xFFFFBAB4, 0x0, 0x1388, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_429B)
    WaitChrThread(0x10B, 0x1)
    Sleep(500)

    ChrTalk(    #149
        0x12,
        "#192F#5PCould it be...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x11,
        (
            "#200FLooks like our client didn't get a receipt \x01",
            "OR our letter this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x12,
        (
            "#198F#5P*sigh* Man, every time I think I can't get\x01",
            "any stupider...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x15,
        "A-Anyway, it's this thing here.\x02",
    )

    CloseMessageWindow()

    def lambda_4399():
        OP_8E(0xFE, 0xFFFFBBE0, 0x0, 0x1388, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_4399)
    WaitChrThread(0x10B, 0x1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #153
        "\x07\x05Rosco handed over the envelope.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    def lambda_4405():
        OP_8F(0xFE, 0xFFFFBAB4, 0x0, 0x1388, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_4405)
    WaitChrThread(0x10B, 0x1)
    Sleep(300)

    ChrTalk(    #154
        0x10B,
        "#415F#5PIt's from the Empire... This has to be it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x15,
        "Th-There a problem?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x10B,
        (
            "#210F#5PThere was, but it's all fine now.\x02\x03",

            "Thanks for giving this to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #157
        0x15,
        "Aww. Anything for you, Your Ladyship!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x15,
        "Well, I'll get back to work.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x15, 100, 500)

    def lambda_4534():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_4534)

    def lambda_4546():
        OP_8E(0xFE, 0xFFFFC374, 0x1F4, 0x1324, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4546)
    WaitChrThread(0x15, 0x1)

    ChrTalk(    #159
        0x11,
        (
            "#200FWhew... I'm relieved we found the letter.\x01",
            "Lucky us, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x12,
        "#490F#5PSo, what's written in it?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10B, 280, 500)
    Sleep(300)

    def lambda_45DC():
        OP_6D(-24400, 0, 7800, 2500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_45DC)

    def lambda_45F4():
        OP_67(0, 5250, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_45F4)

    def lambda_460C():
        OP_6B(2950, 2500)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_460C)

    def lambda_461C():
        OP_8E(0xFE, 0xFFFFAF88, 0x28A, 0x12D4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_461C)
    WaitChrThread(0x10B, 0x1)

    ChrTalk(    #161
        0x10B,
        (
            "#210FLet's see...\x02\x03",

            "#415F...Huh. Apparently, he's going to be leaving the \x01",
            "Empire soon.\x02\x03",

            "He says he's in the middle of looking for someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x11,
        (
            "#200FYeah? I wonder where he's going next.\x02\x03",

            "That it, though?\x02\x03",

            "I figured there'd be a personal message for you\x01",
            "in there or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x10B,
        (
            "#414FWell, there is, but it's not much.\x02\x03",

            "It just says not to forget to take it easy once\x01",
            "in a while and look after yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x11,
        (
            "#202FHaha. At least that shows he cares about you\x01",
            "in his own way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x10B,
        "#416FThere's one more thing under it, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x11,
        "#200FWhat's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x10B,
        (
            "#212FUgh... This bit's from Miss Staff-for-Brains.\x02\x03",

            "'There's no harm in acting tough, but it's all for\x01",
            "nothing if you go and get yourself hurt.'\x02\x03",

            "#214FHmph. SHE can just mind her own business!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x11,
        "#202FSounds like something she'd write, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x12,
        (
            "#191F#5PBwahaha! Sure is nice of them to take the time\x01",
            "to send us a letter, huh?\x02\x03",

            "#490FAnyway, I'd say break time's over for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x10B,
        (
            "#210FYeah... We're gonna need to get a move on if\x01",
            "we want to make our next delivery on time.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x11, 1)
    Sleep(500)

    ChrTalk(    #171
        0x11,
        "#200FShould I speed her up, then, Don?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 240, 500)
    Sleep(300)

    ChrTalk(    #172
        0x12,
        (
            "#490F#11PYeah. We're gonna need to make up for\x01",
            "lost time.\x02\x03",

            "Raise her up to 90% thrust, 2,000 SPH.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x11,
        "#202FYes, sir!\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x11, 0)
    Sleep(500)

    def lambda_4B1E():

        label("loc_4B1E")

        OP_7C(0xA, 0xA, 0xBB8, 0x64)
        OP_48()
        Jump("loc_4B1E")

    QueueWorkItem2(0x11, 3, lambda_4B1E)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2508)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_388E end

    def Function_15_4B50(): pass

    label("Function_15_4B50")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x109, -17690, 0, 2500, 0)
    SetChrPos(0x10F, -18960, 0, 2500, 0)
    SetChrPos(0xF0, -20380, 0, 2800, 0)
    SetChrPos(0xF1, -21710, 0, 2680, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(-20260, 500, 4890, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #174
        0x109,
        "#1079F#6PHey! That looks like another stone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x10F,
        (
            "#1446F#6PIt's hard to see from here, but it could\x01",
            "very well be.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 90, 400)
    Sleep(100)

    def lambda_4C8F():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_4C8F)
    Sleep(100)

    def lambda_4CA2():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_4CA2)
    Sleep(100)

    ChrTalk(    #176
        0x10F,
        "#1440F#5PShould I go up and get it?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #177
        0x109,
        (
            "#1060F#6PNah. I'll go, just to be sure.\x02\x03",

            "You guys wait down here for me.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x109, -18110, 3000, 4140, 0)
    SetChrPos(0x10F, -18430, 0, 2500, 0)
    SetChrPos(0xF0, -19850, 0, 3260, 0)
    SetChrPos(0xF1, -20580, 0, 2500, 0)
    OP_6D(-20900, 500, 6780, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x109, 7)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x1B, 0xFFFFB9B0, 0x1068, 0x1248, 0x12C, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    SetChrFlags(0x1B, 0x80)
    Sleep(500)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #178
        "Found \x1F\x55\x03\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x355, 1)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x109, -17690, 0, 2500, 270)
    SetChrPos(0x10F, -19310, 0, 2920, 90)
    SetChrPos(0xF0, -20350, 0, 2500, 90)
    SetChrPos(0xF1, -19620, 200, 4580, 135)
    OP_6D(-20210, 0, 4940, 0)
    OP_67(0, 4680, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(327000, 0)
    OP_6E(280, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F5B")

    ChrTalk(    #179
        0x10D,
        "#273F#5PSo this is what those sealing stones look like?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4FA3")

    label("loc_4F5B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FA3")

    ChrTalk(    #180
        0x10E,
        "#170F#5PSo it was another of those stones after all.\x02",
    )

    CloseMessageWindow()

    label("loc_4FA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FF7")

    ChrTalk(    #181
        0x107,
        (
            "#560F#5PI wonder if it being here means what I think\x01",
            "it does?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_504D")

    label("loc_4FF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_504D")

    ChrTalk(    #182
        0x10E,
        (
            "#176F#5PI wonder whether it being here means what\x01",
            "I think it does?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_504D")


    ChrTalk(    #183
        0x109,
        (
            "#1065F#4PWell, we'll soon find out. Let's get it back to\x01",
            "the base.\x02\x03",

            "#1060FHere's hoping that releasing whoever's inside\x01",
            "it'll make something happen in the city, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x10F,
        "#1448F#5PThat sounds wise.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x270E)
    OP_28(0x2C, 0x1, 0x20)
    OP_64(0x0, 0x1)
    OP_6D(-18640, 0, 2770, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, -18640, 0, 2770, 0)
    SetChrPos(0x1, -18640, 0, 2770, 0)
    SetChrPos(0x2, -18640, 0, 2770, 0)
    SetChrPos(0x3, -18640, 0, 2770, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_15_4B50 end

    def Function_16_51F1(): pass

    label("Function_16_51F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57F9")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5462")
    Fade(500)
    SetChrPos(0x109, -20320, 500, 4670, 270)
    SetChrPos(0x10F, -19460, 0, 3190, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5263")
    SetChrPos(0x107, -21700, 650, 4990, 270)
    SetChrPos(0xF1, -20650, 0, 2500, 315)
    Jump("loc_5293")

    label("loc_5263")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5293")
    SetChrPos(0x107, -21700, 650, 4990, 270)
    SetChrPos(0xF0, -20650, 0, 2500, 315)

    label("loc_5293")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(-21220, 650, 5380, 0)
    OP_67(0, 5140, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(338000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #185
        "\x07\x05Tita tried to turn the computer on.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #186
        "\x07\x05...But nothing happened.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #187
        0x107,
        (
            "#062F#5P...\x02\x03",

            "#561F...It's no use. It should work, but the orbal\x01",
            "engines just aren't responding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x109,
        "#1063F#6PJust like the Arseille, then. Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x10F,
        (
            "#1446F#6PI don't think we have much choice other\x01",
            "than to give up for now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5728")

    label("loc_5462")

    Fade(500)
    SetChrPos(0x109, -20320, 500, 4670, 270)
    SetChrPos(0x10F, -19460, 0, 3190, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54BC")
    SetChrPos(0x10D, -21700, 650, 4990, 270)
    SetChrPos(0xF1, -20650, 0, 2500, 315)
    Jump("loc_54EC")

    label("loc_54BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54EC")
    SetChrPos(0x10D, -21700, 650, 4990, 270)
    SetChrPos(0xF0, -20650, 0, 2500, 315)

    label("loc_54EC")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(-21220, 650, 5380, 0)
    OP_67(0, 5140, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(338000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #190
        "\x07\x05Mueller tried to turn the computer on.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #191
        "\x07\x05...But nothing happened.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #192
        0x10D,
        (
            "#272F#5PThe orbal engines don't seem to be responding.\x02\x03",

            "#270FAs far as I can tell from here, it looks as though\x01",
            "everything should work, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x10E,
        "#178F#6PI see... Just like the Arseille, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x109,
        "#1841F#6PWell, I can't say I expected any other result.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x10F,
        (
            "#1440F#6PI don't think we have much choice other\x01",
            "than to give up for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5728")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-21610, 650, 4890, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, -21610, 650, 4890, 90)
    SetChrPos(0x1, -21610, 650, 4890, 90)
    SetChrPos(0x2, -21610, 650, 4890, 90)
    SetChrPos(0x3, -21610, 650, 4890, 90)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x2710)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jump("loc_58A6")

    label("loc_57F9")

    TalkBegin(0xFF)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #196
        (
            "\x07\x05Nothing happened ever after trying to switch the\x01",
            "computer on.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #197
        "\x07\x05The orbal engines don't seem to be working.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_58A6")

    Return()

    # Function_16_51F1 end

    SaveToFile()

Try(main)
