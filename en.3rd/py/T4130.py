from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4130   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4130.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Editor-in-Chief',                      # 9
        'Noticia',                              # 10
        'Faults',                               # 11
        'Sariah',                               # 12
        'Baral',                                # 13
        'Connor',                               # 14
        'Cready',                               # 15
        'Spencer',                              # 16
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
        'ED6_DT07/CH02060 ._CH',             # 00
        'ED6_DT07/CH01023 ._CH',             # 01
        'ED6_DT07/CH01100 ._CH',             # 02
        'ED6_DT07/CH01150 ._CH',             # 03
        'ED6_DT07/CH01143 ._CH',             # 04
        'ED6_DT07/CH01210 ._CH',             # 05
        'ED6_DT07/CH02070 ._CH',             # 06
        'ED6_DT07/CH01540 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH02060P._CP',             # 00
        'ED6_DT07/CH01023P._CP',             # 01
        'ED6_DT07/CH01100P._CP',             # 02
        'ED6_DT07/CH01150P._CP',             # 03
        'ED6_DT07/CH01143P._CP',             # 04
        'ED6_DT07/CH01210P._CP',             # 05
        'ED6_DT07/CH02070P._CP',             # 06
        'ED6_DT07/CH01540P._CP',             # 07
    )

    DeclNpc(
        X                   = -54100,
        Z                   = 200,
        Y                   = 61000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -56570,
        Z                   = 0,
        Y                   = 64660,
        Direction           = 1,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -59030,
        Z                   = 100,
        Y                   = 59540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -56630,
        Z                   = 0,
        Y                   = 5500,
        Direction           = 174,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 61020,
        Z                   = 0,
        Y                   = 2490,
        Direction           = 180,
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
        X                   = 65800,
        Z                   = 100,
        Y                   = -3410,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 4560,
        Z                   = 0,
        Y                   = 2500,
        Direction           = 186,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 4500,
        Z                   = 100,
        Y                   = -3850,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    DeclActor(
        TriggerX            = 60700,
        TriggerZ            = 0,
        TriggerY            = 550,
        TriggerRange        = 400,
        ActorX              = 61020,
        ActorZ              = 1500,
        ActorY              = 2490,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4530,
        TriggerZ            = 0,
        TriggerY            = 590,
        TriggerRange        = 400,
        ActorX              = 4560,
        ActorZ              = 1500,
        ActorY              = 2500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -56840,
        TriggerZ            = 0,
        TriggerY            = 3500,
        TriggerRange        = 400,
        ActorX              = -56630,
        ActorZ              = 1500,
        ActorY              = 5500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 57530,
        TriggerZ            = 0,
        TriggerY            = 400,
        TriggerRange        = 800,
        ActorX              = 57290,
        ActorZ              = 900,
        ActorY              = 340,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2480,
        TriggerZ            = -250,
        TriggerY            = -3810,
        TriggerRange        = 800,
        ActorX              = 2480,
        ActorZ              = 1100,
        ActorY              = -3810,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_29E",          # 00, 0
        "Function_1_29F",          # 01, 1
        "Function_2_2AC",          # 02, 2
        "Function_3_429",          # 03, 3
        "Function_4_42E",          # 04, 4
        "Function_5_606",          # 05, 5
        "Function_6_80A",          # 06, 6
        "Function_7_80F",          # 07, 7
        "Function_8_A87",          # 08, 8
        "Function_9_E4C",          # 09, 9
        "Function_10_FE6",         # 0A, 10
        "Function_11_1226",        # 0B, 11
        "Function_12_1445",        # 0C, 12
        "Function_13_144A",        # 0D, 13
        "Function_14_1565",        # 0E, 14
        "Function_15_16C2",        # 0F, 15
    )


    def Function_0_29E(): pass

    label("Function_0_29E")

    Return()

    # Function_0_29E end

    def Function_1_29F(): pass

    label("Function_1_29F")

    OP_B1("t4130_n")
    OP_82(0x82, 0x0)
    Return()

    # Function_1_29F end

    def Function_2_2AC(): pass

    label("Function_2_2AC")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D1")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_413")

    label("loc_2D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EA")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_413")

    label("loc_2EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_303")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_413")

    label("loc_303")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31C")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_413")

    label("loc_31C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_335")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_413")

    label("loc_335")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34E")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_413")

    label("loc_34E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_367")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_413")

    label("loc_367")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_380")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_413")

    label("loc_380")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_399")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_413")

    label("loc_399")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B2")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_413")

    label("loc_3B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CB")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_413")

    label("loc_3CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E4")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_413")

    label("loc_3E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FD")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_413")

    label("loc_3FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_413")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_413")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_428")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_413")

    label("loc_428")

    Return()

    # Function_2_2AC end

    def Function_3_429(): pass

    label("Function_3_429")

    Call(0, 4)
    Return()

    # Function_3_429 end

    def Function_4_42E(): pass

    label("Function_4_42E")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_5E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_54B")

    ChrTalk(    #0
        0x14,
        (
            "On a completely unrelated note, I heard a strange\x01",
            "loud noise yesterday evening, and I'm still not sure\x01",
            "what it was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x14,
        "I wonder what it could have been.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x14,
        (
            "I can't say I feel quite as safe in this area these\x01",
            "days as I once did, and that's not helping...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E4")

    label("loc_54B")


    ChrTalk(    #3
        0x14,
        "Hello there. Interested in having breakfast here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x14,
        "We're best known for our curry and our coffee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x14,
        "I wholeheartedly recommend them both.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_5E4")

    Jump("loc_602")

    label("loc_5E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_5F1")
    Jump("loc_602")

    label("loc_5F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_5FB")
    Jump("loc_602")

    label("loc_5FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_602")

    label("loc_602")

    TalkEnd(0x14)
    Return()

    # Function_4_42E end

    def Function_5_606(): pass

    label("Function_5_606")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_7EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6F8")

    ChrTalk(    #6
        0xFE,
        (
            "He had connections throughout so many different\x01",
            "industries, too, connecting them all together...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "His death will be a big blow to industry here in\x01",
            "Liberl... I just hope it doesn't have too much of\x01",
            "a major impact.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E8")

    label("loc_6F8")


    ChrTalk(    #8
        0xFE,
        (
            "I was beside myself when I'd read about\x01",
            "Saul Holden's passing in the Liberl News\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "I knew he was well known for being rich,\x01",
            "but I don't remember ever reading his age\x01",
            "anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "I hadn't realized he was that old...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_7E8")

    Jump("loc_806")

    label("loc_7EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_7F5")
    Jump("loc_806")

    label("loc_7F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_7FF")
    Jump("loc_806")

    label("loc_7FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_806")

    label("loc_806")

    TalkEnd(0xFE)
    Return()

    # Function_5_606 end

    def Function_6_80A(): pass

    label("Function_6_80A")

    Call(0, 7)
    Return()

    # Function_6_80A end

    def Function_7_80F(): pass

    label("Function_7_80F")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_81C")
    Jump("loc_A83")

    label("loc_81C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_8F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_866")

    ChrTalk(    #11
        0x16,
        "Hello there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x16,
        "Why not stay and have lunch here?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8F5")

    label("loc_866")


    ChrTalk(    #13
        0x16,
        "Hello there! Welcome to the Sunnybell Inn.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x16,
        "Why not try our new menu item, bouillabaisse?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x16,
        "I'm sure you won't be disappointed!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_8F5")

    Jump("loc_A83")

    label("loc_8F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_902")
    Jump("loc_A83")

    label("loc_902")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_A83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9A5")

    ChrTalk(    #16
        0x16,
        (
            "I feel like there are a lot more tourists coming\x01",
            "to Grancel lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x16,
        (
            "That's no bad thing, either. It makes the city \x01",
            "that much livelier!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A83")

    label("loc_9A5")


    ChrTalk(    #18
        0x16,
        (
            "We seem to be getting a lot of customers from \x01",
            "other countries here lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x16,
        (
            "Heehee. I suppose they must all be coming here\x01",
            "on vacation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x16,
        (
            "I certainly don't mind. It's always nice when this\x01",
            "place is lively.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A83")

    TalkEnd(0x16)
    Return()

    # Function_7_80F end

    def Function_8_A87(): pass

    label("Function_8_A87")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_A94")
    Jump("loc_E48")

    label("loc_A94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_C35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_B6F")

    ChrTalk(    #21
        0xFE,
        (
            "I saw a really suspicious group of men wearing\x01",
            "black suits in front of Grancel Castle earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I wonder what they were doing there? I can't say,\x01",
            "but I get the feeling they were up to no good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C32")

    label("loc_B6F")


    ChrTalk(    #23
        0xFE,
        (
            "I saw a really suspicious group in front of\x01",
            "Grancel Castle earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "I've got no idea who they were, either...\x01",
            "They were all wearing black suits is about\x01",
            "as much as I could tell you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_C32")

    Jump("loc_E48")

    label("loc_C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_C3F")
    Jump("loc_E48")

    label("loc_C3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_E48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D1F")

    ChrTalk(    #25
        0xFE,
        (
            "It feels like a lot of people have already forgotten\x01",
            "the Hundred Days War, even though it was only a\x01",
            "few short years ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Still...maybe trying to forget painful memories\x01",
            "is the best thing to do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E48")

    label("loc_D1F")


    ChrTalk(    #27
        0xFE,
        (
            "It feels like people are already beginning to\x01",
            "forget the war that we all endured...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "It was only mere years ago that we had droves\x01",
            "of evacuees flooding into the city, trying to get\x01",
            "away from the fighting elsewhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "...but it feels like everyone's already forgotten\x01",
            "all of that.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_E48")

    TalkEnd(0xFE)
    Return()

    # Function_8_A87 end

    def Function_9_E4C(): pass

    label("Function_9_E4C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_FC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_EE5")

    ChrTalk(    #30
        0xFE,
        (
            "We'll continue the editorial meeting after Nial\x01",
            "gets back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "He'll probably wander back some time in the\x01",
            "afternoon, I think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC4")

    label("loc_EE5")


    ChrTalk(    #32
        0xFE,
        "I'm off to go and meet with someone in a minute.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "Not just anyone, either! A famous reporter who\x01",
            "once received the Fulitzer Prize.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "It's been a long time since we last met, too.\x01",
            "I can't wait to see the guy.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_FC4")

    Jump("loc_FE2")

    label("loc_FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_FD1")
    Jump("loc_FE2")

    label("loc_FD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_FDB")
    Jump("loc_FE2")

    label("loc_FDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_FE2")

    label("loc_FE2")

    TalkEnd(0xFE)
    Return()

    # Function_9_E4C end

    def Function_10_FE6(): pass

    label("Function_10_FE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_1207")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_10B3")

    ChrTalk(    #35
        0xFE,
        (
            "To write a good article, you need to do more than\x01",
            "gather a dumpload of information and analyze it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "You need to always try to provide a fresh take on\x01",
            "what you're working with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1204")

    label("loc_10B3")


    ChrTalk(    #37
        0xFE,
        "That Nial! He really doesn't seem to understand...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "There's no way we could have printed an article\x01",
            "like that as it stands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "He's just so goodnatured that he seems to have\x01",
            "a habit of getting far too wrapped up in a single\x01",
            "opinion or piece of information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "I'm sure he'll come to understand eventually,\x01",
            "but for now...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1204")

    Jump("loc_1222")

    label("loc_1207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_1211")
    Jump("loc_1222")

    label("loc_1211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_121B")
    Jump("loc_1222")

    label("loc_121B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_1222")

    label("loc_1222")

    TalkEnd(0xFE)
    Return()

    # Function_10_FE6 end

    def Function_11_1226(): pass

    label("Function_11_1226")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_1426")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1307")

    ChrTalk(    #41
        0xFE,
        (
            "I-I just handle the culture section of the paper,\x01",
            "so I've never really had that many run-ins with\x01",
            "them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Poor Nial seems to end up in an argument with\x01",
            "them every time he brings a story, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1423")

    label("loc_1307")


    ChrTalk(    #43
        0xFE,
        (
            "Yesterday's editorial meeting was...a disaster,\x01",
            "to put it lightly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "I can understand how frustrated Nial must\x01",
            "feel, though--he finds some incredible stories,\x01",
            "but they never end up getting printed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "Both Noticia and the editor-in-chief are really\x01",
            "strict with him, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1423")

    Jump("loc_1441")

    label("loc_1426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_1430")
    Jump("loc_1441")

    label("loc_1430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_143A")
    Jump("loc_1441")

    label("loc_143A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_1441")

    label("loc_1441")

    TalkEnd(0xFE)
    Return()

    # Function_11_1226 end

    def Function_12_1445(): pass

    label("Function_12_1445")

    Call(0, 13)
    Return()

    # Function_12_1445 end

    def Function_13_144A(): pass

    label("Function_13_144A")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_1546")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_14BF")

    ChrTalk(    #46
        0x13,
        "Nial still isn't back, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x13,
        (
            "I'm guessing he spent the whole night drinking.\x01",
            "AGAIN.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1543")

    label("loc_14BF")


    ChrTalk(    #48
        0x13,
        "Welcome to the Liberl News Service!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x13,
        (
            "This is reception, while the second floor is the\x01",
            "home of our editorial department.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_1543")

    Jump("loc_1561")

    label("loc_1546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_1550")
    Jump("loc_1561")

    label("loc_1550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_155A")
    Jump("loc_1561")

    label("loc_155A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_1561")

    label("loc_1561")

    TalkEnd(0x13)
    Return()

    # Function_13_144A end

    def Function_14_1565(): pass

    label("Function_14_1565")

    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1614")
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #50
        (
            "\x07\x05The Baral Coffee House's specialty!\x01",
            "[Chef's Curry] - 1000 mira\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #51
        (
            "\x07\x05Try our hot curry, cooked to perfection\x01",
            "with our secret spices!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_16AC")

    label("loc_1614")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #52
        (
            "\x07\x05The Baral Coffee House's specialty!\x01",
            "[Curry of Dreams] - 900 mira\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #53
        (
            "\x07\x05Try our hot curry, cooked to perfection\x01",
            "with our secret spices!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_16AC")

    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_14_1565 end

    def Function_15_16C2(): pass

    label("Function_15_16C2")

    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_175E")
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #54
        (
            "\x07\x05- Menu -\x01",
            "Mixed Cocktail    750 mira\x01",
            "Refreshing Pie    450 mira\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #55
        (
            "\x07\x05- Newly Available -\x01",
            "Bouillabaisse    1000 mira\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F4")

    label("loc_175E")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #56
        (
            "\x07\x05- Menu -\x01",
            "Mocking Pie           400 mira\x01",
            "Tomatrio Sandwich    1400 mira\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #57
        (
            "\x07\x05- Chef's Recommendations -\x01",
            "Seafood Hotpot     1200 mira\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_17F4")

    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_16C2 end

    SaveToFile()

Try(main)
