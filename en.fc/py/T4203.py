from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4203   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4203.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        'Private Dan',                          # 9
        'Private Aluts',                        # 10
        'Duke Dunan',                           # 11
        'Butler Phillip',                       # 12
        'Special Ops Soldier',                  # 13
        'Special Ops Soldier',                  # 14
        'Carna',                                # 15
        'Anelace',                              # 16
        'Grant',                                # 17
        'Kurt',                                 # 18
        'Lt. Schwarz',                          # 19
        'Royal Guardsman',                      # 20
        'Royal Guardsman',                      # 21
        'Royal Guardsman',                      # 22
        'Royal Guardsman',                      # 23
        'Royal Guardsman',                      # 24
        'Royal Guardsman',                      # 25
        'Royal Guardsman',                      # 26
        'Royal Guardsman',                      # 27
        'Cassius',                              # 28
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
        'ED6_DT07/CH01300 ._CH',             # 00
        'ED6_DT07/CH02140 ._CH',             # 01
        'ED6_DT07/CH02470 ._CH',             # 02
        'ED6_DT07/CH01330 ._CH',             # 03
        'ED6_DT07/CH00401 ._CH',             # 04
        'ED6_DT07/CH00421 ._CH',             # 05
        'ED6_DT07/CH00391 ._CH',             # 06
        'ED6_DT07/CH00411 ._CH',             # 07
        'ED6_DT07/CH02090 ._CH',             # 08
        'ED6_DT07/CH00321 ._CH',             # 09
        'ED6_DT07/CH02000 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01300P._CP',             # 00
        'ED6_DT07/CH02140P._CP',             # 01
        'ED6_DT07/CH02470P._CP',             # 02
        'ED6_DT07/CH01330P._CP',             # 03
        'ED6_DT07/CH00401P._CP',             # 04
        'ED6_DT07/CH00421P._CP',             # 05
        'ED6_DT07/CH00391P._CP',             # 06
        'ED6_DT07/CH00411P._CP',             # 07
        'ED6_DT07/CH02090P._CP',             # 08
        'ED6_DT07/CH00321P._CP',             # 09
        'ED6_DT07/CH02000P._CP',             # 0A
    )

    DeclNpc(
        X                   = -790,
        Z                   = 0,
        Y                   = 41980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 950,
        Z                   = 0,
        Y                   = 41980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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


    DeclEvent(
        X                   = -5630,
        Y                   = -1000,
        Z                   = 30090,
        Range               = 6050,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x69BE,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )


    ScpFunction(
        "Function_0_3A2",          # 00, 0
        "Function_1_494",          # 01, 1
        "Function_2_4B3",          # 02, 2
        "Function_3_525",          # 03, 3
        "Function_4_598",          # 04, 4
        "Function_5_F28",          # 05, 5
        "Function_6_170D",         # 06, 6
        "Function_7_2F82",         # 07, 7
        "Function_8_3CF6",         # 08, 8
        "Function_9_418E",         # 09, 9
        "Function_10_4245",        # 0A, 10
        "Function_11_5362",        # 0B, 11
    )


    def Function_0_3A2(): pass

    label("Function_0_3A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_3B0")
    OP_A3(0x3FA)
    Event(0, 8)

    label("loc_3B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_3BE")
    OP_A3(0x3FB)
    Event(0, 9)

    label("loc_3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_3CC")
    OP_A3(0x3FC)
    Event(0, 10)

    label("loc_3CC")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_3DC"),
        (101, "loc_3DC"),
        (SWITCH_DEFAULT, "loc_3F2"),
    )


    label("loc_3DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EF")
    OP_A2(0x60B)
    Event(0, 6)

    label("loc_3EF")

    Jump("loc_3F2")

    label("loc_3F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3FC")
    Jump("loc_493")

    label("loc_3FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_43C")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, -790, 0, 41980, 180)
    SetChrPos(0xD, 950, 0, 41980, 180)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_493")

    label("loc_43C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_446")
    Jump("loc_493")

    label("loc_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_450")
    Jump("loc_493")

    label("loc_450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_45A")
    Jump("loc_493")

    label("loc_45A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_464")
    Jump("loc_493")

    label("loc_464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_46E")
    Jump("loc_493")

    label("loc_46E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_478")
    Jump("loc_493")

    label("loc_478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_482")
    Jump("loc_493")

    label("loc_482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_48C")
    Jump("loc_493")

    label("loc_48C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_493")

    label("loc_493")

    Return()

    # Function_0_3A2 end

    def Function_1_494(): pass

    label("Function_1_494")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE4A80, 0x30060)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 450)
    Return()

    # Function_1_494 end

    def Function_2_4B3(): pass

    label("Function_2_4B3")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        (
            "Grancel Castle is totally locked\x01",
            "down right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "We're under orders not to allow\x01",
            "ANYONE to pass.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_2_4B3 end

    def Function_3_525(): pass

    label("Function_3_525")

    TalkBegin(0xFE)

    ChrTalk(    #2
        0xFE,
        (
            "So you're the bracers who won\x01",
            "the tournament, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "The banquet is over. Go back to\x01",
            "the guild.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_525 end

    def Function_4_598(): pass

    label("Function_4_598")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_75E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_649")

    ChrTalk(    #4
        0xFE,
        (
            "I never believed Lt. Schwarz\x01",
            "could be a terrorist...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "And I'm just as convinced now that\x01",
            "Colonel Richard can't possibly be\x01",
            "the one behind the coup.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75B")

    label("loc_649")

    OP_A2(0x0)

    ChrTalk(    #6
        0xFE,
        (
            "I never believed Lt. Schwarz\x01",
            "could be a terrorist...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "And I'm just as convinced now that\x01",
            "Colonel Richard can't possibly be\x01",
            "the one behind the coup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I mean, the facts are the facts...but\x01",
            "it just seems so surreal to me. How\x01",
            "could a man like that fall so far?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75B")

    Jump("loc_F24")

    label("loc_75E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_768")
    Jump("loc_F24")

    label("loc_768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_7A6")

    ChrTalk(    #9
        0xFE,
        (
            "So, did you enjoy your look\x01",
            "around the castle?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F24")

    label("loc_7A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_821")

    ChrTalk(    #10
        0xFE,
        (
            "Welcome to Her Majesty's fabulous\x01",
            "Grancel Castle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "There should be a guide waiting\x01",
            "for you just inside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F24")

    label("loc_821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_8D2")

    ChrTalk(    #12
        0xFE,
        (
            "I wonder what Lt. Schwarz\x01",
            "is doing right now...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "I've always enjoyed seeing her each\x01",
            "day, even if we did speak little more\x01",
            "than pleasantries to one another.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F24")

    label("loc_8D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_A35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_972")

    ChrTalk(    #14
        0xFE,
        (
            "Apparently, our security duties in\x01",
            "the city are to be much more rigorous\x01",
            "from here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "We'll be under Captain Amalthea's\x01",
            "orders.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A32")

    label("loc_972")

    OP_A2(0x0)

    ChrTalk(    #16
        0xFE,
        (
            "Apparently, our security duties in\x01",
            "the city are to be much more rigorous\x01",
            "from here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "We'll be under Captain Amalthea's\x01",
            "orders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Colonel Richard certainly is a\x01",
            "busy man!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A32")

    Jump("loc_F24")

    label("loc_A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_AD3")

    ChrTalk(    #19
        0xFE,
        (
            "The Special Ops team is racking\x01",
            "up the wins at the tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I wish they'd concentrate on finding\x01",
            "the Royal Guardsmen, though, instead!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F24")

    label("loc_AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_C81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B9F")

    ChrTalk(    #21
        0xFE,
        (
            "Colonel Richard's barely been\x01",
            "seen outside the castle since\x01",
            "Her Majesty fell ill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "...I've heard, too, that the core\x01",
            "of the Intelligence Division has\x01",
            "been moved into the castle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7E")

    label("loc_B9F")

    OP_A2(0x0)

    ChrTalk(    #23
        0xFE,
        (
            "Colonel Richard certainly is a\x01",
            "busy man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "He's barely been seen outside\x01",
            "the castle since Her Majesty\x01",
            "fell ill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "...I've heard, too, that the core\x01",
            "of the Intelligence Division has\x01",
            "been moved into the castle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7E")

    Jump("loc_F24")

    label("loc_C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_D58")

    ChrTalk(    #26
        0xFE,
        (
            "I respect Colonel Richard, don't\x01",
            "get me wrong, but those Special\x01",
            "Ops guys...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "They're good at what they do, but they\x01",
            "make people uncomfortable in the process.\x01",
            "Even the army's creeped out by them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F24")

    label("loc_D58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_E0C")

    ChrTalk(    #28
        0xFE,
        (
            "Colonel Richard is truly an\x01",
            "impressive individual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "Thanks to his popularity a large number\x01",
            "of soldiers have requested transfers into\x01",
            "the Intelligence Division.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F24")

    label("loc_E0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_F24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_EC8")

    ChrTalk(    #30
        0xFE,
        (
            "I know it sucks that you can't\x01",
            "enter the castle right now...\x01",
            "but cheer up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "There's lots to see in this\x01",
            "city--the castle is just one\x01",
            "of many tourist attractions!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F24")

    label("loc_EC8")


    ChrTalk(    #32
        0xFE,
        "Just a moment, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "I'm sorry, but entry to the\x01",
            "castle is strictly prohibited.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F24")

    TalkEnd(0xFE)
    Return()

    # Function_4_598 end

    def Function_5_F28(): pass

    label("Function_5_F28")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_100F")

    ChrTalk(    #34
        0xFE,
        (
            "I was shocked when I found out the Intelligence\x01",
            "Division was behind the coup, and they planned\x01",
            "it all out from right inside the castle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Still, I'm glad we were at least able\x01",
            "to hold the Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1709")

    label("loc_100F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1019")
    Jump("loc_1709")

    label("loc_1019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_10A2")

    ChrTalk(    #36
        0xFE,
        "So, how was the banquet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "I only got to see the food during\x01",
            "my rounds inside. I didn't get to\x01",
            "eat any of it, sadly...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1709")

    label("loc_10A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_10C5")

    ChrTalk(    #38
        0xFE,
        "Enjoy your evening!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1709")

    label("loc_10C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1135")

    ChrTalk(    #39
        0xFE,
        (
            "The kitchen supplies were just\x01",
            "unloaded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "Looks like it's going to be one\x01",
            "hell of a banquet!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1709")

    label("loc_1135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1212")

    ChrTalk(    #41
        0xFE,
        (
            "Apparently, our security duties in\x01",
            "the city are to be much more rigorous\x01",
            "as of tonight's shift.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "We've been ordered to step up our\x01",
            "efforts as much as we can, since\x01",
            "the terrorists have yet to be caught.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1709")

    label("loc_1212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1296")

    ChrTalk(    #43
        0xFE,
        (
            "We haven't been told much about\x01",
            "Her Majesty's illness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "We're just as worried about it\x01",
            "as anyone else, honestly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1709")

    label("loc_1296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1308")

    ChrTalk(    #45
        0xFE,
        (
            "Round one of the tournament looks\x01",
            "to have just finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "I wonder how the Royal Garrison\x01",
            "did?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1709")

    label("loc_1308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_14A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_13C0")

    ChrTalk(    #47
        0xFE,
        (
            "Duke Dunan's reputation in the\x01",
            "castle is just as bad as it is\x01",
            "on the outside, I assure you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "Thank goodness Colonel Richard\x01",
            "is around to buffer his nonsense.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A3")

    label("loc_13C0")

    OP_A2(0x1)

    ChrTalk(    #49
        0xFE,
        (
            "Duke Dunan's reputation in the\x01",
            "castle is just as bad as it is\x01",
            "on the outside, I assure you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "All he seems to do is eat, sleep\x01",
            "and fiddle around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Thank goodness Colonel Richard\x01",
            "is around to buffer his nonsense.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A3")

    Jump("loc_1709")

    label("loc_14A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1688")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1589")

    ChrTalk(    #52
        0xFE,
        (
            "Since the tournament is comprised of team\x01",
            "battles this year, there are fewer rounds\x01",
            "than in years past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "The matches are now set to start\x01",
            "in the afternoons, too--again,\x01",
            "very different from years past.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1685")

    label("loc_1589")

    OP_A2(0x1)

    ChrTalk(    #54
        0xFE,
        "Well, the preliminaries are over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "Since the tournament is comprised of team\x01",
            "battles this year, there are fewer rounds\x01",
            "than in years past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "The matches are now set to start\x01",
            "in the afternoons, too--again,\x01",
            "very different from years past.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1685")

    Jump("loc_1709")

    label("loc_1688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1709")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_16D4")

    ChrTalk(    #57
        0xFE,
        (
            "You're in the Royal Capital!\x01",
            "Go and enjoy the sights!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1709")

    label("loc_16D4")


    ChrTalk(    #58
        0xFE,
        (
            "Sorry, but the castle is off-\x01",
            "limits right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1709")

    TalkEnd(0xFE)
    Return()

    # Function_5_F28 end

    def Function_6_170D(): pass

    label("Function_6_170D")

    EventBegin(0x0)
    OP_6C(30000, 0)

    def lambda_171E():
        OP_6D(-930, 750, 44710, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_171E)

    def lambda_1736():
        OP_67(0, 4250, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1736)

    def lambda_174E():
        OP_6B(11000, 10000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_174E)

    def lambda_175E():
        OP_6C(0, 15000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_175E)
    Sleep(12000)
    SetChrPos(0x101, -910, 0, 8880, 0)
    SetChrPos(0x102, 2029, 0, 10110, 0)

    def lambda_1795():
        OP_6D(-290, 0, 32350, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1795)

    def lambda_17AD():
        OP_6B(7180, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17AD)

    def lambda_17BD():
        OP_6E(262, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_17BD)

    def lambda_17CD():
        OP_8E(0xFE, 0xFFFFFD62, 0x0, 0x4808, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17CD)

    def lambda_17E8():
        OP_8E(0xFE, 0x51E, 0x0, 0x4808, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17E8)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #59
        0x101,
        (
            "#000FWow...so that's Grancel Castle.\x02\x03",

            "It's gorgeous. I guess it really\x01",
            "is fit for a queen.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #60
        0x102,
        (
            "#010FIt's not just pretty... It's\x01",
            "also really solidly built.\x02\x03",

            "For instance,\x01",
            "look at the main gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#000FYeah, I don't think getting through\x01",
            "there would be an easy task.\x02\x03",

            "Which means, I guess we'll have\x01",
            "to talk to those soldiers there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x102,
        (
            "#010FWell, steel your nerves,\x01",
            "and let's give it a shot.\x02\x03",

            "Okay, we're just country folk,\x01",
            "here on vacation and checking\x01",
            "out the castle.\x02\x03",

            "And we just thought we'd try\x01",
            "and catch a glimpse of Her\x01",
            "Majesty, since we're here.\x02\x03",

            "Does that sound okay to you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #63
        0x101,
        (
            "#000FYou know, you're disturbingly\x01",
            "good at coming up with that\x01",
            "kind of stuff.\x02\x03",

            "Not that it doesn't come in\x01",
            "handy, but still...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #64
        0x102,
        (
            "#010FI'll take that as a compliment.\x01",
            "Okay, now smile and act natural.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B3E():
        OP_6D(0, 250, 42590, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B3E)
    OP_6B(5100, 4000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    SetChrPos(0x101, -850, 0, 25330, 0)
    SetChrPos(0x102, 1090, 0, 22700, 0)
    Sleep(1000)

    ChrTalk(    #65
        0x101,
        "#000FUmm... Hello there...\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_1BC5():

        label("loc_1BC5")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1BC5")

    QueueWorkItem2(0x8, 1, lambda_1BC5)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_1BED():

        label("loc_1BED")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1BED")

    QueueWorkItem2(0x9, 1, lambda_1BED)

    def lambda_1BFE():
        OP_8E(0xFE, 0xFFFFFCAE, 0x0, 0x9290, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BFE)

    def lambda_1C19():
        OP_8E(0xFE, 0x316, 0x0, 0x9290, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C19)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #66
        0x8,
        "Good afternoon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        (
            "Welcome to Grancel Castle.\x01",
            "Please state your business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x102,
        (
            "#010FOh, we're just getting here\x01",
            "from Rolent. We're taking in\x01",
            "the sights, you might say.\x02\x03",

            "We were wondering if there was\x01",
            "any chance we might get a\x01",
            "tour of the castle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        "Ahh, I get it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        (
            "I'm sorry, but access to\x01",
            "the castle is restricted to\x01",
            "authorized personnel only.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "Security's been tighter, what\x01",
            "with the terrorism scares.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x9,
        (
            "Once the terrorists are caught,\x01",
            "tours will probably open up again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#000FReally...? Dang.\x02\x03",

            "There goes my dream of seeing\x01",
            "the queen in real life...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        "Well, not necessarily...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        (
            "She always addresses the people from\x01",
            "her terrace during the Birthday \x01",
            "Celebration. You could see her then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        (
            "Fair warning, though... Her\x01",
            "Majesty hasn't been in the\x01",
            "best of health these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x9,
        (
            "I don't know if she'll be able to\x01",
            "manage her traditional greeting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        "#000FHuh...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x102,
        "#010FHer Majesty is ill?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        (
            "Yes...\x01",
            "I hear it's because of stress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x9,
        (
            "Or maybe from the shock of\x01",
            "learning the Royal Guardsmen were\x01",
            "involved in a terrorist plot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        (
            "She hasn't been seen much lately.\x01",
            "I believe she's resting in her\x01",
            "private quarters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        "#000FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        (
            "Damn the Guardsmen... How could\x01",
            "they just turn traitor like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        (
            "Never did like those damned\x01",
            "elitist jerks anyway.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)
    OP_44(0x8, 0xFF)
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #86
        0x9,
        (
            "B-But Lieutenant Schwarz was always\x01",
            "so kind and considerate to everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x9,
        (
            "She even taught us court etiquette\x01",
            "and how to wield a sword.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x9,
        (
            "It's just hard for me to picture\x01",
            "someone like that as a terrorist.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 800)

    ChrTalk(    #89
        0x8,
        "O-Of course it's hard!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x8,
        (
            "She probably left because she\x01",
            "felt responsible for her men's\x01",
            "actions!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        "Poor Lieutenant Schwarz...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    ChrTalk(    #92
        0x101,
        (
            "#000F(You don't suppose...)\x02\x03",

            "(...these two had a little crush\x01",
            "on the lieutenant, do you?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x102,
        "#010F(Yeah, it seems so.)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #94
        0x8,
        "Ahem!...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x8,
        (
            "Anyway, yes.\x01",
            "The castle is off limits.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #96
        0x9,
        "Sorry, but you can't go inside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#000F*sigh*\x01",
            "Well, I guess that's that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x102,
        (
            "#010FI'm just a tad bit worried...\x02\x03",

            "If Her Majesty has taken sick,\x01",
            "who's seeing to her daily affairs\x01",
            "with running the country?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x9,
        (
            "Yes, it's certainly a natural\x01",
            "enough concern.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x9,
        (
            "For now, there's someone acting\x01",
            "as her proxy, on paper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#000FHow's that work?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        "Ha ha. Literally. On paper.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        (
            "I can't picture someone like\x01",
            "him ever actually making any\x01",
            "real governmental decisions.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #104
        0x9,
        "Hey, watch what you say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x9,
        (
            "Though I'll admit, I would have\x01",
            "thought that the duty would fall\x01",
            "to the princess...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #106
        0x8,
        (
            "And you tell me to watch\x01",
            "what *I* say...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, -370, 750, 48420, 180)
    SetChrPos(0xB, 550, 750, 49230, 180)

    def lambda_2673():
        OP_67(0, 9500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2673)

    def lambda_268B():
        OP_6B(3800, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_268B)

    def lambda_269B():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_269B)
    Sleep(100)

    def lambda_26B0():
        OP_8F(0xFE, 0xFFFFF6F0, 0x0, 0xA406, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_26B0)

    def lambda_26CB():
        OP_8F(0xFE, 0x802, 0x0, 0xA4A6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_26CB)
    OP_6D(-10, 750, 48050, 3000)

    def lambda_26F7():

        label("loc_26F7")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_26F7")

    QueueWorkItem2(0x101, 1, lambda_26F7)

    def lambda_2708():

        label("loc_2708")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_2708")

    QueueWorkItem2(0x102, 1, lambda_2708)

    def lambda_2719():

        label("loc_2719")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_2719")

    QueueWorkItem2(0x9, 1, lambda_2719)

    def lambda_272A():

        label("loc_272A")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_272A")

    QueueWorkItem2(0x8, 1, lambda_272A)
    SetChrPos(0x101, -2130, 0, 39490, 0)
    SetChrPos(0x102, -2130, 0, 37840, 0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x78)
    Sleep(1000)
    Sleep(1000)

    def lambda_2775():
        OP_8E(0xFE, 0xFFFFFE98, 0x2EE, 0xAE2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2775)
    Sleep(500)

    def lambda_2795():
        OP_8E(0xFE, 0x276, 0x2EE, 0xAF78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2795)
    OP_6D(0, 750, 44920, 2000)
    WaitChrThread(0xA, 0x1)
    TurnDirection(0xA, 0xB, 400)

    ChrTalk(    #107
        0xA,
        (
            "#220FBah! I've never been\x01",
            "so insulted!\x02\x03",

            "The tournament should have\x01",
            "already begun, and I'M NOT\x01",
            "THERE.\x02\x03",

            "Phillip! Why didn't you wake me\x01",
            "sooner! This is all your fault!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(    #108
        0xB,
        (
            "#720FI am terribly sorry, Your Grace.\x02\x03",

            "But I was merely trying to look after your\x01",
            "mental well-being.\x02\x03",

            "For the last few days you have been in the\x01",
            "banquet hall, drinking and singing...\x02\x03",

            "Consuming exclusively beer and donuts\x01",
            "while reading your morning comics...\x02\x03",

            "I feel that it should come as no surprise that\x01",
            "you overslept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xA,
        (
            "#220FSilence, Phillip! I'm not in the mood\x01",
            "to listen to your chastisements!\x02\x03",

            "As the future king, I can do\x01",
            "what I want, whenever I want!\x02\x03",

            "Bah! Time is short! Come on, we\x01",
            "must hurry to the Grand Arena!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A93():
        OP_8E(0xFE, 0xFFFFFEF2, 0x0, 0x6D74, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2A93)
    Sleep(500)

    def lambda_2AB3():
        OP_8E(0xFE, 0x42E, 0x0, 0x6BF8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2AB3)
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_6D(-30, 0, 40870, 5000)

    def lambda_2B0D():
        OP_8F(0xFE, 0xFFFFFCEA, 0x0, 0xA3FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2B0D)

    def lambda_2B28():
        OP_8F(0xFE, 0x3B6, 0x0, 0xA3FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2B28)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #110
        0x101,
        "#000FUhhh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 0)
    OP_8E(0x102, 0xFFFFFD9E, 0x0, 0x95B0, 0x7D0, 0x0)
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(    #111
        0x102,
        "#010FBy any chance, was that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x8,
        "We know. Don't even say it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x8,
        (
            "That was His Grace, the duke...\x01",
            "acting proxy for Her Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        (
            "#000FWow. Suddenly I fear for\x01",
            "the entire country...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)
    OP_44(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #115
        0x9,
        (
            "W-Well, don't worry too much. He\x01",
            "has a very reliable assistant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x9,
        (
            "And it's thanks to him that we\x01",
            "haven't had any major incidents\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    def lambda_2CF0():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CF0)
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(    #117
        0x102,
        "#010FDo tell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x8,
        (
            "Ha ha... Colonel Richard, of the\x01",
            "Royal Army Intelligence Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x8,
        (
            "Since the duke is more of the\x01",
            "playboy sort, the colonel handles\x01",
            "all the government affairs.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #120
        0x101,
        "#000F(I knew it...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x102,
        (
            "#010F(They're pushing harder into\x01",
            "the core of the kingdom than\x01",
            "I'd expected... )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x8,
        (
            "So, try not to let this whole\x01",
            "thing get you down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x8,
        (
            "Grancel's got plenty of other\x01",
            "famous places you can check out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #124
        0x9,
        (
            "Yeah. You're in the royal city,\x01",
            "after all. Just go at your own pace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        (
            "#000FY-You're right.\x01",
            "We will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x102,
        "#010FThank you both for your kindness.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4103   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_170D end

    def Function_7_2F82(): pass

    label("Function_7_2F82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F8F")
    Return()

    label("loc_2F8F")

    EventBegin(0x0)

    def lambda_2F97():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F97)

    def lambda_2FA5():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2FA5)
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(    #127
        0x108,
        (
            "#070FOh, are we going to the\x01",
            "castle already?\x02\x03",

            "Just to remind you, since we're going\x01",
            "to be staying there after the party,\x01",
            "we won't be able to leave until morning.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Enter Grancel Castle]\x01",      # 0
            "[Not just yet]\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_30D2"),
        (1, "loc_31A0"),
        (SWITCH_DEFAULT, "loc_31D4"),
    )


    label("loc_30D2")


    ChrTalk(    #128
        0x108,
        (
            "#070FWell, let's show the gatekeeper\x01",
            "our invitations, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#000FUgh... I don't know why\x01",
            "I'm so nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x102,
        (
            "#010FProbably because we don't get\x01",
            "invitations to big events like\x01",
            "this very often.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D4")

    label("loc_31A0")


    ChrTalk(    #131
        0x108,
        "#070FBack already?\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    label("loc_31D4")


    def lambda_31DA():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31DA)

    def lambda_31E8():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_31E8)

    def lambda_31F6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_31F6)

    def lambda_3204():
        OP_67(0, 5220, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3204)

    def lambda_321C():
        OP_6E(287, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_321C)
    OP_6D(880, 500, 43300, 3000)
    SetChrPos(0x101, -620, 0, 32729, 0)
    SetChrPos(0x102, 920, 0, 32590, 0)
    SetChrPos(0x108, 90, 0, 34050, 0)

    def lambda_3270():
        OP_8E(0xFE, 0xFFFFFCFE, 0x0, 0x9B82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3270)
    Sleep(300)

    def lambda_3290():
        OP_8E(0xFE, 0x4E2, 0x0, 0x9BD2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3290)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #132
        0x8,
        (
            "Hey, this is the castle of Her\x01",
            "Majesty the Queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x9,
        (
            "Unless you have official business\x01",
            "here, you need to lea--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x9,
        "...Hey.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #135
        0x101,
        "#000FHi there!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #136
        0x102,
        (
            "#010FWe're sorry about the\x01",
            "other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x8,
        "Oh, it's you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x9,
        "You're still staying in town?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#000FYeah, we still have some business\x01",
            "to take care of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x102,
        (
            "#010FWe have a formal invitation, so\x01",
            "by your leave, may we pass?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #141
        0x8,
        "A formal...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x9,
        "...invitation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x108,
        "#070FReceived directly from His Grace.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x108, 0x168, 0x0, 0x9862, 0xBB8, 0x0)

    ChrTalk(    #144
        0x8,
        "Wha--?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x9,
        "It's a giant!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x108,
        (
            "#070FSee? Right here.\x01",
            "Written invitation.\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0x108, 0x21C, 0x0, 0xA1D6, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #147
        "\x07\x05Zin handed the soldier the Invitation.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0x108, 0x168, 0x0, 0x9862, 0x7D0, 0x0)

    ChrTalk(    #148
        0x8,
        "Let's see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x9,
        (
            "'To Zin and his team: In appreciation for\x01",
            "your performance in the competition, you\x01",
            "are cordially invited to a dinner party.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x9,
        (
            "Oh, okay... You guys were in the\x01",
            "Martial Arts Competition...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x8,
        (
            "Right, and I heard the winning team\x01",
            "was led by a huge Eastern guy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x8,
        "So is that you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#000FHee hee... You got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x102,
        (
            "#010FWe would greatly appreciate\x01",
            "your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x9,
        "Makes sense...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x9,
        (
            "The head maid told us\x01",
            "you'd be coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x9,
        (
            "You're missing someone...\x01",
            "What happened to him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x108,
        (
            "#070FIt's kind of impolite, I know,\x01",
            "but it doesn't look like he's\x01",
            "going to be able to make it.\x02\x03",

            "We're the only ones coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x8,
        (
            "Ahh...\x01",
            "Well, that's a pity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x8,
        (
            "No matter.\x01",
            "Please, go on in.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3877():
        OP_6D(70, 750, 44190, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3877)

    def lambda_388F():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_388F)

    def lambda_389F():
        OP_6E(438, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_389F)
    OP_8E(0x9, 0x46, 0x2EE, 0xB19E, 0x7D0, 0x0)
    WaitChrThread(0x102, 0x2)

    ChrTalk(    #161
        0x9,
        (
            "Now entering: Zin and company, victors\x01",
            "of the Martial Arts Competition!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x9,
        "Open the gate!\x02",
    )

    CloseMessageWindow()

    def lambda_3929():
        OP_6D(70, 3450, 44190, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3929)

    def lambda_3941():
        OP_67(0, 2270, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3941)

    def lambda_3959():
        OP_8E(0x8, 0xFFFFF8D0, 0x2EE, 0xB004, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3959)
    OP_8E(0x9, 0x7A8, 0x2EE, 0xAFC8, 0x7D0, 0x0)
    OP_8C(0x9, 180, 400)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 180, 400)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x78)

    ChrTalk(    #163
        0x101,
        (
            "#000FWow...\x02\x03",

            "It's like the Haken Gate, but there's\x01",
            "something more impressive about\x01",
            "it being part of a castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x102,
        (
            "#010FI'd bet it's more solid, too,\x01",
            "since it's the royal castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x8,
        "That's part of why it's impregnable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x8,
        (
            "Ever since the nation was established,\x01",
            "no enemy has ever broken through the\x01",
            "Ahnenburg Wall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x8,
        (
            "The capital's been ravaged by war\x01",
            "numerous times as a result of mutinies\x01",
            "and insurrections amongst the nobles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x9,
        (
            "But even then, the castle held the\x01",
            "rebel army at bay and protected the\x01",
            "royal family and the refugees...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x9,
        "Or so the stories say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        (
            "#000FWow...\x01",
            "That's pretty neat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x108,
        (
            "#070FVery much the sort of tale one\x01",
            "would expect from a nation\x01",
            "with such history.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #172
        0x8,
        (
            "Now, welcome to Her Majesty's\x01",
            "Grancel Castle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        (
            "Go right on in. You'll be met by a\x01",
            "welcoming party inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x9,
        "Enjoy your evening.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x638)
    EventEnd(0x0)
    Return()

    # Function_7_2F82 end

    def Function_8_3CF6(): pass

    label("Function_8_3CF6")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    OP_6D(70, -1900, 45200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(357, 0)
    SetChrPos(0xC, -790, 0, 41980, 180)
    SetChrPos(0xD, 950, 0, 41980, 180)
    Sleep(500)

    def lambda_3D85():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3D85)

    def lambda_3D93():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3D93)
    OP_6D(70, 2550, 45150, 2000)

    ChrTalk(    #175
        0xC,
        "Wh-What the...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xD,
        (
            "Uhh... Aren't we on total lockdown\x01",
            "right now? Why's the gate opening?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_3E40():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3E40)

    def lambda_3E4E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3E4E)
    OP_6D(70, -1900, 45200, 1000)

    ChrTalk(    #177
        0xC,
        "Wha--?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xD,
        "Impossible!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-1030, 0, 9000, 0)
    OP_67(0, 9340, -13360, 0)
    OP_6B(1000, 0)
    OP_6C(135000, 0)
    OP_6E(747, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x12, 1730, 0, -280, 0)
    SetChrPos(0x13, 1730, 0, -2790, 180)
    SetChrPos(0x14, 1730, 0, -5480, 180)
    SetChrPos(0x15, 1730, 0, -8070, 180)
    SetChrPos(0x16, 1730, 0, -10050, 180)
    SetChrPos(0xF, 3230, 0, -4350, 0)
    SetChrPos(0x10, 3230, 0, -1480, 0)
    SetChrPos(0x17, -1770, 0, -380, 260)
    SetChrPos(0x18, -1770, 0, -2970, 180)
    SetChrPos(0x19, -1770, 0, -5140, 180)
    SetChrPos(0x1A, -1770, 0, -7650, 180)
    SetChrPos(0xE, -3240, 0, -1470, 360)
    SetChrPos(0x11, -3240, 0, -4130, 360)

    def lambda_3FF0():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3FF0)

    def lambda_400B():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_400B)

    def lambda_4026():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4026)

    def lambda_4041():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4041)

    def lambda_405C():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_405C)

    def lambda_4077():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4077)

    def lambda_4092():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4092)

    def lambda_40AD():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_40AD)

    def lambda_40C8():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_40C8)

    def lambda_40E3():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_40E3)

    def lambda_40FE():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_40FE)

    def lambda_4119():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4119)

    def lambda_4134():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4134)

    def lambda_414F():
        OP_6D(-390, 0, 29050, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_414F)

    def lambda_4167():
        OP_6C(44000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4167)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_3CF6 end

    def Function_9_418E(): pass

    label("Function_9_418E")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(0, 4000, 27740, 0)
    OP_67(0, 3170, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(12000, 0)
    OP_6E(568, 0)
    OP_6D(0, 1000, 27740, 4000)
    Sleep(1000)

    def lambda_4206():
        OP_6D(-310, 5670, 42340, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4206)

    def lambda_421E():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_421E)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_418E end

    def Function_10_4245(): pass

    label("Function_10_4245")

    EventBegin(0x0)
    SetChrPos(0x1B, 2600, 0, -3950, 0)
    SetChrPos(0x101, 3420, 0, -2610, 357)
    SetChrPos(0x102, 4150, 0, -4140, 0)
    ClearChrFlags(0x1B, 0x80)
    SetMapFlags(0x1)
    OP_69(0x101, 0x0)
    OP_6A(0x101)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315, 0)
    OP_6E(262, 0)

    def lambda_42C0():
        OP_6C(45000, 20000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_42C0)

    def lambda_42D0():
        OP_91(0xFE, 0xFFFFF272, 0x0, 0xA1D6, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42D0)

    def lambda_42EB():
        OP_90(0xFE, 0xFFFFF272, 0x0, 0xA1D6, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_42EB)

    def lambda_4306():
        OP_90(0xFE, 0xFFFFF272, 0x0, 0xA1D6, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_4306)
    Sleep(1000)

    ChrTalk(    #179
        0x101,
        (
            "#000FGeez, Dad...\x02\x03",

            "Can't you at least stay with us until\x01",
            "the end of the Birthday Celebration...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x1B,
        (
            "#080FI'm sorry...but there's a war\x01",
            "council starting immediately.\x02\x03",

            "Colonel Richard may be in custody,\x01",
            "but there are plenty of his Special\x01",
            "Ops cohorts still at large.\x02\x03",

            "Captain Amalthea is also hiding\x01",
            "somewhere in the underground ruins.\x02\x03",

            "And if that weren't enough, it\x01",
            "looks like those sky bandits\x01",
            "ran off in all the confusion.\x02\x03",

            "We have to stay on guard so\x01",
            "they don't cause any trouble\x01",
            "during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        (
            "#000FArgh... Those guys are just\x01",
            "a constant pain in the ass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x102,
        (
            "#010FI didn't get the impression that\x01",
            "they'd try to stir up anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x1B,
        (
            "#080FWell, that's one problem solved, then.\x02\x03",

            "The real issue is that we really\x01",
            "don't know the significance of\x01",
            "what happened underground.\x02\x03",

            "We can only guess at what effect\x01",
            "breaking that seal will have.\x02\x03",

            "And what the purpose of\x01",
            "that 'Aureole' is...\x02\x03",

            "That's a puzzle that absolutely\x01",
            "must be solved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x101,
        (
            "#000FYeah, I guess you're right.\x02\x03",

            "And it doesn't sound like Colonel\x01",
            "Richard's memory can be trusted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x1B,
        (
            "#080FYes... Just like Kurt, he seems\x01",
            "to have some missing memories.\x02\x03",

            "Even so, the search team was\x01",
            "able to confirm one thing...\x02\x03",

            "We now know where the Black\x01",
            "Orbment came from.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_47FC():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_47FC)

    ChrTalk(    #186
        0x101,
        "#000FReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x102,
        "#010FYou know who made it?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x1B,
        (
            "#080FNot quite. But we do know who's\x01",
            "responsible for introducing it\x01",
            "to the Intelligence Division.\x02\x03",

            "Commander of the Special Ops:\x01",
            "2nd Lieutenant Lorence Belgar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x101,
        "#000F!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x102,
        "#010FHim...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x1B,
        (
            "#080FHe gave it to Richard shortly\x01",
            "after he was recruited for the\x01",
            "Intelligence Division.\x02\x03",

            "And 'coincidentally,' that would be\x01",
            "just about the same time Richard\x01",
            "planned his coup...\x02\x03",

            "We need to find out everything\x01",
            "about Lorence that we can.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_49F5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_49F5)

    ChrTalk(    #192
        0x101,
        (
            "#000FHuh...\x01",
            "He always did seem strange...\x02\x03",

            "I guess we were lucky that we\x01",
            "actually got a good look at\x01",
            "his face, huh?\x02\x03",

            "If you want, I can try drawing\x01",
            "you a picture of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x1B,
        (
            "#080FThat would be appreciated.\x02\x03",

            "I have to admit, though, that I\x01",
            "don't have the utmost faith in\x01",
            "your artistic skills...\x02\x03",

            "Maybe I should ask Scherazard\x01",
            "or Her Majesty...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1B, 400)

    ChrTalk(    #194
        0x101,
        "#000F...That's not nice.\x02",
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    def lambda_4B90():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4B90)
    ClearMapFlags(0x1)
    OP_69(0x101, 0x3E8)

    ChrTalk(    #195
        0x102,
        (
            "#010FEstelle...\x02\x03",

            "You actually saw Lorence's face?\x02",
        )
    )

    Sleep(500)
    OP_44(0x101, 0xFF)
    TurnDirection(0x101, 0x102, 400)
    OP_44(0x1B, 0xFF)
    TurnDirection(0x1B, 0x102, 400)
    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        (
            "#000FWhat, I didn't tell you?\x02\x03",

            "He took his helmet off, just\x01",
            "before he escaped.\x02\x03",

            "He had really nice\x01",
            "ash blond hair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x102,
        "#010F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        (
            "#000FHe had some seriously creepy\x01",
            "eyes, too, let me tell you...\x02\x03",

            "Brrrr... They were so cold, but\x01",
            "it was like they were on fire\x01",
            "at the same time.\x02\x03",

            "He told the queen, 'You are hardly\x01",
            "qualified to feel pity for me.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x102,
        (
            "#010FHardly qualified...?\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x101,
        "#000FJoshua...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x1B,
        (
            "#080FYour eyes are looking a little\x01",
            "creepy now too, Joshua! Something\x01",
            "on your mind?\x02\x03",

            "How about you let us handle the\x01",
            "cleanup here, and go have fun\x01",
            "at the festival?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1B, 400)

    ChrTalk(    #202
        0x102,
        (
            "#010FI...\x02\x03",

            "Okay. You're right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x101,
        (
            "#000FAwesome. Let's go live it up.\x02\x03",

            "Oh, right. Are we going to be\x01",
            "sleeping at the castle tonight?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x101, 400)

    ChrTalk(    #204
        0x1B,
        (
            "#080FYes. Her Majesty was kind enough\x01",
            "to let me use two of the guest\x01",
            "rooms in the eastern wing.\x02\x03",

            "Joshua and I will be on the\x01",
            "right, you and Schera on\x01",
            "the left.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1B, 400)

    ChrTalk(    #205
        0x101,
        "#000FMe and Schera? Together?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x1B,
        (
            "#080FYou don't like that setup?\x02\x03",

            "Okay. How about me and you in\x01",
            "one room, Joshua and Schera in\x01",
            "the other?\x02\x03",

            "Just imagine...all that time for you\x01",
            "to fawn over me, and wait on me, and\x01",
            "tell me how much you missed me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x101,
        "#000F...I'll bunk with Schera.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x1B,
        (
            "#080FHa ha ha!\x01",
            "I suspected as much.\x02\x03",

            "All right, then I'll see\x01",
            "you kids tonight.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_50FC():

        label("loc_50FC")

        TurnDirection(0xFE, 0x1B, 0)
        OP_48()
        Jump("loc_50FC")

    QueueWorkItem2(0x101, 1, lambda_50FC)

    def lambda_510D():

        label("loc_510D")

        TurnDirection(0xFE, 0x1B, 0)
        OP_48()
        Jump("loc_510D")

    QueueWorkItem2(0x102, 1, lambda_510D)
    OP_43(0x1B, 0x1, 0x0, 0xB)
    Sleep(3000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_92(0x102, 0x101, 0x5DC, 0x3E8, 0x0)

    ChrTalk(    #209
        0x102,
        (
            "#010FYou know, it wouldn't be a big deal for you\x01",
            "to share a room with him. I mean, it has\x01",
            "been a long time since you last saw him.\x02\x03",

            "Didn't you have a lot of stuff\x01",
            "about your mom that you wanted\x01",
            "to talk to him about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        (
            "#000FYeah, but...\x02\x03",

            "I don't much like the idea of\x01",
            "you and Schera in the same\x01",
            "room, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x102,
        "#010FHuh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #212
        0x101,
        (
            "#000FNothing! Nothing!\x02\x03",

            "Let's go and look around.\x02\x03",

            "The town's decked out with some\x01",
            "pretty cool festival-exclusive\x01",
            "shops, you know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x102,
        (
            "#010FWell, we certainly can't let THOSE\x01",
            "pass us by now, can we?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x66B)
    EventEnd(0x0)
    OP_6A(0x0)
    Return()

    # Function_10_4245 end

    def Function_11_5362(): pass

    label("Function_11_5362")

    OP_90(0x1B, 0xFFFFFD26, 0x0, 0x4E2, 0x7D0, 0x0)
    OP_8E(0x1B, 0x46, 0x2EE, 0xAAD2, 0x7D0, 0x0)
    OP_8E(0x1B, 0x190, 0x2EE, 0xBBBC, 0x7D0, 0x0)
    Return()

    # Function_11_5362 end

    SaveToFile()

Try(main)
