from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4135   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4135.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        'Licia',                                # 9
        'Museum Director',                      # 10
        'Santos',                               # 11
        'Wilma',                                # 12
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
        'ED6_DT07/CH01540 ._CH',             # 00
        'ED6_DT07/CH01490 ._CH',             # 01
        'ED6_DT07/CH01660 ._CH',             # 02
        'ED6_DT07/CH01430 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01540P._CP',             # 00
        'ED6_DT07/CH01490P._CP',             # 01
        'ED6_DT07/CH01660P._CP',             # 02
        'ED6_DT07/CH01430P._CP',             # 03
        'ED6_DT07/CH01140P._CP',             # 04
    )

    DeclNpc(
        X                   = 4400,
        Z                   = 0,
        Y                   = -5910,
        Direction           = 255,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -5500,
        Z                   = 0,
        Y                   = 67620,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -69590,
        Z                   = 0,
        Y                   = -2210,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -69580,
        Z                   = 0,
        Y                   = -580,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    DeclActor(
        TriggerX            = 2580,
        TriggerZ            = 0,
        TriggerY            = -5970,
        TriggerRange        = 800,
        ActorX              = 4400,
        ActorZ              = 1700,
        ActorY              = -5910,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5090,
        TriggerZ            = 0,
        TriggerY            = 2190,
        TriggerRange        = 800,
        ActorX              = 5090,
        ActorZ              = 800,
        ActorY              = 2190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7840,
        TriggerZ            = 4000,
        TriggerY            = 6700,
        TriggerRange        = 800,
        ActorX              = 7840,
        ActorZ              = 5700,
        ActorY              = 6700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75860,
        TriggerZ            = 0,
        TriggerY            = -2000,
        TriggerRange        = 800,
        ActorX              = 75860,
        ActorZ              = 1500,
        ActorY              = -2000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 73200,
        TriggerZ            = 0,
        TriggerY            = 710,
        TriggerRange        = 800,
        ActorX              = 73200,
        ActorZ              = 800,
        ActorY              = 710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 68740,
        TriggerZ            = 0,
        TriggerY            = 7310,
        TriggerRange        = 800,
        ActorX              = 68740,
        ActorZ              = 800,
        ActorY              = 7310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 73480,
        TriggerZ            = 0,
        TriggerY            = 6420,
        TriggerRange        = 800,
        ActorX              = 73480,
        ActorZ              = 800,
        ActorY              = 6420,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75820,
        TriggerZ            = 4000,
        TriggerY            = 8010,
        TriggerRange        = 800,
        ActorX              = 75820,
        ActorZ              = 5700,
        ActorY              = 8010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 71960,
        TriggerZ            = 4000,
        TriggerY            = 9290,
        TriggerRange        = 800,
        ActorX              = 71960,
        ActorZ              = 4800,
        ActorY              = 9290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20,
        TriggerZ            = 0,
        TriggerY            = 77880,
        TriggerRange        = 800,
        ActorX              = -20,
        ActorZ              = 1700,
        ActorY              = 77880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -770,
        TriggerZ            = 0,
        TriggerY            = 72650,
        TriggerRange        = 800,
        ActorX              = -770,
        ActorZ              = 800,
        ActorY              = 72650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7000,
        TriggerZ            = 0,
        TriggerY            = 66550,
        TriggerRange        = 1200,
        ActorX              = 7000,
        ActorZ              = 800,
        ActorY              = 66550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1770,
        TriggerZ            = 0,
        TriggerY            = 66890,
        TriggerRange        = 800,
        ActorX              = 1770,
        ActorZ              = 800,
        ActorY              = 66890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3790,
        TriggerZ            = 0,
        TriggerY            = 64959,
        TriggerRange        = 800,
        ActorX              = -3790,
        ActorZ              = 800,
        ActorY              = 64959,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_346",          # 00, 0
        "Function_1_358",          # 01, 1
        "Function_2_368",          # 02, 2
        "Function_3_37E",          # 03, 3
        "Function_4_72F",          # 04, 4
        "Function_5_91C",          # 05, 5
        "Function_6_C15",          # 06, 6
        "Function_7_C1A",          # 07, 7
        "Function_8_E25",          # 08, 8
        "Function_9_FBB",          # 09, 9
        "Function_10_1432",        # 0A, 10
        "Function_11_1688",        # 0B, 11
        "Function_12_1777",        # 0C, 12
        "Function_13_1864",        # 0D, 13
        "Function_14_1954",        # 0E, 14
        "Function_15_1AE2",        # 0F, 15
        "Function_16_1CD9",        # 10, 16
        "Function_17_1EFC",        # 11, 17
        "Function_18_2125",        # 12, 18
        "Function_19_22E6",        # 13, 19
        "Function_20_2425",        # 14, 20
    )


    def Function_0_346(): pass

    label("Function_0_346")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_357")
    SetChrFlags(0x12, 0x10)

    label("loc_357")

    Return()

    # Function_0_346 end

    def Function_1_358(): pass

    label("Function_1_358")

    OP_B1("t4135_n")
    OP_71(0x401, 0x0)
    ExitThread()
    Return()

    # Function_1_358 end

    def Function_2_368(): pass

    label("Function_2_368")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_368")

    label("loc_37D")

    Return()

    # Function_2_368 end

    def Function_3_37E(): pass

    label("Function_3_37E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_38B")
    Jump("loc_72B")

    label("loc_38B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_54A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_435")
    OP_8C(0xFE, 270, 0)

    ChrTalk(    #0
        0xFE,
        (
            "Santos'll be heading off for a conference\x01",
            "in the near future, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Which means that for a while, the only\x01",
            "researcher here will be me...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_547")

    label("loc_435")


    ChrTalk(    #2
        0xFE,
        (
            "The curator here, Wilma, is exceptional at\x01",
            "her job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Which is why it's such a blow to us that she's\x01",
            "going to be leaving us for a research institute\x01",
            "abroad soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "Still, as much as I'll miss her, the right thing\x01",
            "to do here is to wish her well for the future!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_547")

    Jump("loc_72B")

    label("loc_54A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_72B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_645")

    ChrTalk(    #5
        0xFE,
        (
            "Tons of fascinating archaeological finds get\x01",
            "discovered here in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Many of them come from Valleria Lake, but the\x01",
            "Ahnenburg Wall is actually an ancient ruin, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Funny thing, though. Most folks don't realize\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72B")

    label("loc_645")


    ChrTalk(    #8
        0xFE,
        (
            "This vase here was only salvaged from Valleria\x01",
            "Lake last month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "Judging by the design, it's from the Middle Ages.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Haha. I always get as excited as a child on their\x01",
            "birthday when things like these get brought in.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_72B")

    TalkEnd(0xFE)
    Return()

    # Function_3_37E end

    def Function_4_72F(): pass

    label("Function_4_72F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_73C")
    Jump("loc_918")

    label("loc_73C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_83D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_7CB")

    ChrTalk(    #11
        0xFE,
        (
            "The Tetracyclic Towers aren't exactly well known\x01",
            "outside of Liberl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "...so would a paper on them be well received?\x02",
    )

    CloseMessageWindow()
    Jump("loc_83A")

    label("loc_7CB")


    ChrTalk(    #13
        0xFE,
        "I wonder if I should choose a different topic...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "Oooh... I wish I wasn't doubting myself so much!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_83A")

    Jump("loc_918")

    label("loc_83D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_918")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_8A9")

    ChrTalk(    #15
        0xFE,
        (
            "I think I could probably have done with more in\x01",
            "the way of research materials, too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_918")

    label("loc_8A9")


    ChrTalk(    #16
        0xFE,
        "Wh-What do you think, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "I feel so uncertain about how persuasively\x01",
            "I'm putting my argument...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_918")

    TalkEnd(0xFE)
    Return()

    # Function_4_72F end

    def Function_5_91C(): pass

    label("Function_5_91C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_929")
    Jump("loc_C11")

    label("loc_929")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_ABA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_A01")

    ChrTalk(    #18
        0xFE,
        (
            "This year's archeology conference is over in\x01",
            "the Ored State, I believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "Aww... I wish I could've gooone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "Chances of me going aren't looking so hot\x01",
            "this year, either. It bums me out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB7")

    label("loc_A01")

    OP_8C(0xFE, 180, 0)

    ChrTalk(    #21
        0xFE,
        (
            "It's normal to be nervous and start doubting\x01",
            "yourself when you've got your first conference\x01",
            "coming up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Just take a deeeeep breath and relax.\x01",
            "It's gonna be great!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_AB7")

    Jump("loc_C11")

    label("loc_ABA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_C11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_B31")

    ChrTalk(    #23
        0xFE,
        "Santos has his first conference coming up soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "I can't go with him, though I wish I could.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C11")

    label("loc_B31")

    OP_8C(0xFE, 180, 0)

    ChrTalk(    #25
        0xFE,
        (
            "Yeah, your ideas are good, but I think you need a\x01",
            "little more in the way of hard research to back\x01",
            "them up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "I've got a few papers that I think might help you,\x01",
            "as it so happens. Want me to lend 'em to you?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_C11")

    TalkEnd(0xFE)
    Return()

    # Function_5_91C end

    def Function_6_C15(): pass

    label("Function_6_C15")

    Call(0, 7)
    Return()

    # Function_6_C15 end

    def Function_7_C1A(): pass

    label("Function_7_C1A")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_C27")
    Jump("loc_E21")

    label("loc_C27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_DC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CB5")

    ChrTalk(    #27
        0x10,
        "Wilma's going to be moving abroad next month...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        (
            "I'll really miss her... She's been an incredible\x01",
            "part of our team.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBF")

    label("loc_CB5")


    ChrTalk(    #29
        0x10,
        (
            "Wilma, the curator here, is going to be leaving\x01",
            "next month for a research institute abroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "She'll be missed, but none of us have any right\x01",
            "to stop her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10,
        (
            "The fact that she's able to do that just goes to\x01",
            "show how talented she is, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_DBF")

    Jump("loc_E21")

    label("loc_DC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_E21")

    ChrTalk(    #33
        0x10,
        "Hello! Welcome to the history museum.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        "Please feel free to take a look around.\x02",
    )

    CloseMessageWindow()

    label("loc_E21")

    TalkEnd(0x10)
    Return()

    # Function_7_C1A end

    def Function_8_E25(): pass

    label("Function_8_E25")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #35
        (
            "\x07\x05[Tetracyclic Tower Outer Wall Segment]         Age: Pre-Septian?\x01",
            "This wall segment was cut and carried from a Tetracyclic Tower--\x01",
            "a structure built shortly after the Great Collapse.\x01",
            "Depicted upon it are a staff-wielding priest and a winged god-\x01",
            "like being, typical of period frescas. Scholars continue to\x01",
            "examine the design for any connection with Aidios.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_E25 end

    def Function_9_FBB(): pass

    label("Function_9_FBB")

    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E6")
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #36
        (
            "\x07\x05[Septian 1150-1200  ~The Orbal Post-Revolutionary World~]\x01",
            "It's been only 50 years since Prof. C. Epstein invented orbments,\x01",
            "and world technology has advanced at lightning speed ever since.\x01",
            "Perhaps the most notable representative of these advances is the \x01",
            "modern orbal-powered airship. These 'orbalships' are already used\x01",
            "extensively in Liberl, but neighboring nations such as Erebonia\x01",
            "have also begun to devote themselves to their manufacture as well,\x01",
            "and smaller-sized airships are also used.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_142E")

    label("loc_11E6")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #37
        (
            "\x07\x05[Pre-Septian Calendar  ~The Ancient Civilization of Zemuria~]\x01",
            "Around 1,200 years ago, the advanced civilization of Zemuria was\x01",
            "at its peak. Then, suddenly and inexplicably, it disappeared.\x01",
            "A 'Great Collapse' occurred, destroying the Zemurian culture and\x01",
            "plunging its people into a dark age of ruin. The items exhibited\x01",
            "on the first floor are from the very beginning of this era. They\x01",
            "aren't believed to be products of the ancient civilization itself,\x01",
            "but nonetheless, its influence is clearly visible upon them, giving\x01",
            "them immense academic worth.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_142E")

    TalkEnd(0xFF)
    Return()

    # Function_9_FBB end

    def Function_10_1432(): pass

    label("Function_10_1432")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #38
        (
            "\x07\x05[Pre-Septian Calendar  ~The Ancient Civilization of Zemuria~]\x01",
            "Around 1,200 years ago, the advanced civilization of Zemuria was\x01",
            "at its peak. Then, suddenly and inexplicably, it disappeared.\x01",
            "A 'Great Collapse' occurred, destroying the Zemurian culture and\x01",
            "plunging its people into a dark age of ruin. The items exhibited\x01",
            "on the first floor are from the very beginning of this era. They\x01",
            "aren't believed to be products of the ancient civilization itself,\x01",
            "but nonetheless, its influence is clearly visible upon them, giving\x01",
            "them immense academic worth.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_1432 end

    def Function_11_1688(): pass

    label("Function_11_1688")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #39
        (
            "\x07\x05[Ancient Lantern]                              Age: Pre-Septian?\x01",
            "A device built to hold fire. Most often found near towers and\x01",
            "other ceremonial structures. May have religious significance.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_1688 end

    def Function_12_1777(): pass

    label("Function_12_1777")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #40
        (
            "\x07\x05[Stone Pillar with Relief]                     Age: Pre-Septian?\x01",
            "Found at the bottom of Valleria Lake. Adorned with reliefs\x01",
            "similar to those found on the walls of the Tetracyclic Towers.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_12_1777 end

    def Function_13_1864(): pass

    label("Function_13_1864")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #41
        (
            "\x07\x05[Floor Tile]                                   Age: Pre-Septian?\x01",
            "A piece of tiled floor from inside a ruined building. Broken\x01",
            "stones fit together to create beautiful and intricate patterns.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_1864 end

    def Function_14_1954(): pass

    label("Function_14_1954")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #42
        (
            "\x07\x05[Septian Calendar 1-500  ~The Dark Age of Ruin~]\x01",
            "Immediately following the Great Collapse, the world was plunged\x01",
            "into confusion, signaling the beginning of what came to be\x01",
            "referred to as the Dark Ages. \x01",
            "This era was defined by almost endless conflict between various\x01",
            "powers and numerous nations, large and small, and lasted for \x01",
            "roughly 500 years.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_14_1954 end

    def Function_15_1AE2(): pass

    label("Function_15_1AE2")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #43
        (
            "\x07\x05[Knights' Equipment]                    Age: Septian Calendar 500\x01",
            "In an era defined by conflict, war became a way of life, and as a\x01",
            "result, warriors came to wield great influence in society. This\x01",
            "eventually led to them becoming a privileged social class of their\x01",
            "own.\x01",
            "The knights wielded armaments like these when they went out onto \x01",
            "the battlefield, returning with more spoils and land, and gradually\x01",
            "increasing their influence and power all the more.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_1AE2 end

    def Function_16_1CD9(): pass

    label("Function_16_1CD9")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #44
        (
            "\x07\x05[Septian Calendar 500-1100  ~The Septian Era~]\x01",
            "The first appearance of the Septian Church occurred around the\x01",
            "year 500 and marked the end of the Dark Ages.\x01",
            "The church, centered around the 'Goddess of the Sky' Aidios and\x01",
            "espousing an ideology of human salvation, began to take an active\x01",
            "role in society and rapidly permeated social consciousness. \x01",
            "Eventually, the nobility and knight class could no longer ignore\x01",
            "the church's power, and a new order was established with the \x01",
            "church at the center. \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_1CD9 end

    def Function_17_1EFC(): pass

    label("Function_17_1EFC")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #45
        (
            "\x07\x05[Ancient Artifacts]                                 Age: Unknown\x01",
            "'Artifact' (noun) - A relic of any shape or size found in an\x01",
            "ancient ruin and generally of unknown or uncertain purpose.\x01",
            "The church believes these artifacts have some connection with\x01",
            "the Sept-Terrions--gifts from Aidios--and their recovery is\x01",
            "one of the duties that the church fulfills. \x01",
            "Artifacts are said to have supernatural powers, but those on\x01",
            "display here are all ones that have since lost said powers and\x01",
            "are no longer functional.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_1EFC end

    def Function_18_2125(): pass

    label("Function_18_2125")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #46
        (
            "\x07\x05[Church Ritual Items]          Age: Septian Calendar 900 (approx.)\x01",
            "The church has long been a source of art, and this has been true\x01",
            "since the dawn of the Septian Era. It was around the year 900,\x01",
            "however, that the current likeness of Aidios is thought to have\x01",
            "been first created. Likewise, many of the ritual items used by\x01",
            "the church today first assumed their present forms in this time\x01",
            "period, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_2125 end

    def Function_19_22E6(): pass

    label("Function_19_22E6")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #47
        (
            "\x07\x05[Church Testaments, Manuscript]        Age: Septian Calendar 500\x01",
            "A handwritten copy of the scriptures used by the church at the\x01",
            "end of the Dark Ages. The ability to print did not exist in the\x01",
            "Middle Ages, leaving no choice but to copy by hand onto pieces\x01",
            "of parchment.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_22E6 end

    def Function_20_2425(): pass

    label("Function_20_2425")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #48
        (
            "\x07\x05[Medieval Loom]                        Age: Septian Calendar 900\x01",
            "A man-powered machine used to spin thread. As the Septian Era\x01",
            "continued and people became accustomed to peace, cotton and \x01",
            "other crops became more widely cultivated and sold. This was \x01",
            "also the era in which handicrafts with the intent to obtain money \x01",
            "came into practice.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_20_2425 end

    SaveToFile()

Try(main)
