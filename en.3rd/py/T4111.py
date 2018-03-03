from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4111   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4111.x',
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
        'Katrina',                              # 9
        'Dalia',                                # 10
        'Irving',                               # 11
        'Rachel',                               # 12
        'Martin',                               # 13
        'Marian',                               # 14
        'Helena',                               # 15
        'Norche',                               # 16
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
        'ED6_DT07/CH01220 ._CH',             # 00
        'ED6_DT07/CH01230 ._CH',             # 01
        'ED6_DT07/CH01020 ._CH',             # 02
        'ED6_DT07/CH01210 ._CH',             # 03
        'ED6_DT07/CH02490 ._CH',             # 04
        'ED6_DT07/CH01180 ._CH',             # 05
        'ED6_DT07/CH01350 ._CH',             # 06
        'ED6_DT07/CH01480 ._CH',             # 07
        'ED6_DT07/CH01220 ._CH',             # 08
        'ED6_DT07/CH01150 ._CH',             # 09
        'ED6_DT07/CH02730 ._CH',             # 0A
        'ED6_DT26/CH20687 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH01220P._CP',             # 00
        'ED6_DT07/CH01230P._CP',             # 01
        'ED6_DT07/CH01020P._CP',             # 02
        'ED6_DT07/CH01210P._CP',             # 03
        'ED6_DT07/CH02490P._CP',             # 04
        'ED6_DT07/CH01180P._CP',             # 05
        'ED6_DT07/CH01350P._CP',             # 06
        'ED6_DT07/CH01480P._CP',             # 07
        'ED6_DT07/CH01220P._CP',             # 08
        'ED6_DT07/CH01150P._CP',             # 09
        'ED6_DT07/CH02730P._CP',             # 0A
        'ED6_DT26/CH20687P._CP',             # 0B
    )

    DeclNpc(
        X                   = 6600,
        Z                   = 0,
        Y                   = -55460,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 6600,
        Z                   = 0,
        Y                   = -56390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -3550,
        Z                   = 0,
        Y                   = 68290,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -5000,
        Z                   = -100,
        Y                   = 68700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 115690,
        Z                   = 0,
        Y                   = 60750,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 113990,
        Z                   = 0,
        Y                   = -55210,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 114980,
        Z                   = 0,
        Y                   = -55400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 57440,
        Z                   = 0,
        Y                   = 2570,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )


    DeclActor(
        TriggerX            = -5000,
        TriggerZ            = 0,
        TriggerY            = 68840,
        TriggerRange        = 1000,
        ActorX              = -4840,
        ActorZ              = 1200,
        ActorY              = 68840,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_22E",          # 00, 0
        "Function_1_268",          # 01, 1
        "Function_2_286",          # 02, 2
        "Function_3_2AA",          # 03, 3
        "Function_4_2CE",          # 04, 4
        "Function_5_2F2",          # 05, 5
        "Function_6_48B",          # 06, 6
        "Function_7_59F",          # 07, 7
        "Function_8_662",          # 08, 8
        "Function_9_7EA",          # 09, 9
        "Function_10_9F8",         # 0A, 10
        "Function_11_B27",         # 0B, 11
        "Function_12_C30",         # 0C, 12
    )


    def Function_0_22E(): pass

    label("Function_0_22E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_267")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)

    label("loc_267")

    Return()

    # Function_0_22E end

    def Function_1_268(): pass

    label("Function_1_268")

    OP_B1("t4111_n")
    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_285")
    OP_65(0x0, 0x1)

    label("loc_285")

    Return()

    # Function_1_268 end

    def Function_2_286(): pass

    label("Function_2_286")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A9")
    OP_8D(0xFE, 113830, 62500, 117900, 58880, 2000)
    Jump("Function_2_286")

    label("loc_2A9")

    Return()

    # Function_2_286 end

    def Function_3_2AA(): pass

    label("Function_3_2AA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CD")
    OP_8D(0xFE, -1150, 59690, -3770, 62520, 3000)
    Jump("Function_3_2AA")

    label("loc_2CD")

    Return()

    # Function_3_2AA end

    def Function_4_2CE(): pass

    label("Function_4_2CE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F1")
    OP_8D(0xFE, 56680, 3500, 58350, 1840, 2000)
    Jump("Function_4_2CE")

    label("loc_2F1")

    Return()

    # Function_4_2CE end

    def Function_5_2F2(): pass

    label("Function_5_2F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_46C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3BB")

    ChrTalk(    #0
        0xFE,
        (
            "At times like these, the worst thing you can\x01",
            "do is go to pieces and lose your composure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "It's no real surprise why young people do,\x01",
            "of course. I can certainly understand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_469")

    label("loc_3BB")


    ChrTalk(    #2
        0xFE,
        "Rachel's in her final month of pregnancy now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "My husband should be coming over from Haken\x01",
            "Gate any day now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "Heehee! I can hardly wait to see my grandchild.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_469")

    Jump("loc_487")

    label("loc_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_476")
    Jump("loc_487")

    label("loc_476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_480")
    Jump("loc_487")

    label("loc_480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_487")

    label("loc_487")

    TalkEnd(0xFE)
    Return()

    # Function_5_2F2 end

    def Function_6_48B(): pass

    label("Function_6_48B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_580")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_52D")

    ChrTalk(    #5
        0xFE,
        (
            "My wife's currently pregnant, and the baby is\x01",
            "due relatively soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "So right now, I just want to be by her side as\x01",
            "much as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57D")

    label("loc_52D")

    OP_8C(0xFE, 270, 0)

    ChrTalk(    #7
        0xFE,
        "You've got nothing to worry about.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "I'm right here with you.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_57D")

    Jump("loc_59B")

    label("loc_580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_58A")
    Jump("loc_59B")

    label("loc_58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_594")
    Jump("loc_59B")

    label("loc_594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_59B")

    label("loc_59B")

    TalkEnd(0xFE)
    Return()

    # Function_6_48B end

    def Function_7_59F(): pass

    label("Function_7_59F")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_643")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5F5")

    ChrTalk(    #9
        0x13,
        (
            "Oh, Goddess... Please bestow your blessings\x01",
            "upon my child...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_640")

    label("loc_5F5")


    ChrTalk(    #10
        0x13,
        "Yes... Yes... I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x13,
        "I'm sure everything will be fine.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_640")

    Jump("loc_65E")

    label("loc_643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_64D")
    Jump("loc_65E")

    label("loc_64D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_657")
    Jump("loc_65E")

    label("loc_657")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_65E")

    label("loc_65E")

    TalkEnd(0x13)
    Return()

    # Function_7_59F end

    def Function_8_662(): pass

    label("Function_8_662")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_7CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6FB")

    ChrTalk(    #12
        0xFE,
        "Umm... Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "I-I can't think of anything at all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "I'm so useless...and at a time when my help's\x01",
            "needed the most, too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C8")

    label("loc_6FB")


    ChrTalk(    #15
        0xFE,
        "Wh-What should I do, though?\x02",
    )

    CloseMessageWindow()
    OP_4A(0x10, 255)
    TurnDirection(0x10, 0xFE, 500)
    Sleep(300)

    ChrTalk(    #16
        0x10,
        "First, you need to try and calm down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "How about starting by giving some thought\x01",
            "on what to call the baby?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "Wh-What to call it?\x02",
    )

    CloseMessageWindow()
    OP_4B(0x10, 255)
    OP_8C(0x10, 90, 0)
    OP_A2(0x1)

    label("loc_7C8")

    Jump("loc_7E6")

    label("loc_7CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_7D5")
    Jump("loc_7E6")

    label("loc_7D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_7DF")
    Jump("loc_7E6")

    label("loc_7DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_7E6")

    label("loc_7E6")

    TalkEnd(0xFE)
    Return()

    # Function_8_662 end

    def Function_9_7EA(): pass

    label("Function_9_7EA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_9D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_862")

    ChrTalk(    #19
        0xFE,
        (
            "The queen's birthday isn't for another five \x01",
            "months, either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "What am I supposed to do?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D6")

    label("loc_862")


    ChrTalk(    #21
        0xFE,
        "H-Hey, you two!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "You don't know of any exciting events around\x01",
            "this time of year, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "Anything will do! Even your birthdays\x01",
            "will be good enough if it comes down\x01",
            "to it! I. MUST. CELEBRATE.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x103,
        "#1640FI've had mine already.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x151,
        "#1651FMine isn't for a while, I'm afraid...\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #26
        0xFE,
        "O-Oh, right... Sorry for troubling you, then...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_9D6")

    Jump("loc_9F4")

    label("loc_9D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_9E3")
    Jump("loc_9F4")

    label("loc_9E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_9ED")
    Jump("loc_9F4")

    label("loc_9ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_9F4")

    label("loc_9F4")

    TalkEnd(0xFE)
    Return()

    # Function_9_7EA end

    def Function_10_9F8(): pass

    label("Function_10_9F8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_B08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_A4B")

    ChrTalk(    #27
        0xFE,
        (
            "My husband always ends up like this at this\x01",
            "time of year.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B05")

    label("loc_A4B")


    ChrTalk(    #28
        0xFE,
        (
            "He always needs some kind of event to enjoy or\x01",
            "look forward to in the near future, or he goes\x01",
            "bonkers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "Maybe I'll have to make up some kind of occasion\x01",
            "for us to celebrate.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_B05")

    Jump("loc_B23")

    label("loc_B08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_B12")
    Jump("loc_B23")

    label("loc_B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_B1C")
    Jump("loc_B23")

    label("loc_B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_B23")

    label("loc_B23")

    TalkEnd(0xFE)
    Return()

    # Function_10_9F8 end

    def Function_11_B27(): pass

    label("Function_11_B27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_C11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_BB2")
    OP_8C(0xFE, 0, 0)

    ChrTalk(    #30
        0xFE,
        (
            "Mommy, are you sure you shouldn't do something\x01",
            "about him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "Doesn't he need 'restraining' or something?\x02",
    )

    CloseMessageWindow()
    Jump("loc_C0E")

    label("loc_BB2")


    ChrTalk(    #32
        0xFE,
        "Daddy's really high up at a super big company!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "...He just doesn't act like it.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_C0E")

    Jump("loc_C2C")

    label("loc_C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_C1B")
    Jump("loc_C2C")

    label("loc_C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_C25")
    Jump("loc_C2C")

    label("loc_C25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_C2C")

    label("loc_C2C")

    TalkEnd(0xFE)
    Return()

    # Function_11_B27 end

    def Function_12_C30(): pass

    label("Function_12_C30")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_DA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_CC0")

    ChrTalk(    #34
        0xFE,
        (
            "My husband never comes home before midnight.\x01",
            "Never.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "It's quite obvious he doesn't care about me\x01",
            "in the slightest!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA1")

    label("loc_CC0")


    ChrTalk(    #36
        0xFE,
        (
            "My husband barely spends any time in the\x01",
            "house at all. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "On days when he has work, he's out doing that\x01",
            "until past midnight. On days he doesn't, he's out\x01",
            "messing around instead!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "I can't take any more of this!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_DA1")

    Jump("loc_DBF")

    label("loc_DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_DAE")
    Jump("loc_DBF")

    label("loc_DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_DB8")
    Jump("loc_DBF")

    label("loc_DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_DBF")

    label("loc_DBF")

    TalkEnd(0xFE)
    Return()

    # Function_12_C30 end

    SaveToFile()

Try(main)
