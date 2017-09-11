from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3310   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3310.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
        'Dodge',                                # 9
        'Radmira',                              # 10
        'Charles',                              # 11
        'Private Brahm',                        # 12
        'Private Henning',                      # 13
        'CWO Pace',                             # 14
        'Warrant Officer Gerwin',               # 15
        'Rufus',                                # 16
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
        'ED6_DT07/CH01140 ._CH',             # 00
        'ED6_DT07/CH01690 ._CH',             # 01
        'ED6_DT07/CH02640 ._CH',             # 02
        'ED6_DT07/CH01300 ._CH',             # 03
        'ED6_DT07/CH01300 ._CH',             # 04
        'ED6_DT07/CH01310 ._CH',             # 05
        'ED6_DT07/CH01300 ._CH',             # 06
        'ED6_DT07/CH01270 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01140P._CP',             # 00
        'ED6_DT07/CH01690P._CP',             # 01
        'ED6_DT07/CH02640P._CP',             # 02
        'ED6_DT07/CH01300P._CP',             # 03
        'ED6_DT07/CH01300P._CP',             # 04
        'ED6_DT07/CH01310P._CP',             # 05
        'ED6_DT07/CH01300P._CP',             # 06
        'ED6_DT07/CH01270P._CP',             # 07
    )

    DeclNpc(
        X                   = -44500,
        Z                   = 0,
        Y                   = 7710,
        Direction           = 82,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    DeclActor(
        TriggerX            = 7230,
        TriggerZ            = 0,
        TriggerY            = 9350,
        TriggerRange        = 400,
        ActorX              = 6990,
        ActorZ              = 1500,
        ActorY              = 11450,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -49710,
        TriggerZ            = 0,
        TriggerY            = 7160,
        TriggerRange        = 400,
        ActorX              = -51810,
        ActorZ              = 1500,
        ActorY              = 6820,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -49710,
        TriggerZ            = 0,
        TriggerY            = 7160,
        TriggerRange        = 400,
        ActorX              = -51810,
        ActorZ              = 1500,
        ActorY              = 6820,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_256",          # 00, 0
        "Function_1_4D3",          # 01, 1
        "Function_2_529",          # 02, 2
        "Function_3_53F",          # 03, 3
        "Function_4_546",          # 04, 4
        "Function_5_B62",          # 05, 5
        "Function_6_B67",          # 06, 6
        "Function_7_16EF",         # 07, 7
        "Function_8_16F4",         # 08, 8
        "Function_9_1B17",         # 09, 9
        "Function_10_24E5",        # 0A, 10
        "Function_11_25DC",        # 0B, 11
        "Function_12_2A73",        # 0C, 12
        "Function_13_2B87",        # 0D, 13
    )


    def Function_0_256(): pass

    label("Function_0_256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_28C")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 6160, 0, 66940, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 11190, 0, 68400, 180)
    Jump("loc_2F7")

    label("loc_28C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_296")
    Jump("loc_2F7")

    label("loc_296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2A0")
    Jump("loc_2F7")

    label("loc_2A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2AA")
    Jump("loc_2F7")

    label("loc_2AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2B4")
    Jump("loc_2F7")

    label("loc_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2BE")
    Jump("loc_2F7")

    label("loc_2BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2C8")
    Jump("loc_2F7")

    label("loc_2C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_2D2")
    Jump("loc_2F7")

    label("loc_2D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2DC")
    Jump("loc_2F7")

    label("loc_2DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2EB")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_2F7")

    label("loc_2EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2F7")
    ClearChrFlags(0x8, 0x80)

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_343")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 11650, 0, 7310, 359)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -51810, 0, 6820, 97)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 6990, 0, 11450, 189)
    Jump("loc_4D2")

    label("loc_343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3A5")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 11650, 0, 7310, 359)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -55630, 0, 9700, 105)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -54180, 0, 9800, 267)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 6990, 0, 11450, 189)
    Jump("loc_4D2")

    label("loc_3A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3DB")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -51810, 0, 6820, 97)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 6990, 0, 11450, 189)
    Jump("loc_4D2")

    label("loc_3DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_427")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 11650, 0, 7310, 359)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -51810, 0, 6820, 97)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 6990, 0, 11450, 189)
    Jump("loc_4D2")

    label("loc_427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_489")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3860, 0, 68230, 108)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3970, 0, 9040, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -51810, 0, 6820, 97)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 6990, 0, 11450, 189)
    Jump("loc_4D2")

    label("loc_489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4D2")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 11650, 0, 7310, 359)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -51810, 0, 6820, 97)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 6990, 0, 11450, 189)

    label("loc_4D2")

    Return()

    # Function_0_256 end

    def Function_1_4D3(): pass

    label("Function_1_4D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_4E1")
    OP_64(0x2, 0x1)
    Jump("loc_528")

    label("loc_4E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_4F3")
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    Jump("loc_528")

    label("loc_4F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_501")
    OP_64(0x2, 0x1)
    Jump("loc_528")

    label("loc_501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_50F")
    OP_64(0x2, 0x1)
    Jump("loc_528")

    label("loc_50F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_51D")
    OP_64(0x1, 0x1)
    Jump("loc_528")

    label("loc_51D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_528")
    OP_64(0x2, 0x1)

    label("loc_528")

    Return()

    # Function_1_4D3 end

    def Function_2_529(): pass

    label("Function_2_529")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_529")

    label("loc_53E")

    Return()

    # Function_2_529 end

    def Function_3_53F(): pass

    label("Function_3_53F")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_3_53F end

    def Function_4_546(): pass

    label("Function_4_546")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_67D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5E4")

    ChrTalk(    #0
        0xFE,
        (
            "Just about time for me to take\x01",
            "over at the gates...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Eh. I'll just wait here like\x01",
            "I always do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "I'll go when Brahm calls me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_67A")

    label("loc_5E4")

    OP_A2(0x4)

    ChrTalk(    #3
        0xFE,
        (
            "I wonder, where did the guys\x01",
            "who attacked the factory\x01",
            "disappear to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "Not even the chief can\x01",
            "figure it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "Not that it's his job to.\x02",
    )

    CloseMessageWindow()

    label("loc_67A")

    Jump("loc_B5E")

    label("loc_67D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_7A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_703")

    ChrTalk(    #6
        0xFE,
        (
            "The chief probably doesn't\x01",
            "agree with our orders either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Of course, he'd never say so.\x01",
            "It's not in him to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_79E")

    label("loc_703")

    OP_A2(0x4)

    ChrTalk(    #8
        0xFE,
        (
            "I don't know from who, but we've\x01",
            "received orders to suspend our\x01",
            "inspections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "It's pretty weird. I can't imagine\x01",
            "what the brass is thinking...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79E")

    Jump("loc_B5E")

    label("loc_7A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_95B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_8CC")

    ChrTalk(    #10
        0xFE,
        (
            "We can watch for the Republic\x01",
            "around the clock if we want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "We need to save our strength\x01",
            "for the time we'll need it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "The chief understands that, \x01",
            "but Warrant Officer Gerwin's pretty\x01",
            "hardheaded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Things have gotten pretty tough\x01",
            "around here ever since he\x01",
            "showed up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_958")

    label("loc_8CC")

    OP_A2(0x4)

    ChrTalk(    #14
        0xFE,
        "There's a trick to it, see?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Save your strength for when\x01",
            "you'll really need it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "That's the kind of place this\x01",
            "garrison is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_958")

    Jump("loc_B5E")

    label("loc_95B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_9BC")

    ChrTalk(    #17
        0xFE,
        "It's not goofing off!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "We still cross all the T's and dot\x01",
            "all the I's.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2F")

    label("loc_9BC")

    OP_A2(0x4)

    ChrTalk(    #19
        0xFE,
        (
            "This is Chief Warrant Officer Pace's\x01",
            "lunchtime, don't you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "That's why he's downstairs\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2F")

    Jump("loc_B5E")

    label("loc_A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_AC7")

    ChrTalk(    #21
        0xFE,
        (
            "I should be out relieving Brahm,\x01",
            "but I'll bet he's out there fast asleep. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "No need for me to go out there\x01",
            "and bother him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5E")

    label("loc_AC7")

    OP_A2(0x4)

    ChrTalk(    #23
        0xFE,
        (
            "Well, guess it's time to go and\x01",
            "relieve Private Brahm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "...No need to rush, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "I'll just wait for him to come call\x01",
            "me out there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5E")

    TalkEnd(0xFE)
    Return()

    # Function_4_546 end

    def Function_5_B62(): pass

    label("Function_5_B62")

    Call(0, 6)
    Return()

    # Function_5_B62 end

    def Function_6_B67(): pass

    label("Function_6_B67")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_C87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_BEB")

    ChrTalk(    #26
        0xD,
        (
            "The orders from HQ don't make\x01",
            "any sense lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xD,
        (
            "Something has got to be going on\x01",
            "behind closed doors.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C84")

    label("loc_BEB")

    OP_A2(0x5)

    ChrTalk(    #28
        0xD,
        (
            "We've just received orders to\x01",
            "re-institute inspections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xD,
        (
            "Why? The terrorist attack is too\x01",
            "far gone, inspections now won't\x01",
            "serve any purpose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C84")

    Jump("loc_16EB")

    label("loc_C87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_EDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_D54")

    ChrTalk(    #30
        0xD,
        (
            "We can't break our orders, though.\x01",
            "So we may as well not waste time\x01",
            "trying to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xD,
        (
            "We will therefore continue to\x01",
            "enforce inspection protocols,\x01",
            "as a tenet of our 'official' security.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED9")

    label("loc_D54")

    OP_A2(0x5)

    ChrTalk(    #32
        0xD,
        (
            "I can sympathize with the lieutenants\x01",
            "doubts, but our orders still stand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xD,
        (
            "We don't break orders. And while\x01",
            "we can't re-institute inspections\x01",
            "on those grounds...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xD,
        "We have other orders as well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xD,
        (
            "We will therefore continue to\x01",
            "enforce inspection protocols,\x01",
            "as a tenet of our 'official' security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xD,
        (
            "We're not going to let anyone\x01",
            "suspicious just walk out of\x01",
            "the country.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED9")

    Jump("loc_16EB")

    label("loc_EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1083")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_F95")

    ChrTalk(    #37
        0xD,
        (
            "Thanks to what happened in Zeiss,\x01",
            "people without VERY good reason\x01",
            "will not be granted passes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xD,
        (
            "I'd rethink things if you're planning\x01",
            "on going to the Republic.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1080")

    label("loc_F95")

    OP_A2(0x5)

    ChrTalk(    #39
        0xD,
        (
            "Thanks to what happened in Zeiss,\x01",
            "people without VERY good reason\x01",
            "will not be granted passes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xD,
        (
            "I'd rethink things if you're planning\x01",
            "on going to the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xD,
        (
            "The attack was a huge deal, and\x01",
            "it's slowing down customs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1080")

    Jump("loc_16EB")

    label("loc_1083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1262")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1167")

    ChrTalk(    #42
        0xD,
        (
            "Warrant Officer Gerwin's being\x01",
            " something of a...problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xD,
        (
            "Of course, people like him rush\x01",
            "into things and end up causing\x01",
            "extra problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xD,
        (
            "Hopefully he'll notice that about\x01",
            "himself while he's here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125F")

    label("loc_1167")

    OP_A2(0x5)

    ChrTalk(    #45
        0xD,
        (
            "*sigh* Warrant Officer Gerwin's\x01",
            "being something of a...problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xD,
        (
            "He's a motivated and loyal soldier,\x01",
            "but he hasn't learned an important\x01",
            "lesson yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xD,
        (
            "It's that people who rush into\x01",
            "things end up causing a\x01",
            "boatload of extra problems.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_125F")

    Jump("loc_16EB")

    label("loc_1262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1436")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_133E")

    ChrTalk(    #48
        0xD,
        (
            "This area is full of people who\x01",
            "moved from the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xD,
        (
            "Take our bartender Rufus. \x01",
            "He's from the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xD,
        (
            "I'd prefer it if we were able to\x01",
            "live in peace with the Republic,\x01",
            "side-by-side.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1433")

    label("loc_133E")

    OP_A2(0x5)

    ChrTalk(    #51
        0xD,
        (
            "Most travelers coming through\x01",
            "here are merchants moving\x01",
            "between Liberl and the Republic. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xD,
        (
            "There may be transit ships for\x01",
            "travel between us, but using\x01",
            "them is pretty expensive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xD,
        (
            "A large number of people cross\x01",
            "the border on foot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1433")

    Jump("loc_16EB")

    label("loc_1436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_16EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_15AF")

    ChrTalk(    #54
        0xD,
        (
            "Our biggest duty here is not to\x01",
            "make unnecessary waves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xD,
        (
            "Since relations are so strained with the Empire\x01",
            "right now, we simply can't afford to jeopardize\x01",
            "our relationship with the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xD,
        (
            "So there's an understanding\x01",
            "that my troops are to keep\x01",
            "our presence...relaxed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xD,
        (
            "It ends up making this place\x01",
            "quite the cushy assignment!\x01",
            "Ha ha ha ha ha!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16EB")

    label("loc_15AF")

    OP_A2(0x5)

    ChrTalk(    #58
        0xD,
        "Welcome to the end of the road.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xD,
        (
            "We at the Wolf Fort are charged \x01",
            "with protecting our border\x01",
            "with the Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xD,
        (
            "Since we're talking about the Republic though, \x01",
            "our definition of 'protect' is a little different\x01",
            "from, say, the base at the Haken Gate.  \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xD,
        "It's more like...'keep an eye on.'\x02",
    )

    CloseMessageWindow()

    label("loc_16EB")

    TalkEnd(0xD)
    Return()

    # Function_6_B67 end

    def Function_7_16EF(): pass

    label("Function_7_16EF")

    Call(0, 8)
    Return()

    # Function_7_16EF end

    def Function_8_16F4(): pass

    label("Function_8_16F4")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1895")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1795")

    ChrTalk(    #62
        0xE,
        (
            "Sir! Please give the order to\x01",
            "re-open inspections!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xE,
        (
            "Every minute we wait, we give\x01",
            "those criminals another chance\x01",
            "to escape justice!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1892")

    label("loc_1795")

    OP_A2(0x6)

    ChrTalk(    #64
        0xE,
        (
            "The chief's questioned the order\x01",
            "to suspend inspections himself,\x01",
            "when he heard them. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xE,
        (
            "And when such an order comes\x01",
            "without any news of the terrorists'\x01",
            "apprehension...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xE,
        (
            "...how are we supposed to inspire\x01",
            "morale in the troops?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 400)
    SetChrFlags(0xE, 0x10)

    label("loc_1892")

    Jump("loc_1B13")

    label("loc_1895")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1B13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_19A3")

    ChrTalk(    #67
        0xE,
        (
            "Any resulting negligence of duty\x01",
            "is the responsibility of the\x01",
            "commanding officer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xE,
        (
            "It's my unofficial opinion that\x01",
            "the chief should reassess\x01",
            "his line of thinking...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xE,
        (
            "But in the end he's the one\x01",
            "to assume responsibility. \x01",
            "My hands are tied.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B13")

    label("loc_19A3")

    OP_A2(0x6)

    ChrTalk(    #70
        0xE,
        (
            "Any reports of negligence on the\x01",
            "soldiers' parts is the chief's\x01",
            "responsibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xE,
        (
            "Chief Warrant Officer Pace\x01",
            " doesn't reprimand the troops because\x01",
            "of his laissez-faire attitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xE,
        (
            "I've tried to bring it up with him,\x01",
            "but I was told my thoughts\x01",
            "would be...'duly noted.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xE,
        (
            "Well, the responsibility is\x01",
            "his to shoulder. I can't do anything\x01",
            "more than that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B13")

    TalkEnd(0xE)
    Return()

    # Function_8_16F4 end

    def Function_9_1B17(): pass

    label("Function_9_1B17")

    TalkBegin(0xF)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Rest\x01",       # 2
            "Leave\x01",      # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B7C")
    OP_0D()
    OP_A9(0x48)
    OP_56(0x0)
    TalkEnd(0xF)
    Return()

    label("loc_1B7C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B95")
    OP_0D()
    OP_A9(0x47)
    OP_56(0x0)
    TalkEnd(0xF)
    Return()

    label("loc_1B95")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BA6")
    TalkEnd(0xF)
    Return()

    label("loc_1BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1C76")

    ChrTalk(    #74
        0xF,
        "Hey, did you hear?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xF,
        (
            "They say that the people who\x01",
            "attacked the central factory\x01",
            "haven't been caught yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xF,
        (
            "I have to wonder what the \x01",
            "military has been doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xF,
        "Maybe I'll skip dinner.\x02",
    )

    CloseMessageWindow()
    Jump("loc_24E1")

    label("loc_1C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1E29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1D68")

    ChrTalk(    #78
        0xF,
        (
            "I'm glad the inspections are\x01",
            "finished...but what happened\x01",
            "with those terrorists?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xF,
        (
            "I had a special meal all planned out\x01",
            "to commemorate their arrest, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xF,
        (
            "No matter. I'll just save the idea\x01",
            "for some other time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E26")

    label("loc_1D68")

    OP_A2(0x7)

    ChrTalk(    #81
        0xF,
        (
            "Whew. The inspections have been\x01",
            "suspended. What a relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xF,
        (
            "I haven't heard what happened to\x01",
            "that gang of terrorists...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xF,
        (
            "But I'm sure the Royal Army did\x01",
            "something about them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E26")

    Jump("loc_24E1")

    label("loc_1E29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1FC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1ED8")

    ChrTalk(    #84
        0xF,
        (
            "I hope they catch those terrorists\x01",
            "quickly so things can go back to\x01",
            "normal here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xF,
        (
            "If they don't I'm going to have\x01",
            "to raise prices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xF,
        "Ha ha ha ha!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FC6")

    label("loc_1ED8")

    OP_A2(0x7)

    ChrTalk(    #87
        0xF,
        (
            "I heard about what happened in\x01",
            "Zeiss. How terrible for everyone\x01",
            "living there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xF,
        (
            "But still, you've got to be more\x01",
            "than 60% brass to hit the\x01",
            "central factory like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xF,
        (
            "Whoever they are, they can't\x01",
            "just be some petty crooks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC6")

    Jump("loc_24E1")

    label("loc_1FC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_21AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_20BE")

    ChrTalk(    #90
        0xF,
        (
            "This guy came to my shop to\x01",
            "have something to eat...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xF,
        "...and boy, could he eat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xF,
        (
            "He ate up almost all my stock,\x01",
            "and that night, nobody but the\x01",
            "chief got any meals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xF,
        (
            "Ha ha ha! I hope he drops by\x01",
            "again someday...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21AC")

    label("loc_20BE")

    OP_A2(0x7)

    ChrTalk(    #94
        0xF,
        (
            "And once there was this one time,\x01",
            "when this HUGE guy came in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xF,
        (
            "He was dressed like he came from\x01",
            "the Republic, but his appetite HAD\x01",
            "to be from Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xF,
        (
            "With a body like his you could\x01",
            "literally call him a 'monster' of\x01",
            "a man.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21AC")

    Jump("loc_24E1")

    label("loc_21AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2314")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_227B")

    ChrTalk(    #97
        0xF,
        (
            "In my younger days, I wanted\x01",
            "to be a big shot septium trader\x01",
            "and build up my own harem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xF,
        (
            "But here I am, running this old\x01",
            "hole-in-the-wall bar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xF,
        "No regrets though...ha ha ha!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2311")

    label("loc_227B")

    OP_A2(0x7)

    ChrTalk(    #100
        0xF,
        "I'm from the Republic myself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xF,
        (
            "Maybe that figures into the karma\x01",
            "that pushed me into this old dump\x01",
            "of a bar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xF,
        "Some life, right? Ha!\x02",
    )

    CloseMessageWindow()

    label("loc_2311")

    Jump("loc_24E1")

    label("loc_2314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_24E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_23D8")

    ChrTalk(    #103
        0xF,
        (
            "Welcome to Jack & Squat's Pub!\x01",
            "I'm Rufus. I'm afraid both of the\x01",
            "proprietors stepped out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xF,
        (
            "We can whip you up anything in\x01",
            "the back as long as it's liquor\x01",
            "or breakfast.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24E1")

    label("loc_23D8")

    OP_A2(0x7)

    ChrTalk(    #105
        0xF,
        (
            "Hello! Welcome to Jack & Squat's Pub!\x01",
            "As the name implies, we ain't got much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xF,
        (
            "Sadly, both of the owners are out\x01",
            "of town right now...heh. That's my\x01",
            "little joke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xF,
        (
            "Anyway, we have cheap rooms\x01",
            "and plenty of space, so come\x01",
            "right in and get comfortable!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24E1")

    TalkEnd(0xF)
    Return()

    # Function_9_1B17 end

    def Function_10_24E5(): pass

    label("Function_10_24E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_25D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2547")
    TurnDirection(0xFE, 0xA, 400)

    ChrTalk(    #108
        0xFE,
        "Charles!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "We'll be leaving soon, so get\x01",
            "your things together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D8")

    label("loc_2547")

    OP_A2(0x1)

    ChrTalk(    #110
        0xFE,
        (
            "All right. Time to go get our travel\x01",
            "passes in order...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "We've got to leave early in the\x01",
            "morning tomorrow. Calvard's a\x01",
            "long way off.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25D8")

    TalkEnd(0xFE)
    Return()

    # Function_10_24E5 end

    def Function_11_25DC(): pass

    label("Function_11_25DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2A6F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2980")
    OP_A2(0x583)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #112
        0xFE,
        "Hey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "Hey. Long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x102,
        (
            "#014F...?\x02\x03",

            "#010FAh, hey.\x01",
            "It HAS been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        "#501FWho's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x102,
        (
            "#010FYou remember that kid who was\x01",
            "looking for that piece of quartz in\x01",
            "Rolent, don't you?\x02\x03",

            "Remember? We took a request\x01",
            "to find it a while back.\x02\x03",

            "Are you on your way back to\x01",
            "the Republic now?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #117
        0xFE,
        "Yeah, pretty much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        "But I'll be back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "When my sisters get bigger,\x01",
            "I'm totally moving to Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "I'm going to get into the central\x01",
            "factory, start at the bottom, and\x01",
            "learn to build airships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "I'm good with my hands, so my\x01",
            "mom ought to understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#000FWow...\x02\x03",

            "Good for you! That's a pretty\x01",
            "big ambition!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "No kidding. I got my whole\x01",
            "life ahead of me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "Well, I should get back to\x01",
            "helping out my mom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "I got four little sisters, you know.\x01",
            "Real little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#006FOkay, then.\x01",
            "Good luck!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #127
        0xFE,
        "Yeah, whatever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "Good luck to you guys, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A6F")

    label("loc_2980")


    ChrTalk(    #129
        0xFE,
        (
            "Y'know, once my sisters get\x01",
            "a little bigger, I'm getting out\x01",
            "of this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "I'm going to get into the central\x01",
            "factory, start at the bottom, and\x01",
            "learn to build airships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "I'm good with my hands, so my\x01",
            "mom ought to understand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A6F")

    TalkEnd(0xFE)
    Return()

    # Function_11_25DC end

    def Function_12_2A73(): pass

    label("Function_12_2A73")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2B0A")

    ChrTalk(    #132
        0xFE,
        (
            "I tried to choose my outfit so\x01",
            "I'd look more like I was from\x01",
            "Liberl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "What do you think?\x01",
            "Do I look 'Liberl' enough?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B83")

    label("loc_2B0A")

    OP_A2(0x0)

    ChrTalk(    #134
        0xFE,
        (
            "So yeah, Liberl's like a stone's\x01",
            "throw away, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "I'm practically at Zeiss' front door!\x01",
            "This is so great!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B83")

    TalkEnd(0xFE)
    Return()

    # Function_12_2A73 end

    def Function_13_2B87(): pass

    label("Function_13_2B87")

    Call(0, 9)
    Return()

    # Function_13_2B87 end

    SaveToFile()

Try(main)
