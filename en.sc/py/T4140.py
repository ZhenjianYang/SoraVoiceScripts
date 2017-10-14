from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4140   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4140.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Chaeli',                               # 9
        'Shepard',                              # 10
        'Zacharias',                            # 11
        'Tom',                                  # 12
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
        'ED6_DT07/CH01690 ._CH',             # 00
        'ED6_DT07/CH01140 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01043 ._CH',             # 03
        'ED6_DT07/CH01680 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01690P._CP',             # 00
        'ED6_DT07/CH01140P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01043P._CP',             # 03
        'ED6_DT07/CH01680P._CP',             # 04
    )

    DeclNpc(
        X                   = 1260,
        Z                   = 0,
        Y                   = -240,
        Direction           = 236,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 0,
        Y                   = 129840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 58580,
        Z                   = 0,
        Y                   = 360,
        Direction           = 102,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 120030,
        Z                   = 0,
        Y                   = -1260,
        Direction           = 10,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    DeclActor(
        TriggerX            = -10,
        TriggerZ            = 0,
        TriggerY            = -1600,
        TriggerRange        = 800,
        ActorX              = 1260,
        ActorZ              = 1500,
        ActorY              = -240,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 60410,
        TriggerZ            = 0,
        TriggerY            = 390,
        TriggerRange        = 800,
        ActorX              = 58580,
        ActorZ              = 1500,
        ActorY              = 360,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 119960,
        TriggerZ            = 0,
        TriggerY            = 650,
        TriggerRange        = 800,
        ActorX              = 120030,
        ActorZ              = 1500,
        ActorY              = -1260,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1BE",          # 00, 0
        "Function_1_1F4",          # 01, 1
        "Function_2_216",          # 02, 2
        "Function_3_23A",          # 03, 3
        "Function_4_23F",          # 04, 4
        "Function_5_34D",          # 05, 5
        "Function_6_352",          # 06, 6
        "Function_7_4EC",          # 07, 7
        "Function_8_4F1",          # 08, 8
        "Function_9_5F9",          # 09, 9
    )


    def Function_0_1BE(): pass

    label("Function_0_1BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F3")
    OP_44(0xB, 0x0)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 3)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xB, 125240, 200, -1310, 90)

    label("loc_1F3")

    Return()

    # Function_0_1BE end

    def Function_1_1F4(): pass

    label("Function_1_1F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_205")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_215")
    OP_64(0x2, 0x1)

    label("loc_215")

    Return()

    # Function_1_1F4 end

    def Function_2_216(): pass

    label("Function_2_216")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_239")
    OP_8D(0x9, 1470, 131290, -1690, 128210, 2000)
    Jump("Function_2_216")

    label("loc_239")

    Return()

    # Function_2_216 end

    def Function_3_23A(): pass

    label("Function_3_23A")

    Call(0, 4)
    Return()

    # Function_3_23A end

    def Function_4_23F(): pass

    label("Function_4_23F")

    TalkBegin(0xA)
    Call(6, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25C")
    OP_A9(0xC8)
    TalkEnd(0xA)
    Return()

    label("loc_25C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26D")
    TalkEnd(0xA)
    Return()

    label("loc_26D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_2BE")

    ChrTalk(    #0
        0xA,
        "Why do you look so panicked?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xA,
        "Our store's not going anywhere.\x02",
    )

    CloseMessageWindow()
    Jump("loc_349")

    label("loc_2BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_349")

    ChrTalk(    #2
        0xA,
        (
            "Lately, the South Block's been\x01",
            "open even at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xA,
        (
            "Sounds like a pain, but it's not\x01",
            "a bad way to rake in some extra\x01",
            "cash.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_349")

    TalkEnd(0xA)
    Return()

    # Function_4_23F end

    def Function_5_34D(): pass

    label("Function_5_34D")

    Call(0, 6)
    Return()

    # Function_5_34D end

    def Function_6_352(): pass

    label("Function_6_352")

    TalkBegin(0x8)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_380")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_377")
    OP_A9(0xDA)
    Jump("loc_379")

    label("loc_377")

    OP_A9(0xC9)

    label("loc_379")

    TalkEnd(0x8)
    Return()

    label("loc_380")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_391")
    TalkEnd(0x8)
    Return()

    label("loc_391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_411")

    ChrTalk(    #4
        0x8,
        (
            "*sigh* I can't stand this. I guess\x01",
            "I really should leave this house...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        "Ah... I-I'm sorry. Welcome!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E8")

    label("loc_411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_4E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C6")

    ChrTalk(    #7
        0x8,
        (
            "*sigh* I had a fight with\x01",
            "my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "...Sort of. Since he never\x01",
            "really talks, it was mostly\x01",
            "just me getting angry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        "It feels so empty somehow...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_4E8")

    label("loc_4C6")


    ChrTalk(    #10
        0x8,
        "Maybe I don't matter to him.\x02",
    )

    CloseMessageWindow()

    label("loc_4E8")

    TalkEnd(0x8)
    Return()

    # Function_6_352 end

    def Function_7_4EC(): pass

    label("Function_7_4EC")

    Call(0, 8)
    Return()

    # Function_7_4EC end

    def Function_8_4F1(): pass

    label("Function_8_4F1")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_580")

    ChrTalk(    #11
        0xB,
        (
            "Maybe it's because everything's\x01",
            "dark, but I can really focus on my\x01",
            "work at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xB,
        "All right, time to repair this stuff.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F5")

    label("loc_580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_5F5")

    ChrTalk(    #13
        0xB,
        (
            "Well, that's a problem...\x01",
            "Looks like the quartz shorted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xB,
        (
            "If I adjust this here...\x01",
            "*mutter* *mutter*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F5")

    TalkEnd(0xB)
    Return()

    # Function_8_4F1 end

    def Function_9_5F9(): pass

    label("Function_9_5F9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_6B1")

    ChrTalk(    #15
        0xFE,
        (
            "I had a fight with my wife,\x01",
            "so she wouldn't make dinner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "I made myself some pasta\x01",
            "since I didn't have any other\x01",
            "options, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "That just made her angrier.\x02",
    )

    CloseMessageWindow()
    Jump("loc_823")

    label("loc_6B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_823")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C4")

    ChrTalk(    #18
        0xFE,
        (
            "I wanted to talk to my wife\x01",
            "about the store...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "I really did, but something's\x01",
            "got her angry right now, so\x01",
            "she won't listen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I'm not the most talkative guy in the\x01",
            "world; sometimes, my wife takes that\x01",
            "as me not wanting to talk to her at all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_823")

    label("loc_7C4")


    ChrTalk(    #21
        0xFE,
        (
            "I love my wife as much as\x01",
            "I ever could, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "I just don't really know what to say.\x02",
    )

    CloseMessageWindow()

    label("loc_823")

    TalkEnd(0xFE)
    Return()

    # Function_9_5F9 end

    SaveToFile()

Try(main)
