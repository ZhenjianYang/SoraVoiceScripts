from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0120   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0120.x',
        MapIndex            = 4,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T0120   ._SN',
            'ED6_DT21/T0120_1 ._SN',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Freddy',                               # 9
        'Melders',                              # 10
        'Elger',                                # 11
        'Stella',                               # 12
        'Tico',                                 # 13
        'Morie',                                # 14
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
        'ED6_DT07/CH01040 ._CH',             # 00
        'ED6_DT07/CH01000 ._CH',             # 01
        'ED6_DT07/CH01680 ._CH',             # 02
        'ED6_DT07/CH01690 ._CH',             # 03
        'ED6_DT07/CH01050 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
        'ED6_DT07/CH01000P._CP',             # 01
        'ED6_DT07/CH01680P._CP',             # 02
        'ED6_DT07/CH01690P._CP',             # 03
        'ED6_DT07/CH01050P._CP',             # 04
    )

    DeclNpc(
        X                   = -38180,
        Z                   = 0,
        Y                   = -497,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -39499,
        Z                   = 0,
        Y                   = 678,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -36678,
        Z                   = 0,
        Y                   = 73751,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -86132,
        Z                   = 0,
        Y                   = 71210,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -45100,
        Z                   = 0,
        Y                   = 1430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -44360,
        Z                   = 0,
        Y                   = -390,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )


    DeclActor(
        TriggerX            = -38537,
        TriggerZ            = 0,
        TriggerY            = -1845,
        TriggerRange        = 400,
        ActorX              = -38180,
        ActorZ              = 1500,
        ActorY              = -497,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -41599,
        TriggerZ            = 0,
        TriggerY            = 299,
        TriggerRange        = 1000,
        ActorX              = -39499,
        ActorZ              = 1500,
        ActorY              = 678,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36170,
        TriggerZ            = 0,
        TriggerY            = 71651,
        TriggerRange        = 1000,
        ActorX              = -36678,
        ActorZ              = 1500,
        ActorY              = 73751,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1FE",          # 00, 0
        "Function_1_268",          # 01, 1
        "Function_2_28A",          # 02, 2
        "Function_3_2A2",          # 03, 3
        "Function_4_2A7",          # 04, 4
        "Function_5_2AC",          # 05, 5
        "Function_6_24DA",         # 06, 6
        "Function_7_349F",         # 07, 7
        "Function_8_5D88",         # 08, 8
        "Function_9_8351",         # 09, 9
        "Function_10_8436",        # 0A, 10
    )


    def Function_0_1FE(): pass

    label("Function_0_1FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_20D")
    SetChrFlags(0x9, 0x80)
    Jump("loc_241")

    label("loc_20D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_217")
    Jump("loc_241")

    label("loc_217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_22B")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_241")

    label("loc_22B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_23A")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_241")

    label("loc_23A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_241")

    label("loc_241")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_267")
    SetChrFlags(0x8, 0x80)
    OP_64(0x1, 0x1)
    SetChrPos(0x9, -38180, 0, -497, 180)

    label("loc_267")

    Return()

    # Function_0_1FE end

    def Function_1_268(): pass

    label("Function_1_268")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_279")
    OP_71(0x1, 0x4)

    label("loc_279")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_289")
    OP_64(0x1, 0x1)

    label("loc_289")

    Return()

    # Function_1_268 end

    def Function_2_28A(): pass

    label("Function_2_28A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29D")
    Call(0, 6)
    Jump("loc_2A1")

    label("loc_29D")

    Call(0, 5)

    label("loc_2A1")

    Return()

    # Function_2_28A end

    def Function_3_2A2(): pass

    label("Function_3_2A2")

    Call(0, 6)
    Return()

    # Function_3_2A2 end

    def Function_4_2A7(): pass

    label("Function_4_2A7")

    Call(0, 7)
    Return()

    # Function_4_2A7 end

    def Function_5_2AC(): pass

    label("Function_5_2AC")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_308")
    Call(6, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2EE")
    OP_A9(0x7)
    Jump("loc_2F0")

    label("loc_2EE")

    OP_A9(0x0)

    label("loc_2F0")

    TalkEnd(0x8)
    Return()

    label("loc_2F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_308")
    TalkEnd(0x8)
    Return()

    label("loc_308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1655")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_131B")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -38800, 0, -2650, 0)
    SetChrPos(0x102, -38000, 0, -2850, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_372")
    SetChrPos(0xF9, -38400, 0, -3850, 0)
    SetChrPos(0xF8, -37500, 0, -4050, 0)
    Jump("loc_394")

    label("loc_372")

    SetChrPos(0xF8, -38400, 0, -3850, 0)
    SetChrPos(0xF9, -37500, 0, -4050, 0)

    label("loc_394")

    OP_8C(0x8, 180, 0)
    OP_6D(-37570, 0, -1360, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(    #0
        0x8,
        "Ah, Estelle and Joshua...\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #1
        0x8,
        "...J-JOSHUA?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        "#1040F#4PHey, Freddy. It's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#1001F#6PI made extra sure to bring him out here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "No KIDDING it's been a while!\x01",
            "You been well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "Feels like a million years since\x01",
            "I've seen you two together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#1016F#6PHaha, well, kinda...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        "#1040F#4PYou don't seem to have changed much, Freddy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "I'm doing okay personally, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        "Unfortunately, the factory's in a real spot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "This is gonna sound weird as Gehenna I know,\x01",
            "but we can't offer any services...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_686")

    ChrTalk(    #11
        0x101,
        (
            "#1018F#6POh, right, of course.\x01",
            "Don't worry, though!\x02\x03",

            "I THINK we have a little something to\x01",
            "help with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        "Huh, what's that?\x02",
    )

    CloseMessageWindow()
    Jump("loc_C1F")

    label("loc_686")


    ChrTalk(    #13
        0x101,
        (
            "#1007F#6POhhh, right.\x02\x03",

            "The shop equipment isn't working, is it.\x02\x03",

            "#1015FWell, that's kind of a problem.\x02\x03",

            "If we can't manufacture quartz or\x01",
            "upgrade our slots, we're kinda\x01",
            "in trouble.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_790")

    ChrTalk(    #14
        0x103,
        (
            "#025FYes, at this rate we're just\x01",
            "wasting our generators.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87A")

    label("loc_790")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7DC")

    ChrTalk(    #15
        0x108,
        (
            "#072FAt this rate, we're just\x01",
            "wasting our generators.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87A")

    label("loc_7DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_87A")

    ChrTalk(    #16
        0x106,
        (
            "#552FKeep in mind we ARE kind of lucky to\x01",
            "even have arts right now.\x02\x03",

            "Does feel like a waste to just be sittin'\x01",
            "on all this sepith, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8ED")

    ChrTalk(    #17
        0x107,
        (
            "#064FAh, but, Estelle...\x02\x03",

            "If it's just for a little while,\x01",
            "we might be able to do something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_958")

    label("loc_8ED")


    ChrTalk(    #18
        0x102,
        (
            "#1043F#4PThat's true, but...\x02\x03",

            "#1040FHowever, we may be able to do\x01",
            "something for a short time, anyway.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_958")

    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9D5")

    def lambda_988():
        TurnDirection(0x0, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_988)
    Sleep(120)

    def lambda_99B():
        TurnDirection(0x1, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_99B)

    def lambda_9A9():
        TurnDirection(0x2, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_9A9)
    Sleep(120)

    def lambda_9BC():
        TurnDirection(0x3, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_9BC)

    def lambda_9CA():
        TurnDirection(0x8, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9CA)
    Jump("loc_9DC")

    label("loc_9D5")

    TurnDirection(0x101, 0x102, 400)

    label("loc_9DC")

    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)

    ChrTalk(    #19
        0x101,
        "#1004F#6PHuh...?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A43")

    ChrTalk(    #20
        0x106,
        "#052FCan you get the factory working?\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB8")

    label("loc_A43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A7F")

    ChrTalk(    #21
        0x103,
        "#023FCan you get the factory working?\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB8")

    label("loc_A7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB8")

    ChrTalk(    #22
        0x108,
        "#073FCan you get the factory working?\x02",
    )

    CloseMessageWindow()

    label("loc_AB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B01")

    ChrTalk(    #23
        0x107,
        (
            "#062FY-Yeah, probably.\x02\x03",

            "If we use the generator...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B73")

    label("loc_B01")


    ChrTalk(    #24
        0x102,
        (
            "#1040F#4PYes, most likely...\x02\x03",

            "If we use the generator, we can briefly\x01",
            "restore the equipment here, I suspect.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B73")


    ChrTalk(    #25
        0x101,
        "#1018F#6PRight, of course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        "Ummm, Joshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        "What are you talking about?\x02",
    )

    CloseMessageWindow()

    def lambda_BCF():
        TurnDirection(0x0, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_BCF)
    Sleep(120)

    def lambda_BE2():
        TurnDirection(0x1, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_BE2)

    def lambda_BF0():
        TurnDirection(0x2, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_BF0)
    Sleep(120)

    def lambda_C03():
        TurnDirection(0x3, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_C03)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)

    label("loc_C1F")


    ChrTalk(    #28
        0x102,
        "#1040F#4PLet me explain.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #29
        (
            "\x07\x05Joshua explained that by using the Zero Field Generator the\x01",
            "factory's functionality could be temporarily restored.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #30
        0x8,
        "Th-That's an incredible piece of equipment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "Yeah, I've got no objections.\x01",
            "Try it out immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        "#1006F#6PThanks, Freddy.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D8E")

    ChrTalk(    #33
        0x107,
        "#560FOkay, just a sec...\x02",
    )

    CloseMessageWindow()
    Jump("loc_DD3")

    label("loc_D8E")


    ChrTalk(    #34
        0x102,
        (
            "#1040F#4PWell, just let me borrow the\x01",
            "equipment for a moment...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_22(0x9D, 0x0, 0x64)
    OP_8C(0x8, 90, 0)
    SetChrName("")

    AnonymousTalk(    #35
        (
            "\x07\x05On activation, the Zero Field Generator restored\x01",
            "power to the factory's tools.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #36
        0x8,
        (
            "Whoa...\x01",
            "The machines are actually working again.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EF2")
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(    #37
        0x8,
        (
            "All right, let's finish what you\x01",
            "need done while it lasts.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Jump("loc_1059")

    label("loc_EF2")


    ChrTalk(    #38
        0x101,
        "#1000F#6POh, good... It worked.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F7F")

    ChrTalk(    #39
        0x107,
        (
            "#063FYeah, but it won't last long.\x02\x03",

            "#561FIt'll go back to how it was before soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FD8")

    label("loc_F7F")


    ChrTalk(    #40
        0x102,
        (
            "#1040F#4PYeah, it went well...\x02\x03",

            "But it's not fixed.\x01",
            "With time it should stop again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD8")

    TurnDirection(0x8, 0x0, 400)

    ChrTalk(    #41
        0x8,
        (
            "I see, that makes sense considering\x01",
            "the principles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "All right, let's finish what you\x01",
            "need done while it lasts.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    label("loc_1059")

    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x7)
    OP_56(0x0)
    OP_0D()
    Sleep(30)

    ChrTalk(    #43
        0x8,
        (
            "Whenever you want to use the factory\x01",
            "just bring the equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        "I'll gladly tune your stuff any time.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1176")

    ChrTalk(    #45
        0x103,
        (
            "#020FThe guild's doing the best it can to\x01",
            "determine what's happened.\x02\x03",

            "It may take a while, but please\x01",
            "be patient and hang in there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1207")

    label("loc_1176")


    ChrTalk(    #46
        0x102,
        (
            "#1040F#4PThe guild's doing the best it can to\x01",
            "determine what's happened.\x02\x03",

            "It may take some time, but please\x01",
            "hang in there and do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1207")


    ChrTalk(    #47
        0x8,
        "Yeah, I'll try and do my part.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "Well, then, everyone.\x01",
            "Good luck with your work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "In times like this, the only people we\x01",
            "can count on are the bracers, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#1006F#6PYeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x102,
        (
            "#1040F#4PWe'll do our best to live up to\x01",
            "your expectations.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    OP_A2(0x188A)
    OP_A2(0x209A)
    OP_A2(0x20E6)
    EventEnd(0x0)
    Jump("loc_1652")

    label("loc_131B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_158E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_139E")

    ChrTalk(    #52
        0x8,
        (
            "Whenever you want to use the factory\x01",
            "just bring the equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        "I'll gladly tune your stuff any time.\x02",
    )

    CloseMessageWindow()
    OP_A3(0x6)
    Jump("loc_158B")

    label("loc_139E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14DF")

    ChrTalk(    #54
        0x8,
        (
            "The old man's off checking up on\x01",
            "the clock at Paddington's request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "From the fact that he's not back yet, I'd guess\x01",
            "he's gazing up at that floating island again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "He's been really fascinated by it.\x01",
            "He's even done sketches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "Seriously, how can he be acting like a curious\x01",
            "child at his age?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_158B")

    label("loc_14DF")


    ChrTalk(    #58
        0x8,
        (
            "The old man's off checking up on\x01",
            "the clock at Paddington's request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "From the fact that he's not back yet, I'd guess\x01",
            "he's gazing up at that floating island again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_158B")

    Jump("loc_1652")

    label("loc_158E")


    ChrTalk(    #60
        0x8,
        (
            "Whenever you want to use the factory\x01",
            "just bring the equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        "I'll gladly tune your stuff any time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "Man, I wish they'd mass produce those\x01",
            "little generators at the central factory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1652")

    Jump("loc_24D6")

    label("loc_1655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_197B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34B, 1)), scpexpr(EXPR_END)), "loc_1705")

    ChrTalk(    #63
        0x8,
        (
            "I know a lot happened, but I'm\x01",
            "just glad the fog's cleared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        (
            "It's your first time back in Rolent in a while,\x01",
            "so try and enjoy yourselves a bit, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1978")

    label("loc_1705")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 0)
    Sleep(400)

    ChrTalk(    #65
        0x8,
        "Hey, you two. Great work out there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "I know a lot happened, but I'm\x01",
            "just glad the fog's cleared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "How about hanging around for a while\x01",
            "before you head to your next job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#1006FAh, yeah! That's the idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x103,
        (
            "#021FYes...\x02\x03",

            "#027FSo, how about you share a drink with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        "*cough* *cough*\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 400)

    ChrTalk(    #71
        0x8,
        (
            "I-I'm afraid I'll have to leave that\x01",
            "pleasure to Herbert or Faulkner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "I've still got work.\x01",
            "Lots and lots of work...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        "#1016FAhahaha...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #74
        0x8,
        (
            "A-Anyway, you should relax before\x01",
            "you head out again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        (
            "After all, it's your first time\x01",
            "back in Rolent for a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188A)
    OP_A2(0x1A59)

    label("loc_1978")

    Jump("loc_24D6")

    label("loc_197B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1D44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1A6C")

    ChrTalk(    #76
        0x8,
        (
            "The Royal Army arrived just a bit ago.\x01",
            "They've begun patrols here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        (
            "I didn't think they'd actually deploy\x01",
            "into a mess like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        (
            "I was just talking to the old man about it,\x01",
            "wondering if something had happened.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D41")

    label("loc_1A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 2)), scpexpr(EXPR_END)), "loc_1ABE")

    ChrTalk(    #79
        0x8,
        (
            "The Royal Army arrived just a bit ago.\x01",
            "They've begun patrols here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C09")

    label("loc_1ABE")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 0)
    Sleep(400)

    ChrTalk(    #80
        0x8,
        (
            "Estelle and Scherazard.\x01",
            "How's it going, you too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        "It's been a while. Finished your work?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        "#1025FAh... Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x103,
        (
            "#020FThere was some emergency work, you see.\x01",
            "We just got back.\x02\x03",

            "...Incidentally, it seems the army's already\x01",
            "patrolling the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        "Yeah, they just arrived a bit ago.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x188A)

    label("loc_1C09")


    ChrTalk(    #85
        0x8,
        (
            "The commander of the unit is Ashton.\x01",
            "It's great to have a local in charge,\x01",
            "and a relief to have them here, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        (
            "It's also kind of scary. I mean, things must\x01",
            "be pretty serious if the army had to mobilize,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        (
            "I was just talking to the old man about it,\x01",
            "wondering if something had happened.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1D41")

    Jump("loc_24D6")

    label("loc_1D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_1F99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1DAC")

    ChrTalk(    #88
        0x8,
        "The fog's nasty today too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        "Man, oh, man, when will the blue skies return...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F96")

    label("loc_1DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 2)), scpexpr(EXPR_END)), "loc_1DFE")

    ChrTalk(    #90
        0x8,
        (
            "Hey, good morning. Well, sorta good, anyway.\x01",
            "Fog's as bad as ever.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F0E")

    label("loc_1DFE")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 0)
    Sleep(400)

    ChrTalk(    #91
        0x8,
        "Estelle and Scherazard. How's it going?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "It's been a while.\x01",
            "Good to see you're well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#1006FYeah, you too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x103,
        "#020FYou look well, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x8,
        "Yeah, thanks. Work's been going great.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x8,
        "Still, though... Nasty fog today again.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x188A)

    label("loc_1F0E")


    ChrTalk(    #97
        0x8,
        (
            "It seems like in some places it might\x01",
            "even be worse than yesterday, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        "Man, oh, man, when will the blue skies return...?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1F96")

    Jump("loc_24D6")

    label("loc_1F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_24D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 2)), scpexpr(EXPR_END)), "loc_210F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2061")

    ChrTalk(    #99
        0x8,
        "Hey, welcome. Fog's still bad outside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "Apparently this is the first time even\x01",
            "the old man's seen fog this bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x8,
        (
            "If you go outside on work,\x01",
            "take care, all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_210C")

    label("loc_2061")


    ChrTalk(    #102
        0x8,
        (
            "If you need to tune your orbments,\x01",
            "say the word any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        (
            "I'll tune anything you've got to perfection\x01",
            "with the techniques I learned over at the\x01",
            "central factory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_210C")

    Jump("loc_24D6")

    label("loc_210F")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 0)
    Sleep(400)

    ChrTalk(    #104
        0x8,
        "Estelle and Scherazard. How's it going?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        (
            "It's been a while.\x01",
            "Good to see you're well.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 2)), scpexpr(EXPR_END)), "loc_222B")

    ChrTalk(    #106
        0x101,
        (
            "#1006FYou too, Freddy.\x02\x03",

            "Looks like you finished your\x01",
            "training over in Zeiss, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x103,
        (
            "#027FHaha. Looking forward to seeing\x01",
            "what you've learned.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_243B")

    label("loc_222B")


    ChrTalk(    #108
        0x101,
        "#1000FHey, Freddy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x103,
        "#027FYou look like you're doing pretty well.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 400)

    ChrTalk(    #110
        0x8,
        (
            "Yeah, I went off to Zeiss and studied\x01",
            "the new model orbments, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "It was a good chance to brush up on\x01",
            "my skills and learn something new.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#1004FWait, you were over in Zeiss too?!\x02\x03",

            "#1015FAw, it's too bad I didn't get the chance\x01",
            "to meet you.\x02\x03",

            "I went to the central factory loads of\x01",
            "times, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x103,
        (
            "#020FStill, it's great to hear our local orbal\x01",
            "expert has leveled-up, so to speak.\x02\x03",

            "How about you show us what you've learned?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_243B")


    ChrTalk(    #114
        0x8,
        "Yeah, of course. Just say the word.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x8,
        (
            "I'll tune anything you've got to perfection\x01",
            "with the techniques I learned over at the\x01",
            "central factory.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188A)
    OP_A2(0x5)

    label("loc_24D6")

    TalkEnd(0x8)
    Return()

    # Function_5_2AC end

    def Function_6_24DA(): pass

    label("Function_6_24DA")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_27F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34B, 0)), scpexpr(EXPR_END)), "loc_25A9")

    ChrTalk(    #116
        0x9,
        (
            "Hmph, you bracers are always so busy\x01",
            "I can hardly keep up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x9,
        (
            "Well, once your work settles down again,\x01",
            "come on back here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x9,
        (
            "Make sure you bring that Joshua with\x01",
            "you, all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27F3")

    label("loc_25A9")

    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x101, 0)
    Sleep(400)

    ChrTalk(    #119
        0x9,
        "Hey, you guys. Good work on everything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x9,
        (
            "You aren't already off onto your next job,\x01",
            "are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        (
            "#1015FWell, you could say that, but...\x02\x03",

            "#1006FFirst we plan to do a bit of work\x01",
            "around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x103,
        (
            "#020FYes...\x02\x03",

            "We need to take care of this branch at least\x01",
            "a little or I think Aina will get out of sorts,\x01",
            "and that is something I do NOT wish to face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x9,
        "Hmph, must be hard work all the time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x9,
        (
            "Well, once things are settled a bit,\x01",
            "come on back here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x9,
        (
            "Oh, yeah, and bring that Joshua with you,\x01",
            "you got that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        "#1006FUh... Sure! Will do!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A58)

    label("loc_27F3")

    Jump("loc_349B")

    label("loc_27F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_2A69")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_END)), "loc_2891")

    ChrTalk(    #127
        0x9,
        (
            "Still, it was quite the shock to have the\x01",
            "Royal Army show up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x9,
        (
            "It's just some fog. Why are they so\x01",
            "worked up about it? Sheesh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A66")

    label("loc_2891")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 1)), scpexpr(EXPR_END)), "loc_28C6")

    ChrTalk(    #129
        0xFE,
        "Hey, you guys. You seem awfully busy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_29B8")

    label("loc_28C6")

    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x101, 0)
    Sleep(400)

    ChrTalk(    #130
        0x9,
        "Hey there, Estelle, Scherazard!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x9,
        (
            "Seems like you're pretty busy\x01",
            "with the fog and all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        "#1003FYeah... There's been some stuff.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x103, 400)

    ChrTalk(    #133
        0x103,
        "#020FNothing new over here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x9,
        "Nope, no problems at all.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1889)

    label("loc_29B8")


    ChrTalk(    #135
        0x9,
        (
            "Still, it was quite the shock to have the\x01",
            "Royal Army show up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x9,
        (
            "I mean, yeah it's pretty thick, but it's just\x01",
            "fog. Seems like they're going a bit overboard,\x01",
            "yeah?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2A66")

    Jump("loc_349B")

    label("loc_2A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2DA7")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_END)), "loc_2AED")

    ChrTalk(    #137
        0x9,
        "The fog outside's as bad as ever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x9,
        (
            "I've lived here a long time, but I've\x01",
            "never seen anything like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DA4")

    label("loc_2AED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 1)), scpexpr(EXPR_END)), "loc_2B80")

    ChrTalk(    #139
        0x9,
        (
            "Oh, hey, you all.\x01",
            "Fog's still pretty nasty out there huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x9,
        (
            "I've lived here a long time, but I've\x01",
            "never seen anything like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D1B")

    label("loc_2B80")

    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x101, 0)
    Sleep(400)

    ChrTalk(    #141
        0x9,
        "Hey there, Estelle, Scherazard!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x9,
        "It's about time you turned up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        (
            "#1008FAhaha... Sorry, sir. We meant to come\x01",
            "and say hello sooner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x103,
        "#020FI see you're the same as always.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x103, 400)

    ChrTalk(    #145
        0x9,
        (
            "Yeah, of course. I'm not gonna\x01",
            "lose to you youngsters yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x9,
        "Still, the fog's still really bad today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x9,
        (
            "I've lived here a long time, but I've\x01",
            "never seen anything like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1889)

    label("loc_2D1B")


    ChrTalk(    #148
        0x9,
        "You all be careful when you go outside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x9,
        (
            "At this rate, even if you went onto the roads,\x01",
            "you wouldn't be able to see a thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2DA4")

    Jump("loc_349B")

    label("loc_2DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_315D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 1)), scpexpr(EXPR_END)), "loc_2F2B")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB0")

    ChrTalk(    #150
        0x9,
        (
            "Hey, good work. Must be hard doin'\x01",
            "your job in this fog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x9,
        (
            "If you need work done on your new\x01",
            "orbments, ask Freddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x9,
        (
            "After all, he went all the way to Zeiss to\x01",
            "train for those things. Might as well use\x01",
            "'im for what he's worth.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F28")

    label("loc_2EB0")


    ChrTalk(    #153
        0x9,
        (
            "Freddy's back from his training in Zeiss,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x9,
        (
            "Ask him to tune any of those new model\x01",
            "orbments you got.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F28")

    Jump("loc_315A")

    label("loc_2F2B")

    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x101, 0)
    Sleep(400)

    ChrTalk(    #155
        0x9,
        (
            "Oh, Estelle! And you've got Scherazard\x01",
            "with you, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x9,
        "It's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        "#1017FAhaha... You seem well, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x103,
        "#020FSame as always.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x103, 400)

    ChrTalk(    #159
        0x9,
        (
            "Yeah, of course. I'm not gonna\x01",
            "lose to you youngsters yet.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 6)), scpexpr(EXPR_END)), "loc_30AA")

    ChrTalk(    #160
        0x9,
        (
            "Freddy's back from his training\x01",
            "in Zeiss, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x9,
        (
            "If you got any new model orbments to tune,\x01",
            "leave it to him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3154")

    label("loc_30AA")


    ChrTalk(    #162
        0x9,
        (
            "Freddy's finally back from his trip to Zeiss\x01",
            "where he trained to handle those new\x01",
            "model orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x9,
        (
            "If you need to tune them or open slots,\x01",
            "go ahead and ask him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3154")

    OP_A2(0x1889)
    OP_A2(0x4)

    label("loc_315A")

    Jump("loc_349B")

    label("loc_315D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_349B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 6)), scpexpr(EXPR_END)), "loc_3214")

    ChrTalk(    #164
        0x9,
        "Freddy's off in Zeiss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x9,
        (
            "I dunno the details, but apparently there's some\x01",
            "kinda training program at the central factory\x01",
            "on those new model tactical orbments.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_349B")

    label("loc_3214")


    ChrTalk(    #166
        0x9,
        "Oh, welco--\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x9, 0x101, 400)
    Sleep(600)
    OP_63(0x9)

    ChrTalk(    #167
        0x9,
        (
            "Why, hello, Estelle! I've missed\x01",
            "you brightening up my shop.\x01",
            "It's been a while, ain't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        "#000FAhaha. You look well, Mr. Melders.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x9,
        (
            "Heh, 'course I'm well. I'm not about\x01",
            "to lose to you kids just yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x9,
        (
            "Ah, but if you're looking for Freddy,\x01",
            "he's off in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        "#505FZeiss? What's he doing there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x9,
        (
            "The central factory is giving some\x01",
            "kind of training session on tactical\x01",
            "orbments, of all things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        "#501FTactical orbments? Huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x9,
        (
            "But, boy, I've been ten kinds of\x01",
            "busy lately!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x9,
        (
            "I don't care if the boy's learning to perform\x01",
            "miracles. He needs to get back here!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x102E)

    label("loc_349B")

    TalkEnd(0x9)
    Return()

    # Function_6_24DA end

    def Function_7_349F(): pass

    label("Function_7_349F")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 7)), scpexpr(EXPR_END)), "loc_352E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_34E5")

    ChrTalk(    #176
        0xA,
        "Estelle, give my best to Joshua.\x02",
    )

    CloseMessageWindow()
    Jump("loc_352B")

    label("loc_34E5")


    ChrTalk(    #177
        0xA,
        "Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        "#501FHm? What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xA,
        "No... it's nothing.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_352B")

    Jump("loc_37E0")

    label("loc_352E")


    ChrTalk(    #180
        0xA,
        "Estelle...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xA,
        "Estelle! It IS you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        "#001FHi, Elger. I've missed you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xA,
        (
            "YOU, young lady, have been all over the\x01",
            "damned news. Heard you're a\x01",
            "full bracer now, among other things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xA,
        (
            "Really. You Brights just surprise me\x01",
            "again and again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xA,
        "I heard that old dog Cassius is well, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xA,
        "Though... Wait a moment. Where's Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        (
            "#000FAh, he came home a bit ahead of us.\x01",
            "I was just on my way back home myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xA,
        "Did he, now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xA,
        (
            "He came back and didn't even drop by\x01",
            "to say hello? Well, that's just heartless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        (
            "#505FJoshua didn't stop by to say hi?\x02\x03",

            "#000FThat silly... Don't worry. I'll tell him\x01",
            "to come visit when I see him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xA,
        "Yes, please do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x142,
        "#1067F...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x102F)

    label("loc_37E0")

    TalkEnd(0xA)
    Return()

    label("loc_37E4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_383D")
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_382C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3823")
    OP_A9(0x8)
    Jump("loc_3825")

    label("loc_3823")

    OP_A9(0x1)

    label("loc_3825")

    TalkEnd(0xA)
    Return()

    label("loc_382C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_383D")
    TalkEnd(0xA)
    Return()

    label("loc_383D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3E6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A52")
    TurnDirection(0xA, 0x102, 400)
    Sleep(1000)

    ChrTalk(    #193
        0xA,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xA,
        "Oh, Joshua. Finally back, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x102,
        "#1035FHey, Elger. Glad to be back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xA,
        "Yes... You look a lot more mature.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xA,
        (
            "Seems like you've had some worthwhile\x01",
            "experiences.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x102,
        (
            "#1040FYes, a number...\x02\x03",

            "#1043FStill, I know I made everyone worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xA,
        "Haha, you're a man. That's part of the job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xA,
        (
            "Joshua, you're the pride of this town;\x01",
            "our favorite son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xA,
        "Welcome back... Stay a while, and listen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x102,
        (
            "#1040FThank you...\x02\x03",

            "Once I've completed some work,\x01",
            "I'll be glad to do just that.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_A2(0x209C)
    Jump("loc_3E69")

    label("loc_3A52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3ADE")

    ChrTalk(    #203
        0xA,
        "Did you already see Stella?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xA,
        "If not, you should go pay her a visit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xA,
        (
            "She was worried about you even more\x01",
            "than I was.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E69")

    label("loc_3ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_3CD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C21")

    ChrTalk(    #206
        0xA,
        "Oh, Estelle and Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xA,
        (
            "I knew the scheduled airships were off service,\x01",
            "but even the cargo carriers aren't working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xA,
        (
            "Which means all routes of transport\x01",
            "are completely closed off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xA,
        (
            "Rolent's got fields near, so we're okay,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xA,
        (
            "What'll happen to Bose and the capital,\x01",
            "I wonder?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_3CD6")

    label("loc_3C21")


    ChrTalk(    #211
        0xA,
        (
            "These events have totally locked\x01",
            "down all routes of transport.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xA,
        (
            "Rolent's got fields near, so we're okay,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xA,
        (
            "Bose and the capital might be in some\x01",
            "serious trouble.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CD6")

    Jump("loc_3E69")

    label("loc_3CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DD2")

    ChrTalk(    #214
        0xA,
        "Oh, it's Estelle and the others.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xA,
        "Still, what bad timing to come home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xA,
        (
            "Right now orbal instruments all across\x01",
            "town have stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xA,
        (
            "There've been no serious issues yet, but I'll\x01",
            "admit we have had our share of problems.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_3E69")

    label("loc_3DD2")


    ChrTalk(    #218
        0xA,
        (
            "Right now orbal devices across the entire\x01",
            "town aren't working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xA,
        (
            "We asked the factory staff what could've\x01",
            "caused it, but even they don't know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E69")

    Jump("loc_5D84")

    label("loc_3E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_4449")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34B, 2)), scpexpr(EXPR_END)), "loc_40E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4038")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3F23")

    ChrTalk(    #220
        0xA,
        (
            "I'll have to ask you about this case\x01",
            "another time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xA,
        (
            "When that happens, make sure to bring Joshua.\x01",
            "I want to hear everything from both of you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4035")

    label("loc_3F23")


    ChrTalk(    #222
        0xA,
        (
            "Sounds like you contributed a lot to\x01",
            "solving this case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xA,
        (
            "I have to admit, I'm terribly curious\x01",
            "about how you did it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xA,
        "I'll have to ask you about that another time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xA,
        (
            "Well, when that happens, bring Joshua\x01",
            "along too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xA,
        "I need to talk to him, man to man.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4035")

    Jump("loc_40E1")

    label("loc_4038")


    ChrTalk(    #227
        0xA,
        (
            "I'll want to ask you about this case's\x01",
            "details another time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xA,
        (
            "Next time you come be sure to\x01",
            "bring Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xA,
        (
            "There's a lot we need to talk about,\x01",
            "man to man.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40E1")

    Jump("loc_4446")

    label("loc_40E4")

    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x101, 0)
    Sleep(400)

    ChrTalk(    #230
        0xA,
        (
            "Hey, Estelle and Scherazard.\x01",
            "Lovely weather we're having, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xA,
        (
            "Sounds like all the people who\x01",
            "were asleep woke up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xA,
        "...I'm guessing this is your doing, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x101,
        (
            "#1016FW-Well, it's kind of weird, but...\x02\x03",

            "#1015FI guess, yeah, technically it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xA,
        "I knew you all would solve it for us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xA,
        (
            "I'd love to hear all the details on\x01",
            "exactly HOW you did it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xA,
        (
            "...But knowing you guys, I'm guessing\x01",
            "you've got more work lined up that you\x01",
            "need to go and get on with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xA,
        (
            "So I'd better let you go. I look forward\x01",
            "to hearing all the exciting details another\x01",
            "day, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x101,
        (
            "#1008FA-Ahahaha...\x02\x03",

            "#1007F(I-It's like he can read our minds...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x103,
        (
            "#020FHeehee. We appreciate it.\x02\x03",

            "Well, if you'll pardon us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xA,
        "Yeah, and bring Joshua with you then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xA,
        (
            "I've been praying to Aidios that you\x01",
            "can track him down.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188C)
    OP_A2(0x1A5A)
    OP_A2(0x1)

    label("loc_4446")

    Jump("loc_5D84")

    label("loc_4449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_4BBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 5)), scpexpr(EXPR_END)), "loc_4754")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4541")

    ChrTalk(    #242
        0xA,
        (
            "Looks like some army troops are\x01",
            "here to patrol the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xA,
        "Now you bracers can focus on investigating.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xA,
        (
            "I'm sure it'll be tough, but we're expecting\x01",
            "a lot from you. Bring us back some good news,\x01",
            "ya hear?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46D8")

    label("loc_4541")

    TurnDirection(0xA, 0x101, 0)

    ChrTalk(    #245
        0xA,
        "Hey, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xA,
        (
            "A Royal Army soldier just stopped by\x01",
            "to greet us. Nice chap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xA,
        (
            "Apparently, the army'll be watching over\x01",
            "the city from today on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xA,
        (
            "Normally they're hard to approach since\x01",
            "they're kind of imposing, if you know what\x01",
            "I mean, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xA,
        (
            "I admit it's a relief to have army folks\x01",
            "around at a time like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xA,
        (
            "Hmph, humans really are all about that\x01",
            "self-interest, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_46D8")

    Jump("loc_4751")

    label("loc_46DB")


    ChrTalk(    #251
        0xA,
        "Good luck with the investigation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xA,
        "But don't overdo it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xA,
        "If you bracers collapse, we won't get anywhere.\x02",
    )

    CloseMessageWindow()

    label("loc_4751")

    Jump("loc_4BB7")

    label("loc_4754")

    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x101, 0)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_485B")

    ChrTalk(    #254
        0xA,
        "Oh, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xA,
        (
            "Haha, I've been ready since yesterday,\x01",
            "waiting for you lot to turn up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x101,
        "#1016FAh, sorry to keep you waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xA,
        (
            "Busy as always, huh? Sorry to put you right\x01",
            "to work the second you get back.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188C)
    Jump("loc_488B")

    label("loc_485B")


    ChrTalk(    #258
        0xA,
        "Hey, everyone. At it bright and early, eh?\x02",
    )

    CloseMessageWindow()

    label("loc_488B")


    ChrTalk(    #259
        0xA,
        (
            "Luke and the others' conditions seem\x01",
            "stable for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xA,
        (
            "I hope they wake up soon, but us fretting\x01",
            "won't make that happen faster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xA,
        (
            "You all'd better not overdo it yourselves,\x01",
            "you got that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xA,
        "If you collapse, we won't get anywhere.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x103,
        (
            "#020FWe'll be fine, don't worry.\x02\x03",

            "Even Estelle's an experienced,\x01",
            "full bracer now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x101,
        (
            "#1008FAhaha, well...\x02\x03",

            "#1015FI've still got a long way to go\x01",
            "compared to Schera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xA,
        (
            "Haha, if you've still got the energy\x01",
            "to compliment your superior, then\x01",
            "you should be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xA,
        (
            "Well, then, good luck with the investigation.\x01",
            "We're expecting good news.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B09")

    ChrTalk(    #267
        0x106,
        "#050FYeah, leave it to us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BB1")

    label("loc_4B09")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B3D")

    ChrTalk(    #268
        0x108,
        "#070FYeah, we'll do our best.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BB1")

    label("loc_4B3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B92")

    ChrTalk(    #269
        0x104,
        (
            "#030FHeh, you may certainly expect great things\x01",
            "from my deeds.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BB1")

    label("loc_4B92")


    ChrTalk(    #270
        0x103,
        "#525FYes, leave it to us.\x02",
    )

    CloseMessageWindow()

    label("loc_4BB1")

    OP_A2(0x188D)
    OP_A2(0x1)

    label("loc_4BB7")

    Jump("loc_5D84")

    label("loc_4BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_539A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 5)), scpexpr(EXPR_END)), "loc_4DE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4C69")

    ChrTalk(    #271
        0xA,
        (
            "I knew this fog wasn't your run of the mill bad\x01",
            "weather, but for something like this to happen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xA,
        "You all better take good care too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D5D")

    label("loc_4C69")

    TurnDirection(0xA, 0x101, 0)

    ChrTalk(    #273
        0xA,
        "Oh, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xA,
        (
            "I thought this fog seemed unnatural, but to\x01",
            "have cases of people losing consciousness...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xA,
        (
            "Well, we don't know if it's a 'case' or just\x01",
            "an accident, now do we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xA,
        "The truth is shrouded in mist. Literally.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4D5D")

    Jump("loc_4DE0")

    label("loc_4D60")


    ChrTalk(    #277
        0xA,
        "Good luck with the investigation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xA,
        "But don't overdo it, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xA,
        "If you bracers collapse, we won't get anywhere.\x02",
    )

    CloseMessageWindow()

    label("loc_4DE0")

    Jump("loc_5397")

    label("loc_4DE3")


    ChrTalk(    #280
        0x101,
        "#1011FGood morning, Elger.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E29")

    ChrTalk(    #281
        0x105,
        "#040FGood morning.\x02",
    )

    CloseMessageWindow()

    label("loc_4E29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E55")

    ChrTalk(    #282
        0x107,
        "#060FUm... Good morning.\x02",
    )

    CloseMessageWindow()

    label("loc_4E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F5C")
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x101, 400)
    Sleep(400)

    ChrTalk(    #283
        0xA,
        "Oh, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xA,
        (
            "Haha, I've been ready since yesterday,\x01",
            "waiting for you lot to turn up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x101,
        "#1008FAh, sorry to keep you waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xA,
        (
            "Busy as always, huh? Sorry to put you right\x01",
            "to work the second you get back.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188C)
    Jump("loc_4F98")

    label("loc_4F5C")

    TurnDirection(0xA, 0x101, 0)

    ChrTalk(    #287
        0xA,
        "Hey, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xA,
        "At it bright and early, eh?\x02",
    )

    CloseMessageWindow()

    label("loc_4F98")


    ChrTalk(    #289
        0x103,
        (
            "#025FYeah, seriously...\x01",
            "I wish I was still in bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x101,
        (
            "#1015F(W-Well given how late you stayed up,\x01",
            "it's no surprise...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x103, 400)

    ChrTalk(    #291
        0xA,
        (
            "Welp, time to show off how tough a\x01",
            "bracer can be to your subordinates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xA,
        (
            "Luke and the others' conditions\x01",
            "seem stable for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xA,
        (
            "I hope they wake up soon, but us fretting\x01",
            "won't make that happen faster.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #294
        0xA,
        (
            "You all better not overdo it yourselves,\x01",
            "ya hear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xA,
        "If you collapse, we won't get anywhere.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x103,
        (
            "#020FWe'll be fine, don't worry.\x02\x03",

            "Even Estelle's an experienced,\x01",
            "full bracer now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x101,
        (
            "#1008FAhaha, well...\x02\x03",

            "#1015FI've still got a long way to go to compare\x01",
            "to Schera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xA,
        (
            "Haha, if you've still got the energy to\x01",
            "compliment your superior, then you should\x01",
            "be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xA,
        (
            "Well, then, good luck with the investigation.\x01",
            "We're expecting good news.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52E9")

    ChrTalk(    #300
        0x106,
        "#050FYeah, leave it to us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5391")

    label("loc_52E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_531D")

    ChrTalk(    #301
        0x108,
        "#070FYeah, we'll do our best.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5391")

    label("loc_531D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5372")

    ChrTalk(    #302
        0x104,
        (
            "#030FHeh, you may certainly expect great things\x01",
            "from my deeds.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5391")

    label("loc_5372")


    ChrTalk(    #303
        0x103,
        "#525FYes, leave it to us.\x02",
    )

    CloseMessageWindow()

    label("loc_5391")

    OP_A2(0x188D)
    OP_A2(0x1)

    label("loc_5397")

    Jump("loc_5D84")

    label("loc_539A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_5D7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 4)), scpexpr(EXPR_END)), "loc_553B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5484")

    ChrTalk(    #304
        0xA,
        "Still, though, I've never seen fog this bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xA,
        (
            "To stop even the scheduled airship flights...\x01",
            "This weather sure wants to stir up trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xA,
        (
            "Well, it'll clear up soon.\x01",
            "There's nothing to worry about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5538")

    label("loc_5484")

    TurnDirection(0xA, 0x101, 0)

    ChrTalk(    #307
        0xA,
        (
            "Don't hold it in. If you need to talk,\x01",
            "come any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xA,
        (
            "Even if you just need equipment or something,\x01",
            "I'll have lots of high quality gear ready and\x01",
            "waiting for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5538")

    Jump("loc_5D7A")

    label("loc_553B")

    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x101, 0)
    Sleep(400)

    ChrTalk(    #309
        0xA,
        "Oh, if it isn't Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xA,
        (
            "It's been a while. Ever since you\x01",
            "went off on that training trip, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x101,
        "#1000FHi, Elger. Long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xA,
        "Welcome back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0xA,
        (
            "So if Scherazard's with you, does\x01",
            "that mean you're in the middle of some\x01",
            "work for the guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x103,
        "#020FYeah, a bit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xA,
        (
            "I heard from Aina that the two of you are\x01",
            "working pretty hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xA,
        (
            "Especially you, Estelle. Word is you've been\x01",
            "solving lots of cases and you're even a full\x01",
            "bracer now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xA,
        (
            "Hmph, quite a bit of success for such\x01",
            "a short time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xA,
        (
            "Ahhh, I can't help but be nostalgic for the\x01",
            "days you were complaining about training\x01",
            "because you hated paper tests, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #319
        0x101,
        "#1008FH-Hey, Elger, ixnay on the eststay...\x02",
    )

    CloseMessageWindow()

    def lambda_5830():
        TurnDirection(0x0, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5830)

    def lambda_583E():
        TurnDirection(0x1, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_583E)

    def lambda_584C():
        TurnDirection(0x2, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_584C)
    TurnDirection(0x3, 0x101, 400)
    Sleep(400)

    ChrTalk(    #320
        0x103,
        (
            "#021FNow, now, what is there to hide?\x02\x03",

            "Certainly your paper tests were appalling\x01",
            "like no other bracer before, but you've\x01",
            "always been top in the practicals.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5947")

    ChrTalk(    #321
        0x106,
        (
            "#051FHaha, thought so.\x02\x03",

            "That's so freakin' you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A28")

    label("loc_5947")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_597A")

    ChrTalk(    #322
        0x107,
        (
            "#560FAhaha...\x02\x03",

            "Ohh, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A28")

    label("loc_597A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59BC")

    ChrTalk(    #323
        0x104,
        "#031FHeh, what a very Estelle-like episode.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A28")

    label("loc_59BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A28")

    ChrTalk(    #324
        0x108,
        (
            "#070FHaha. Now, don't be embarrassed.\x02\x03",

            "A couple of flaws are a part of a\x01",
            "person's charm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A4A")

    ChrTalk(    #325
        0x105,
        "#041FHeehee...\x02",
    )

    CloseMessageWindow()

    label("loc_5A4A")


    ChrTalk(    #326
        0xA,
        "Ah, sorry, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0xA,
        (
            "I suppose yammering on about the past\x01",
            "like this is proof I'm getting old.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0xA,
        "Anyway, putting that aside...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xA,
        (
            "Did you find out anything about\x01",
            "Joshua's whereabouts?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5B14():
        TurnDirection(0x0, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5B14)

    def lambda_5B22():
        TurnDirection(0x1, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5B22)

    def lambda_5B30():
        TurnDirection(0x2, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_5B30)
    TurnDirection(0x3, 0xA, 400)
    Sleep(400)

    ChrTalk(    #330
        0x101,
        (
            "#1003FAh...\x02\x03",

            "#1007FI've looked a lot, but I still haven't\x01",
            "really found anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xA,
        (
            "I see... I guess he won't\x01",
            "be that easy to find.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xA,
        (
            "I admit I was worried when\x01",
            "I heard from Cassius, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xA,
        (
            "From the looks of it, Estelle,\x01",
            "you seem to be hanging in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xA,
        "But, if it gets hard, come on by any time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xA,
        (
            "If you're okay with it, Stella and\x01",
            "I would be glad to hear you out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x101,
        (
            "#1025FElger...\x02\x03",

            "#1000F... Yeah. Thanks. I'll definitely\x01",
            "take you up on that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xA,
        "Stop by any time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0xA,
        (
            "I'll have lots of good equipment\x01",
            "ready and waiting for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188C)
    OP_A2(0x0)

    label("loc_5D7A")

    Jump("loc_5D84")

    label("loc_5D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_5D84")

    label("loc_5D84")

    TalkEnd(0xA)
    Return()

    # Function_7_349F end

    def Function_8_5D88(): pass

    label("Function_8_5D88")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_653D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60B9")
    TurnDirection(0xB, 0x101, 0)

    ChrTalk(    #339
        0xFE,
        "Oh, Estelle. Welcome. Thanks for com...\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xB, 0x102, 400)

    ChrTalk(    #340
        0xFE,
        "...Oh? Oh, my!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0xFE,
        "Is that you...Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x102,
        "#1040FIt's been a while, Miss Stella.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0xFE,
        (
            "It... it isn't a dream...\x01",
            "It really is little Joshua!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xFE,
        "Oh, where have you been?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x102,
        "#1043FI'm sorry...to have worried you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xFE,
        "Oh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0xFE,
        "I shouldn't be blaming you, should I?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xFE,
        (
            "I'm sure this must have been\x01",
            "hardest on you above all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x101,
        "#1025FStella...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0xFE,
        "Joshua... Raise your head.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xFE,
        "We're just happy you've come back to Rolent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xFE,
        "So don't make such a face, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0xFE,
        (
            "A grim look like that is just too sad\x01",
            "when we haven't met in so long, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x102,
        "#1040FHaha... you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0xFE,
        "Yes, yes. Young people need smiles.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0xFE,
        (
            "You can overcome anything life\x01",
            "throws at you with that smile!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A2(0x209D)
    Jump("loc_653A")

    label("loc_60B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_6398")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_61C7")

    ChrTalk(    #357
        0xFE,
        (
            "And this old lady will make sure to work just as\x01",
            "hard in the house as you do out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0xFE,
        (
            "After all, I have to do all the cleaning\x01",
            "and laundry by hand now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0xFE,
        (
            "If I just went about it like I normally do,\x01",
            "the sun would be down before I knew it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6395")

    label("loc_61C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62E8")

    ChrTalk(    #360
        0xFE,
        "Oh, everyone. How's work?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0xFE,
        (
            "This old lady's going to do her part and work\x01",
            "hard to overcome these household struggles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0xFE,
        (
            "After all, I have to do all the cleaning\x01",
            "and laundry by hand now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0xFE,
        (
            "It's a tough job, but this is where I can\x01",
            "show the power of a housewife!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_6395")

    label("loc_62E8")


    ChrTalk(    #364
        0xFE,
        (
            "This old lady's going to do her part and work\x01",
            "hard to overcome these household struggles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0xFE,
        (
            "It's a tough job, but this is where I can\x01",
            "show the power of a housewife!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6395")

    Jump("loc_653A")

    label("loc_6398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_648F")
    TurnDirection(0xB, 0x102, 0)

    ChrTalk(    #366
        0xFE,
        (
            "This old lady isn't going to complain\x01",
            "about what's in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0xFE,
        (
            "After all, it was the hardest on you,\x01",
            "Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0xFE,
        "So, lift your head and smile, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0xFE,
        (
            "The number one thing for a young\x01",
            "man to have is a lovely smile.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_653A")

    label("loc_648F")


    ChrTalk(    #370
        0xFE,
        "How odd that orbal devices aren't working.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0xFE,
        (
            "I'm sure there's a lot out there that\x01",
            "needs doin', but don't overdo it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0xFE,
        "When you're tired, make sure you rest...\x02",
    )

    CloseMessageWindow()

    label("loc_653A")

    Jump("loc_834D")

    label("loc_653D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_6E59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34B, 3)), scpexpr(EXPR_END)), "loc_685D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_65D8")

    ChrTalk(    #373
        0xFE,
        (
            "Mmm, I'm terribly sorry, dear.\x01",
            "I don't know that specific recipe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0xFE,
        (
            "It might be a local recipe\x01",
            "only passed down in Rolent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_685A")

    label("loc_65D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6603")
    Call(1, 0)
    Jump("loc_685A")

    label("loc_6603")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6693")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #375
        0xFE,
        "Well, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0xFE,
        "Be sure to take care of yourself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0xFE,
        (
            "I'm looking forward to the day\x01",
            "you bring Joshua with you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67D4")

    label("loc_6693")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #378
        0xFE,
        (
            "I heard you all did amazingly this time too,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0xFE,
        (
            "The fog's finally cleared, and our bright,\x01",
            "happy city is back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0xFE,
        (
            "You have to go off again, I suppose.\x01",
            "But, Estelle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0xFE,
        (
            "Be sure to take care of your health\x01",
            "and stay well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0xFE,
        (
            "I'm looking forward to the day\x01",
            "you bring Joshua with you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)
    OP_A2(0x2)

    label("loc_67D4")

    Jump("loc_685A")

    label("loc_67D7")

    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(    #383
        0xFE,
        "...Schera.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0xFE,
        "This old lady believes in you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x103,
        (
            "#025FIt-It'll be okay.\x02\x03",

            "#525FYou can rest assured on that account.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_685A")

    Jump("loc_6E56")

    label("loc_685D")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #386
        0xFE,
        "My, my. Welcome, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0xFE,
        (
            "HI've heard all about the\x01",
            "wonderful job you've been doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x101,
        "#1008FAww, no... It was nothing that big.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0xFE,
        (
            "*sigh* Estelle, you've become such\x01",
            "an impressive bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0xFE,
        "The little girl I knew isn't here anymore.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0xFE,
        "*sniffle* Now I'm all by my lonesome...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x101,
        "#1004FH-Hey, Stella...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0xFE,
        "...Teehee. Just kidding. ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0xFE,
        (
            "Teehee. Looks like you've still\x01",
            "got a ways to go, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x101,
        (
            "#1016FUh... If you say so.\x02\x03",

            "(G-Geez, Stella's crying act is no joke.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0xFE,
        (
            "You have to go off again, I suppose.\x01",
            "But, Estelle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0xFE,
        (
            "Be sure to take care of your health\x01",
            "and stay well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0xFE,
        (
            "I'm looking forward to the day\x01",
            "you bring Joshua with you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #399
        0xFE,
        "So, Schera.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0xFE,
        "Take good care of Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0xFE,
        "Don't make her drink, all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0x103,
        (
            "#021FHaha. Don't worry.\x02\x03",

            "#525FIt's not my style to force alcohol on people.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(15)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6BFC")
    OP_62(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)

    label("loc_6BFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C26")
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)

    label("loc_6C26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C50")
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)

    label("loc_6C50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C7A")
    OP_62(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)

    label("loc_6C7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6CA4")
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)

    label("loc_6CA4")

    Sleep(1000)

    def lambda_6CAF():
        TurnDirection(0x0, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6CAF)

    def lambda_6CBD():
        TurnDirection(0x1, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_6CBD)

    def lambda_6CCB():
        TurnDirection(0x2, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_6CCB)
    TurnDirection(0x3, 0x103, 400)

    ChrTalk(    #403
        0x101,
        "#1020FWhaaa...?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D13")

    ChrTalk(    #404
        0x107,
        "#065FH-Huh...?!\x02",
    )

    CloseMessageWindow()

    label("loc_6D13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D47")

    ChrTalk(    #405
        0x105,
        "#542F(I-I must have misheard...)\x02",
    )

    CloseMessageWindow()

    label("loc_6D47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D67")

    ChrTalk(    #406
        0x104,
        "#036F...Heh.\x02",
    )

    CloseMessageWindow()

    label("loc_6D67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D83")

    ChrTalk(    #407
        0x108,
        "#073F...\x02",
    )

    CloseMessageWindow()

    label("loc_6D83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D9F")

    ChrTalk(    #408
        0x106,
        "#055F...\x02",
    )

    CloseMessageWindow()

    label("loc_6D9F")

    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x103, 0x3, 400)
    Sleep(400)
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #409
        0x103,
        "#023FOh, what is it, everyone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0xFE,
        "S-Suddenly this old lady is worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0xFE,
        "...Schera.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0xFE,
        "Please, we're counting on you.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A5B)
    OP_A2(0x3)

    label("loc_6E56")

    Jump("loc_834D")

    label("loc_6E59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7762")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 6)), scpexpr(EXPR_END)), "loc_7236")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_719F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6FA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_6F13")

    ChrTalk(    #413
        0xFE,
        (
            "It was a bit of a shock to see\x01",
            "the Royal Army come to town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0xFE,
        (
            "But, I can't deny that it's a relief having\x01",
            "those boys around right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FA5")

    label("loc_6F13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_6FA5")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #415
        0xFE,
        (
            "I'm sure things must be hard investigating\x01",
            "this case, but don't overdo it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0xFE,
        "If you collapsed, I...I just couldn't bear it!\x02",
    )

    CloseMessageWindow()

    label("loc_6FA5")

    Jump("loc_719C")

    label("loc_6FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_70B2")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #417
        0xFE,
        "My, my. Welcome, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0xFE,
        "Hard at work already, hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0xFE,
        (
            "It was a bit of a shock to see\x01",
            "the Royal Army come to town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0xFE,
        (
            "But, I can't deny that it's a relief having\x01",
            "those boys around right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0xFE,
        "Well, then, you take care out there.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7199")

    label("loc_70B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_7199")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #422
        0xFE,
        (
            "Oh, good morning.\x01",
            "You're all up early, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0xFE,
        (
            "I'm sure things must be hard investigating\x01",
            "this case, but don't overdo it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0xFE,
        "If you collapsed, I...I just couldn't bear it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x101,
        "#1008FI-I'll take care.\x02",
    )

    CloseMessageWindow()

    label("loc_7199")

    OP_A2(0x2)

    label("loc_719C")

    Jump("loc_7233")

    label("loc_719F")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #426
        0xFE,
        (
            "Even you're working so diligently,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0xFE,
        (
            "You've got such a perfectly lovely,\x01",
            "clean outfit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0xFE,
        "Ahh, I feel relieved somehow.\x02",
    )

    CloseMessageWindow()

    label("loc_7233")

    Jump("loc_775F")

    label("loc_7236")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #429
        0xFE,
        "Oh, my...!\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #430
        0xFE,
        "Aah, is it...? Is it truly Estelle?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0xFE,
        (
            "I heard rumors you'd come in yesterday, and\x01",
            "I've been waiting and waiting for you to visit me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0x101,
        "#1008FAhaha... It's been a while, Miss Stella.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0x103,
        (
            "#020FWe're sorry we didn't come to\x01",
            "offer our greetings sooner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0xFE,
        (
            "No, not at all.\x01",
            "You were busy with work, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0xFE,
        (
            "I was a bit worried when I heard\x01",
            "about Joshua, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0xFE,
        (
            "It looks like you're giving it\x01",
            "your best, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0x101,
        "#1016FY-Yeah... Somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0xFE,
        "Well, putting that aside, Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0xFE,
        "Hmmmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0x101,
        (
            "#1015FWh-What? Why are you staring at me?\x02\x03",

            "I brushed my teeth and washed my face. I know\x01",
            "I did. I swear! I even got behind the ears!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #441
        0xFE,
        "#3SOhh, it's just wonderful!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #442
        0x101,
        "#1004FWhat is?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0xFE,
        "What is this SKIRT!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #444
        0xFE,
        (
            "It's just perfect on you! It matches\x01",
            "that feeling of being an energetic\x01",
            "young woman!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0x101,
        (
            "#1008FAhaha... Y-You think so?\x02\x03",

            "Schera bought this for me in the capital.\x02\x03",

            "It was a present for becoming a full bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #446
        0xFE,
        (
            "Hmm, very nice, Schera.\x01",
            "You've got good taste!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0x103,
        "#021FI'm glad you like it, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0xFE,
        "Your attitude reveals itself in your clothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #449
        0xFE,
        (
            "I can tell you're working\x01",
            "hard on the current case...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #450
        0xFE,
        (
            "Yes, yes. Looks like you'll do\x01",
            "wonderfully as a full bracer.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188E)
    OP_A2(0x3)

    label("loc_775F")

    Jump("loc_834D")

    label("loc_7762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_7EE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 6)), scpexpr(EXPR_END)), "loc_7807")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #451
        0xFE,
        (
            "Even you're working so diligently,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0xFE,
        (
            "You've got such a perfectly lovely,\x01",
            "clean outfit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #453
        0xFE,
        "Ahh, I feel relieved somehow.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7EE0")

    label("loc_7807")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #454
        0xFE,
        "Oh, my...!\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #455
        0xFE,
        "Oh, my goodness! If it isn't Estelle!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #456
        0xFE,
        (
            "My, my, my! And looking closely,\x01",
            "Schera's with her, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #457
        0x101,
        "#1008FHeya! Been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0x103,
        "#021FHeehee. Indeed, it has.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #459
        0xFE,
        (
            "Awwww, it really has! I've been\x01",
            "pretty frustrated, you know.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #460
        0xFE,
        (
            "After all, I kept hearing rumors you were\x01",
            "back, but I couldn't meet you in person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0x101,
        "#1016FAhaha, sorry, Stella.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #462
        0x103,
        (
            "#027FWell, Estelle's been preoccupied with\x01",
            "a few things.\x02\x03",

            "Mind forgiving her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #463
        0xFE,
        (
            "Don't you worry about that.\x01",
            "Even this old lady knows that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #464
        0xFE,
        (
            "I was a bit worried when I heard\x01",
            "about Joshua, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0xFE,
        (
            "It looks like you're giving it\x01",
            "your best, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #466
        0x101,
        "#1016FY-Yeah... Somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #467
        0xFE,
        "Well, putting that aside, Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #468
        0xFE,
        "Hmmmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #469
        0x101,
        (
            "#1015FWh-What? Why are you staring at me?\x02\x03",

            "I brushed my teeth and washed my face. I know\x01",
            "I did. I swear! I even got behind the ears!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #470
        0xFE,
        "#3SOhh, it's just wonderful!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #471
        0x101,
        "#1004FWhat is?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #472
        0xFE,
        "What is this SKIRT!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #473
        0xFE,
        (
            "It's just perfect on you! It matches\x01",
            "that feeling of being an energetic\x01",
            "young woman!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #474
        0x101,
        (
            "#1008FAhaha... Y-You think so?\x02\x03",

            "Schera bought this for me in the capital.\x02\x03",

            "It was a present for becoming a full bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #475
        0xFE,
        (
            "Hmm, very nice, Schera.\x01",
            "You've got good taste!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #476
        0x103,
        "#021FI'm glad you like it, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #477
        0xFE,
        "Your attitude reveals itself in your clothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #478
        0xFE,
        (
            "Yes, yes. Looks like you'll do\x01",
            "wonderfully as a full bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #479
        0xFE,
        (
            "My sloppy, dirty little Estelle's\x01",
            "become this clean and sharp...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #480
        0xFE,
        "Oooh... Th-This old lady is going to cry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #481
        0x101,
        (
            "#1008FHa... Haha...\x02\x03",

            "#1013F(I... I didn't think she'd cry over a skirt.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #482
        0x103,
        (
            "#025F(If she saw you dressed up for a wedding\x01",
            "she'd probably collapse on the spot.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x188E)

    label("loc_7EE0")

    Jump("loc_834D")

    label("loc_7EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_834D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 0)), scpexpr(EXPR_END)), "loc_7F59")

    ChrTalk(    #483
        0xFE,
        (
            "Estelle, next time bring Joshua\x01",
            "with you and stay a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #484
        0xFE,
        "I'll make your favorite dishes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_834D")

    label("loc_7F59")

    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(600)
    OP_63(0xFE)

    ChrTalk(    #485
        0xFE,
        "...Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #486
        0x101,
        "#001FHiya, Stella.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #487
        0xFE,
        "It's really you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #488
        0x101,
        "#501FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #489
        0xFE,
        "It's really my little Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #490
        0xFE,
        (
            "Oh, Aidios. It feels like I haven't\x01",
            "seen you in years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #491
        0x101,
        (
            "#506FI kinda think you're blowing\x01",
            "it out of proportion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #492
        0xFE,
        "We talked about you every day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #493
        0xFE,
        (
            "You went off to travel without\x01",
            "saying anything to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #494
        0x101,
        "#008F Yeah... Sorry, Stella.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #495
        0xFE,
        (
            "Oh, it's all right.\x01",
            "I know you were in a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #496
        0xFE,
        (
            "More importantly, come on!\x01",
            "Tell me all about your journey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #497
        0xFE,
        (
            "I'd love to see Joshua, too.\x01",
            "Is he with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #498
        0x101,
        "#501FUm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #499
        0x142,
        "#1060FAh, excuse me...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x142, 400)

    ChrTalk(    #500
        0xFE,
        "Pardon, you're...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #501
        0x142,
        (
            "#1060FNice to meet'cha.\x01",
            "I'm Kevin Graham, wandering priest.\x02\x03",

            "Sorry to interrupt the reunion, but\x01",
            "Estelle's in a bit of a hurry.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #502
        0xFE,
        "O-Oh... Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #503
        0xFE,
        "I'm sorry. I just got so excited...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #504
        0x101,
        (
            "#000FNo, don't worry about it.\x01",
            "I'll make sure to come by again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #505
        0xFE,
        "Yes, I'll make your favorite dish, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #506
        0xFE,
        "Bring Joshua next time, too!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1030)

    label("loc_834D")

    TalkEnd(0xB)
    Return()

    # Function_8_5D88 end

    def Function_9_8351(): pass

    label("Function_9_8351")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_8432")

    ChrTalk(    #507
        0xFE,
        (
            "Looks like the scheduled flights are\x01",
            "grounded until the fog clears.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #508
        0xFE,
        (
            "In which case, seems I'll have to\x01",
            "spend a while longer here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #509
        0xFE,
        (
            "I'd be less bored if there was at\x01",
            "least some sightseeing nearby to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8432")

    TalkEnd(0xC)
    Return()

    # Function_9_8351 end

    def Function_10_8436(): pass

    label("Function_10_8436")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_84D3")

    ChrTalk(    #510
        0xFE,
        (
            "There's a lot of places I'd like to get shots\x01",
            "of, like the Gurune Gate, or the Verte Bridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #511
        0xFE,
        "I'm in Rolent, but this is such a waste.\x02",
    )

    CloseMessageWindow()
    Jump("loc_86B9")

    label("loc_84D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_86B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_8578")

    ChrTalk(    #512
        0xFE,
        (
            "I came to get the photos from\x01",
            "my trip developed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #513
        0xFE,
        (
            "I can't go anywhere thanks to the fog,\x01",
            "so I figured I might as well look over\x01",
            "my photos.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86B9")

    label("loc_8578")


    ChrTalk(    #514
        0xFE,
        (
            "I came to get the photos from\x01",
            "my trip developed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #515
        0xFE,
        (
            "I can't go anywhere thanks to the fog,\x01",
            "so I figured I might as well look over\x01",
            "my photos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #516
        0xFE,
        (
            "There's a lot of things that'd make great photos\x01",
            "here, like Rolent's clock tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #517
        0xFE,
        (
            "In this weather I'd basically just be\x01",
            "wasting my photo-quartz, though.\x01",
            "*sigh*\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_86B9")

    TalkEnd(0xD)
    Return()

    # Function_10_8436 end

    SaveToFile()

Try(main)
