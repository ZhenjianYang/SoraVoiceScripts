from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R0303   ._SN',
        MapName             = 'Rolent',
        Location            = 'R0303.x',
        MapIndex            = 21,
        MapDefaultBGM       = "ed60022",
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
        'Scherazard',                           # 9
        'Miner Landan',                         # 10
        'Miner-in-Training',                    # 11
        'Malga Trail',                          # 12
        'Malga Trail',                          # 13
        'Target Camera',                        # 14
    )

    DeclEntryPoint(
        Unknown_00              = -1500,
        Unknown_04              = 0,
        Unknown_08              = -28000,
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
        Unknown_30              = 315,
        Unknown_32              = 315,
        Unknown_34              = 315,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 21,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = -1500,
        Unknown_04              = 0,
        Unknown_08              = -28000,
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
        Unknown_30              = 315,
        Unknown_32              = 315,
        Unknown_34              = 315,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 21,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 4000,
        Unknown_08              = -10000,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 315,
        Unknown_34              = 315,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 21,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = -1500,
        Unknown_04              = 0,
        Unknown_08              = -28000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 3200,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 315,
        Unknown_34              = 315,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 21,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00020 ._CH',             # 00
        'ED6_DT07/CH01500 ._CH',             # 01
        'ED6_DT06/CH20063 ._CH',             # 02
        'ED6_DT06/CH20064 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH00020P._CP',             # 00
        'ED6_DT07/CH01500P._CP',             # 01
        'ED6_DT06/CH20063P._CP',             # 02
        'ED6_DT06/CH20064P._CP',             # 03
    )

    DeclNpc(
        X                   = 8600,
        Z                   = 4000,
        Y                   = -8230,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -166100,
        Z                   = 100,
        Y                   = 127500,
        Direction           = 180,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -167010,
        Z                   = -70,
        Y                   = 78790,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2070,
        Z                   = -120,
        Y                   = -72730,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
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


    DeclEvent(
        X                   = -2500,
        Y                   = -1000,
        Z                   = -45000,
        Range               = 4000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF38C8,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )

    DeclEvent(
        X                   = -2000,
        Y                   = 4000,
        Z                   = -7442,
        Range               = 2000,
        Unknown_10          = 0x1770,
        Unknown_14          = 0xFFFFE4E4,
        Unknown_18          = 0x0,
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = -168250,
        Y                   = -1000,
        Z                   = 128000,
        Range               = -164500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x1EBCC,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = -2472,
        Y                   = -1000,
        Z                   = -21384,
        Range               = 2537,
        Unknown_10          = 0x1770,
        Unknown_14          = 0xFFFFB32C,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )


    ScpFunction(
        "Function_0_2D6",          # 00, 0
        "Function_1_33A",          # 01, 1
        "Function_2_387",          # 02, 2
        "Function_3_39D",          # 03, 3
        "Function_4_70B",          # 04, 4
        "Function_5_14BC",         # 05, 5
        "Function_6_14C6",         # 06, 6
        "Function_7_14D8",         # 07, 7
        "Function_8_14E2",         # 08, 8
        "Function_9_14FE",         # 09, 9
        "Function_10_151A",        # 0A, 10
        "Function_11_1536",        # 0B, 11
        "Function_12_1552",        # 0C, 12
        "Function_13_1667",        # 0D, 13
        "Function_14_1C2D",        # 0E, 14
        "Function_15_1C2E",        # 0F, 15
        "Function_16_1D76",        # 10, 16
        "Function_17_207B",        # 11, 17
        "Function_18_209B",        # 12, 18
    )


    def Function_0_2D6(): pass

    label("Function_0_2D6")

    ClearMapFlags(0x400000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 4)), scpexpr(EXPR_END)), "loc_2F3")
    SetChrPos(0x9, -167300, 0, 128100, 180)

    label("loc_2F3")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (3, "loc_2FF"),
        (SWITCH_DEFAULT, "loc_339"),
    )


    label("loc_2FF")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    OP_6D(-166000, 0, 128270, 0)
    SetChrPos(0xA, -166200, 0, 131180, 0)
    Event(0, 15)
    Jump("loc_339")

    label("loc_339")

    Return()

    # Function_0_2D6 end

    def Function_1_33A(): pass

    label("Function_1_33A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_352"),
        (101, "loc_352"),
        (102, "loc_36C"),
        (103, "loc_36C"),
        (SWITCH_DEFAULT, "loc_386"),
    )


    label("loc_352")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFD7790, 0x30011)
    ClearChrFlags(0xB, 0x4)
    Jump("loc_386")

    label("loc_36C")

    OP_16(0x2, 0xFA0, 0xFFFB8390, 0xFFFFBD98, 0x3006A)
    ClearChrFlags(0xC, 0x4)
    Jump("loc_386")

    label("loc_386")

    Return()

    # Function_1_33A end

    def Function_2_387(): pass

    label("Function_2_387")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_387")

    label("loc_39C")

    Return()

    # Function_2_387 end

    def Function_3_39D(): pass

    label("Function_3_39D")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_454")

    ChrTalk(    #0
        0x9,
        "Well, if it isn't you bracers, again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        (
            "The monster scare at the mines\x01",
            "has finally settled down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x9,
        (
            "The boss finally went home to\x01",
            "Rolent after this long stint.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_4D9")

    ChrTalk(    #3
        0x9,
        (
            "Trent snuck out on me, too, when\x01",
            "I took my eyes off him for a second.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        (
            "I'm sure he's off sluffing work\x01",
            "somewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707")

    label("loc_4D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_END)), "loc_558")

    ChrTalk(    #5
        0x9,
        "Oh, it's you bracers from the other day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x9,
        (
            "You got some more business here?\x01",
            "It's dark inside, so be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707")

    label("loc_558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_61A")

    ChrTalk(    #7
        0x9,
        (
            "Man, things have really made\x01",
            "a turn for the worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x9,
        (
            "But I'm glad you kids were around\x01",
            "to help us out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        (
            "If it had been just us miners alone,\x01",
            "we may not have fared so well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707")

    label("loc_61A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 4)), scpexpr(EXPR_END)), "loc_697")

    ChrTalk(    #10
        0x9,
        "It's dark inside, so be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x9,
        (
            "If you're looking for the boss, he\x01",
            "should be down in the lower tunnels.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707")

    label("loc_697")


    ChrTalk(    #12
        0x9,
        (
            "This is the entrance to the Malga Mine.\x01",
            "If you're not here on business then\x01",
            "I'll have to ask you to leave.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_707")

    TalkEnd(0x9)
    Return()

    # Function_3_39D end

    def Function_4_70B(): pass

    label("Function_4_70B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14BB")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_A2(0x254)
    OP_43(0xD, 0x1, 0x0, 0x5)
    OP_43(0xD, 0x2, 0x0, 0x6)
    OP_43(0x0, 0x1, 0x0, 0x7)
    OP_6D(0, 5200, -6500, 3000)
    Sleep(1000)
    Fade(1000)
    SetChrPos(0x101, -845, 0, -22467, 0)
    SetChrPos(0x102, 471, 0, -22527, 0)
    SetChrPos(0x10F, -1170, 0, -24389, 0)
    SetChrPos(0x110, 72, 0, -24459, 0)
    OP_6C(315000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3000, 0)
    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x10F, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x10F, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x10F, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xD, 0x0)
    OP_0D()

    ChrTalk(    #13
        0x110,
        (
            "#153F#6PWow! This tower is really tall.\x02\x03",

            "#153FI wonder how many floors it has.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#000F#3PThe last time we were here, we only\x01",
            "made it as far as the 2nd floor...\x02\x03",

            "#000FBut judging from the scale, I'd\x01",
            "say it probably has about 5 or 6.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x102,
        (
            "#010F#6PThere should be 5. At least, that's\x01",
            "what it said in a book at home.\x02\x03",

            "#010FIt was investigated some time ago,\x01",
            "but it looks like it was abandoned\x01",
            "after that.\x02\x03",

            "#010FThat reminds me. It seems like\x01",
            "there are a number of other\x01",
            "towers like this in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10F,
        (
            "#140F#3PThat's correct.\x02\x03",

            "#140FThere are towers similar to this\x01",
            "one in the Bose, Ruan, and\x01",
            "Zeiss regions.\x02\x03",

            "#140FThey all seem to have been built\x01",
            "around the time that the Liberl\x01",
            "Kingdom was founded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#000F#3PIs that so? I think I'm starting\x01",
            "to feel the history already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10F,
        (
            "#141F#3PMy job this time is to uncover\x01",
            "the truth about them.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10F, 0x110, 400)
    TurnDirection(0x101, 0x110, 400)
    TurnDirection(0x102, 0x110, 400)

    ChrTalk(    #19
        0x10F,
        (
            "#140F#3PDorothy, get me a few long\x01",
            "angle shots of this place.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x110, 0x10F, 400)

    ChrTalk(    #20
        0x110,
        "#151F#6PSure!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x110, 2)
    OP_43(0x101, 0x1, 0x0, 0x8)
    OP_43(0x102, 0x1, 0x0, 0x9)
    OP_43(0x10F, 0x1, 0x0, 0xA)
    OP_43(0x110, 0x1, 0x0, 0xB)
    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x110, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x110, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x110, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xD, 0xBB8)
    SetChrChipByIndex(0x110, 3)

    ChrTalk(    #21
        0x110,
        "#150F#6PHere we go!\x02",
    )

    CloseMessageWindow()
    OP_6B(2800, 1000)

    ChrTalk(    #22
        0x110,
        "#150F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#004F(A-Amazing... Is a photographer's personality\x01",
            "supposed to change by taking a camera in\x01",
            "their hands like that?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        "#010F(She certainly looks like a pro...)\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #25
        0x110,
        (
            "#6P...\x02\x03",

            "#6P...\x02\x03",

            "#6P...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_62(0x110, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(2000)

    ChrTalk(    #26
        0x110,
        "#6P...*snork*...Zzz...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    OP_92(0x10F, 0x110, 0x7D0, 0xFA0, 0x0)
    OP_92(0x10F, 0x110, 0x3E8, 0x1388, 0x0)
    OP_92(0x10F, 0x110, 0x1F4, 0x1770, 0x0)
    SetChrChipByIndex(0x110, 2)
    OP_22(0x7D, 0x0, 0x64)
    OP_8F(0x110, 0x0, 0x0, 0xFFFF97B4, 0x1770, 0x0)
    OP_63(0x110)
    OP_62(0x110, 0x0, 1900, 0x30, 0x32, 0x96, 0x0)
    OP_22(0x30, 0x0, 0x64)
    Sleep(2000)
    OP_63(0x110)
    Sleep(600)
    TurnDirection(0x110, 0x10F, 400)

    ChrTalk(    #27
        0x110,
        (
            "#152F#2POw...\x02\x03",

            "#152FThat really hurts, Nial!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10F,
        (
            "#144F#1PThis happens every time you\x01",
            "try to take a picture like that!\x02\x03",

            "#144FQuit trying to act professional\x01",
            "and just get me a shot using\x01",
            "your usual style!\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x10F, 0xFFFFF360, 0x0, 0xFFFFA091, 0xBB8, 0x0)
    TurnDirection(0x10F, 0x110, 400)

    ChrTalk(    #29
        0x110,
        (
            "#151F#2PI guess I shouldn't try to tone down\x01",
            "my style just to look good...\x02\x03",

            "#151FWell, I guess I'll have to do it\x01",
            "in my own way.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x110, 0xFFFFFE58, 0x0, 0xFFFF98E9, 0xBB8, 0x0)
    SetChrChipByIndex(0x110, 3)
    OP_8C(0x110, 0, 400)
    LoadEffect(0x0, "map\\\\mp032_00.eff")

    ChrTalk(    #30
        0x110,
        "#5P#150FOh, looking good, looking good!\x02",
    )

    CloseMessageWindow()
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x110, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_8F(0x110, 0x2F6, 0x0, 0xFFFF99A3, 0xBB8, 0x0)

    ChrTalk(    #31
        0x110,
        (
            "#5P#150FNow that's what I call sexy\x01",
            "and cute!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x110, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_8F(0x110, 0xFFFFFFC2, 0x0, 0xFFFF9BE7, 0xBB8, 0x0)

    ChrTalk(    #32
        0x110,
        "#5P#151FHere we go! Say cheese!\x02",
    )

    CloseMessageWindow()
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x110, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_43(0x110, 0x1, 0x0, 0xC)
    OP_69(0x102, 0x3E8)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #33
        0x101,
        (
            "#008FI don't get it...\x01",
            "Why is she doing that when she's\x01",
            "not taking photos of a person...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x102,
        (
            "#019FSomehow it seems natural\x01",
            "for her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10F,
        (
            "#145FShe says that she can see the\x01",
            "expression of the scenery,\x01",
            "whatever that's supposed to mean.\x02\x03",

            "#145FAnd believe it or not, she takes\x01",
            "some pretty breathtaking pictures\x01",
            "acting all ridiculous like that.\x02\x03",

            "#145FI guess it could be considered a\x01",
            "type of genius. The kind that's\x01",
            "borderline insane, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#501FWow... People are sure never\x01",
            "what they seem to be.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x110, 0xFF)
    Sleep(1000)
    SetChrChipByIndex(0x110, 65535)
    OP_92(0x110, 0x0, 0x640, 0xBB8, 0x0)
    TurnDirection(0x110, 0x10F, 400)
    TurnDirection(0x10F, 0x110, 400)

    ChrTalk(    #37
        0x110,
        "#151FOkay. I'm all done here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10F,
        (
            "#141FAll right, then.\x01",
            "Let's get inside.\x02\x03",

            "#141FWe're headed for the roof. I'm\x01",
            "counting on you two greenhorns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#006FYou just leave it to us.\x02\x03",

            "#006FWe won't let any monsters lay\x01",
            "a single paw on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        (
            "#010FPlease make sure to keep close\x01",
            "behind us.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_14BB")

    Return()

    # Function_4_70B end

    def Function_5_14BC(): pass

    label("Function_5_14BC")

    OP_6C(0, 3000)
    Return()

    # Function_5_14BC end

    def Function_6_14C6(): pass

    label("Function_6_14C6")

    OP_67(0, 4500, -10000, 3000)
    Return()

    # Function_6_14C6 end

    def Function_7_14D8(): pass

    label("Function_7_14D8")

    OP_6B(6000, 3000)
    Return()

    # Function_7_14D8 end

    def Function_8_14E2(): pass

    label("Function_8_14E2")

    OP_8E(0x101, 0xFFFFF652, 0x0, 0xFFFFA67D, 0xBB8, 0x0)
    TurnDirection(0x101, 0x110, 400)
    Return()

    # Function_8_14E2 end

    def Function_9_14FE(): pass

    label("Function_9_14FE")

    OP_8E(0x102, 0xFFFFF5CE, 0x0, 0xFFFFA41E, 0xBB8, 0x0)
    TurnDirection(0x102, 0x110, 400)
    Return()

    # Function_9_14FE end

    def Function_10_151A(): pass

    label("Function_10_151A")

    OP_8E(0x10F, 0xFFFFF360, 0x0, 0xFFFFA091, 0xBB8, 0x0)
    TurnDirection(0x10F, 0x110, 400)
    Return()

    # Function_10_151A end

    def Function_11_1536(): pass

    label("Function_11_1536")

    OP_8E(0x110, 0xFFFFFE58, 0x0, 0xFFFF98E9, 0xBB8, 0x0)
    OP_8C(0x110, 0, 400)
    Return()

    # Function_11_1536 end

    def Function_12_1552(): pass

    label("Function_12_1552")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1666")
    OP_8F(0x110, 0xFFFFFE58, 0x0, 0xFFFF98E9, 0xBB8, 0x0)
    Sleep(2000)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x110, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_8F(0x110, 0x2F6, 0x0, 0xFFFF99A3, 0xBB8, 0x0)
    Sleep(1500)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x110, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_8F(0x110, 0xFFFFFFC2, 0x0, 0xFFFF9BE7, 0xBB8, 0x0)
    Sleep(3000)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x110, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Jump("Function_12_1552")

    label("loc_1666")

    Return()

    # Function_12_1552 end

    def Function_13_1667(): pass

    label("Function_13_1667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1735")
    EventBegin(0x0)
    TurnDirection(0x9, 0x0, 400)
    OP_4A(0x9, 255)

    ChrTalk(    #41
        0x9,
        (
            "This is the entrance to the\x01",
            "Malga Mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        (
            "If you're not here on business,\x01",
            "then I'll have to ask you to leave.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x1E654), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_92(0x0, 0xD, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    OP_8C(0x9, 180, 0)
    OP_4B(0x9, 255)
    Return()

    label("loc_1735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C2C")
    OP_4A(0x9, 255)
    EventBegin(0x0)
    OP_A2(0x23C)
    OP_28(0x3, 0x1, 0x8)
    Fade(1000)
    SetChrPos(0x101, -166670, 30, 125190, 0)
    SetChrPos(0x102, -165340, 40, 125200, 0)
    OP_6D(-167300, 0, 128070, 2000)
    TurnDirection(0x9, 0x101, 0)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8E(0x9, 0xFFFD775E, 0x0, 0x1F040, 0x3E8, 0x0)
    OP_8C(0x9, 180, 400)

    ChrTalk(    #43
        0x9,
        (
            "#2PThis is the entrance to the\x01",
            "Malga Mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        (
            "#2PIf you're not here on business,\x01",
            "then I'll have to ask you to leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#502FBelieve it or not, we are here\x01",
            "on business!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x102,
        (
            "#010FRolent's mayor, Klaus, has asked\x01",
            "that we come here and pick up a\x01",
            "certain septium crystal.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #47
        "\x07\x05Estelle shows Landan the Mayor's Referral.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #48
        0x9,
        (
            "#2PWell, all right, then. If you've got\x01",
            "a referral from the mayor, then\x01",
            "that's a different story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        (
            "#2PI don't mean to make your job any more\x01",
            "difficult, but would you mind going inside\x01",
            "and speaking with the boss directly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        (
            "#2PI'm supposed to stand watch\x01",
            "out here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#505FSure, that's fine but...\x01",
            "why the boss?\x02\x03",

            "We're actually here to see the\x01",
            "mine chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "#2PThat mine chief you're talking about is\x01",
            "actually our boss, Mr. Gaton. He manages\x01",
            "the mine and all of its workers. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "#2PHe's the kind of guy who enjoys\x01",
            "discovering a septium lode more\x01",
            "than eating three meals a day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "#2PI'm fairly sure he's working down\x01",
            "in the lower tunnels today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        (
            "#010FThanks for the tip. We'll go\x01",
            "see if we can locate him.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x9, 0xFFFD727C, 0x0, 0x1F464, 0xBB8, 0x0)
    OP_8C(0x9, 180, 400)
    OP_4B(0x9, 255)
    EventEnd(0x0)

    label("loc_1C2C")

    Return()

    # Function_13_1667 end

    def Function_14_1C2D(): pass

    label("Function_14_1C2D")

    Return()

    # Function_14_1C2D end

    def Function_15_1C2E(): pass

    label("Function_15_1C2E")

    EventBegin(0x0)
    OP_6D(-166260, 20, 124370, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_8E(0xA, 0xFFFD7646, 0xFFFFFFF6, 0x1DF9C, 0x1388, 0x0)
    OP_8C(0xA, 0, 400)

    ChrTalk(    #56
        0xA,
        (
            "That was a huge miscalculation\x01",
            "on my part...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xA,
        (
            "I never expected monsters to\x01",
            "surface or bracers to show up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xA,
        (
            "I guess I just have to report\x01",
            "the truth about everything that\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)
    OP_8E(0xA, 0xFFFD756A, 0x14, 0x1B47C, 0x1770, 0x0)
    NewScene("ED6_DT01/C0100   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1C2E end

    def Function_16_1D76(): pass

    label("Function_16_1D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 6)), scpexpr(EXPR_END)), "loc_1E3A")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    TurnDirection(0x106, 0x108, 0)

    ChrTalk(    #59
        0x108,
        (
            "#070Fどうした。\x01",
            "今から町に戻るのかい？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x106, 0)

    ChrTalk(    #60
        0x106,
        "#050Fいや、止めておくか……\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0x0, 0, 0, -42800, 0)
    SetChrPos(0x1, 0, 0, -42800, 0)
    SetChrPos(0x2, 0, 0, -42800, 0)
    SetChrPos(0x3, 0, 0, -42800, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    label("loc_1E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E46")
    Return()

    label("loc_1E46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_END)), "loc_1E4E")
    Return()

    label("loc_1E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207A")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    StopSound(0x9470, 0x30D40, 0x0)

    def lambda_1E70():
        OP_6B(6000, 9500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1E70)

    def lambda_1E80():
        OP_6C(0, 6000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1E80)

    def lambda_1E90():
        OP_67(0, 4000, -10000, 9500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_1E90)
    OP_6D(140, 5000, -10820, 6000)
    SetChrPos(0x101, 500, 100, -22600, 0)
    SetChrPos(0x102, -500, 100, -22600, 0)
    OP_43(0x102, 0x0, 0x0, 0x11)
    OP_A2(0x3)
    OP_8E(0x101, 0x1F4, 0xFA0, 0xFFFFD738, 0x1388, 0x0)
    OP_A5(0x3)
    WaitChrThread(0x0, 0x3)
    Fade(1000)
    StopSound(0x9470, 0x186A0, 0x1F40)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6D(140, 4000, -10820, 0)
    OP_0D()

    ChrTalk(    #61
        0x101,
        (
            "#002FIt looks like we've come all the\x01",
            "way to the Esmelas Tower...\x02\x03",

            "#002FI didn't see any sign of them along\x01",
            "the trail, so do you think they've\x01",
            "wandered inside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x102,
        "#012FIt's quite likely that's the case.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #63
        0x102,
        (
            "#012FLet's go in.\x01",
            "It looks like we'll need to hurry...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #64
        0x101,
        "#002FRight!\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_28(0x1, 0x1, 0x4)
    OP_A2(0x221)

    label("loc_207A")

    Return()

    # Function_16_1D76 end

    def Function_17_207B(): pass

    label("Function_17_207B")

    OP_A6(0x3)
    Sleep(500)
    OP_8E(0xFE, 0xFFFFFE0C, 0xFA0, 0xFFFFD3D2, 0x1388, 0x0)
    OP_A3(0x3)
    Return()

    # Function_17_207B end

    def Function_18_209B(): pass

    label("Function_18_209B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 6)), scpexpr(EXPR_END)), "loc_20AD")
    EventBegin(0x0)
    NewScene("ED6_DT01/C2100   ._SN", 1, 0, 0)
    IdleLoop()

    label("loc_20AD")

    Return()

    # Function_18_209B end

    SaveToFile()

Try(main)
