from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1110   ._SN',
        MapName             = 'Bose',
        Location            = 'T1110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        'Borden',                               # 9
        'Rionne',                               # 10
        'Alvelle',                              # 11
        'Kuwano',                               # 12
        'Cecile',                               # 13
        'Modena',                               # 14
        'Mirano',                               # 15
        'Simon',                                # 16
        'Launa',                                # 17
        'Elke',                                 # 18
        'Royal Army Soldier',                   # 19
        'Royal Army Soldier',                   # 20
        'Royal Army Soldier',                   # 21
        'Trino',                                # 22
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 3000,
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
        'ED6_DT07/CH01680 ._CH',             # 00
        'ED6_DT07/CH01690 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01000 ._CH',             # 03
        'ED6_DT07/CH01010 ._CH',             # 04
        'ED6_DT07/CH01183 ._CH',             # 05
        'ED6_DT07/CH01230 ._CH',             # 06
        'ED6_DT07/CH01030 ._CH',             # 07
        'ED6_DT07/CH01480 ._CH',             # 08
        'ED6_DT07/CH01140 ._CH',             # 09
        'ED6_DT07/CH01640 ._CH',             # 0A
        'ED6_DT07/CH01200 ._CH',             # 0B
        'ED6_DT07/CH01003 ._CH',             # 0C
        'ED6_DT07/CH01010 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH01680P._CP',             # 00
        'ED6_DT07/CH01690P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01000P._CP',             # 03
        'ED6_DT07/CH01010P._CP',             # 04
        'ED6_DT07/CH01183P._CP',             # 05
        'ED6_DT07/CH01230P._CP',             # 06
        'ED6_DT07/CH01030P._CP',             # 07
        'ED6_DT07/CH01480P._CP',             # 08
        'ED6_DT07/CH01140P._CP',             # 09
        'ED6_DT07/CH01640P._CP',             # 0A
        'ED6_DT07/CH01200P._CP',             # 0B
        'ED6_DT07/CH01003P._CP',             # 0C
        'ED6_DT07/CH01010P._CP',             # 0D
    )

    DeclNpc(
        X                   = -22100,
        Z                   = 0,
        Y                   = 69250,
        Direction           = 0,
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
        X                   = -21340,
        Z                   = 0,
        Y                   = 72520,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -11200,
        Z                   = 5250,
        Y                   = 72600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -21700,
        Z                   = 0,
        Y                   = 3000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -16400,
        Z                   = 0,
        Y                   = -1700,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -18730,
        Z                   = 0,
        Y                   = 33060,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 19400,
        Z                   = 0,
        Y                   = 31200,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -21100,
        Z                   = 0,
        Y                   = 33600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 20970,
        Z                   = 0,
        Y                   = 67860,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 27100,
        Z                   = 4000,
        Y                   = 72200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -20715,
        Z                   = 0,
        Y                   = -1884,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -21300,
        Z                   = 0,
        Y                   = 66800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 21176,
        Z                   = 0,
        Y                   = 66028,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -21100,
        Z                   = 0,
        Y                   = 33600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )


    ScpFunction(
        "Function_0_2DA",          # 00, 0
        "Function_1_49A",          # 01, 1
        "Function_2_49B",          # 02, 2
        "Function_3_4B1",          # 03, 3
        "Function_4_540",          # 04, 4
        "Function_5_564",          # 05, 5
        "Function_6_5D4",          # 06, 6
        "Function_7_696",          # 07, 7
        "Function_8_1379",         # 08, 8
        "Function_9_1C81",         # 09, 9
        "Function_10_247E",        # 0A, 10
        "Function_11_2A92",        # 0B, 11
        "Function_12_428A",        # 0C, 12
        "Function_13_4C56",        # 0D, 13
        "Function_14_55C9",        # 0E, 14
        "Function_15_5E4E",        # 0F, 15
        "Function_16_6257",        # 10, 16
        "Function_17_63F3",        # 11, 17
        "Function_18_6457",        # 12, 18
        "Function_19_64CF",        # 13, 19
        "Function_20_65D6",        # 14, 20
        "Function_21_6701",        # 15, 21
    )


    def Function_0_2DA(): pass

    label("Function_0_2DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2E9")
    ClearChrFlags(0x15, 0x80)
    Jump("loc_3FD")

    label("loc_2E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_302")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_3FD")

    label("loc_302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_316")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_3FD")

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_348")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x10)
    Jump("loc_3FD")

    label("loc_348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_385")
    SetChrPos(0xD, 17400, 300, 28530, 270)
    SetChrPos(0xE, -20530, 0, 33050, 180)
    SetChrPos(0xC, -16400, 0, -1700, 90)
    Jump("loc_3FD")

    label("loc_385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_3AA")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)
    SetChrPos(0xC, -16400, 0, -1700, 90)
    Jump("loc_3FD")

    label("loc_3AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_3DB")
    SetChrFlags(0xD, 0x10)
    SetChrPos(0xC, -16400, 0, -1700, 135)
    SetChrPos(0xE, -23120, 0, 34500, 180)
    Jump("loc_3FD")

    label("loc_3DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_3FD")
    SetChrPos(0xB, -17620, 0, -680, 135)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_3FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_499")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, 20852, 0, 68000, 180)
    SetChrPos(0x11, 21329, 0, 68470, 180)
    OP_44(0x11, 0xFF)
    OP_43(0x11, 0x3, 0x0, 0x2)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x8, -20868, 0, 68402, 180)
    SetChrPos(0xA, -22006, 0, 68102, 135)
    SetChrPos(0x9, -19902, 0, 68102, 225)
    OP_44(0x8, 0xFF)
    OP_43(0x8, 0x3, 0x0, 0x2)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xC, -21950, 0, -570, 135)

    label("loc_499")

    Return()

    # Function_0_2DA end

    def Function_1_49A(): pass

    label("Function_1_49A")

    Return()

    # Function_1_49A end

    def Function_2_49B(): pass

    label("Function_2_49B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_49B")

    label("loc_4B0")

    Return()

    # Function_2_49B end

    def Function_3_4B1(): pass

    label("Function_3_4B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_4D0")

    label("loc_4B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4CD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4B8")

    label("loc_4CD")

    Jump("loc_53F")

    label("loc_4D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_51C")

    label("loc_4D7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_519")
    OP_8E(0xFE, 0xFFFFA5A6, 0x0, 0x8F0C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 500)
    OP_8E(0xFE, 0xFFFFA5A6, 0x0, 0x7BAC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 500)
    Jump("loc_4D7")

    label("loc_519")

    Jump("loc_53F")

    label("loc_51C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53F")
    OP_8D(0xFE, 20900, 30000, 15300, 31700, 2000)
    Jump("loc_51C")

    label("loc_53F")

    Return()

    # Function_3_4B1 end

    def Function_4_540(): pass

    label("Function_4_540")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_563")
    OP_8D(0xFE, 26200, 71400, 28400, 72600, 2000)
    Jump("Function_4_540")

    label("loc_563")

    Return()

    # Function_4_540 end

    def Function_5_564(): pass

    label("Function_5_564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_591")

    label("loc_56B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_58E")
    OP_8D(0xFE, 17430, 68790, 23880, 64870, 1500)
    Jump("loc_56B")

    label("loc_58E")

    Jump("loc_5D3")

    label("loc_591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_5B0")

    label("loc_598")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5AD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_598")

    label("loc_5AD")

    Jump("loc_5D3")

    label("loc_5B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5D3")
    OP_8D(0xFE, 17430, 68790, 23880, 64870, 1500)
    Jump("loc_5B0")

    label("loc_5D3")

    Return()

    # Function_5_564 end

    def Function_6_5D4(): pass

    label("Function_6_5D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_62A")

    label("loc_5DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_627")
    OP_8E(0xFE, 0xFFFFA6F0, 0x0, 0x11B34, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFB050, 0x0, 0x11AE4, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    Jump("loc_5DB")

    label("loc_627")

    Jump("loc_695")

    label("loc_62A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_649")

    label("loc_631")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_646")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_631")

    label("loc_646")

    Jump("loc_695")

    label("loc_649")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_695")
    OP_8E(0xFE, 0xFFFFA6F0, 0x0, 0x11B34, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFB050, 0x0, 0x11AE4, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    Jump("loc_649")

    label("loc_695")

    Return()

    # Function_6_5D4 end

    def Function_7_696(): pass

    label("Function_7_696")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_7F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_768")
    OP_A2(0x0)

    ChrTalk(    #0
        0xFE,
        (
            "It looks like Trino has come back\x01",
            "safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Now I can get back to business\x01",
            "without any reservations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "I know a Bose merchant shouldn't let\x01",
            "trouble like this discourage them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F3")

    label("loc_768")


    ChrTalk(    #3
        0xFE,
        (
            "Now I can get back to business\x01",
            "without any reservations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "I know a Bose merchant shouldn't let\x01",
            "trouble like this discourage them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F3")

    Jump("loc_1375")

    label("loc_7F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_A57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BB")
    OP_A2(0x0)

    ChrTalk(    #5
        0xFE,
        "But still...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "I feel like I'm going insane without\x01",
            "Trino being here in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "We've been fighting since we were\x01",
            "kids, so it's weird not having him\x01",
            "around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "And though he's a business rival,\x01",
            "we seem to have this strange\x01",
            "sense of solidarity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "I'm actually pretty proud of the\x01",
            "fact that the two of us built up\x01",
            "trade like we have in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Ha ha. Although, I'm sure if he heard\x01",
            "this, he'd laugh off the notion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A54")

    label("loc_9BB")


    ChrTalk(    #11
        0xFE,
        (
            "I feel like I'm going insane without\x01",
            "Trino being here in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Though he's a business rival, we seem\x01",
            "to have this strange sense of solidarity.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A54")

    Jump("loc_1375")

    label("loc_A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_C7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB2")
    OP_A2(0x0)

    ChrTalk(    #13
        0xFE,
        (
            "By the Goddess... First an airliner\x01",
            "goes missing and now we've got a\x01",
            "bunch of burglaries...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "I wonder what'll be next.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "The Cecilia resuming flights is about\x01",
            "the only good thing happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Although, as long as the international\x01",
            "lines with the Empire don't reopen, we\x01",
            "merchants can't reopen our businesses...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C78")

    label("loc_BB2")


    ChrTalk(    #17
        0xFE,
        (
            "Although, as long as the international\x01",
            "lines with the Empire don't reopen, we\x01",
            "merchants can't reopen our businesses...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "In any case, we merchants have all\x01",
            "been hit hard by these incidents.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C78")

    Jump("loc_1375")

    label("loc_C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF7")
    TurnDirection(0x13, 0x0, 0)

    ChrTalk(    #19
        0x13,
        (
            "We'll be done with our questioning\x01",
            "soon enough, so be good little\x01",
            "children and sit tight.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 0, 0)
    Jump("loc_1375")

    label("loc_CF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_ED0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E56")
    OP_A2(0x0)

    ChrTalk(    #20
        0xFE,
        (
            "With the Bose airspace being designated\x01",
            "a no-fly zone, businesses are being hit\x01",
            "hard economically.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "Flights from the border are also\x01",
            "being held up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "At this rate, there'll be no deals\x01",
            "to be made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "But...Mirano seems to be hammering\x01",
            "away under these conditions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "And if she can do it...I can't give\x01",
            "in either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECD")

    label("loc_E56")


    ChrTalk(    #25
        0xFE,
        (
            "Ms. Mirano seems to be hammering\x01",
            "away under these conditions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "And if she can do it...I can't give in either.\x02",
    )

    CloseMessageWindow()

    label("loc_ECD")

    Jump("loc_1375")

    label("loc_ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_10B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_105D")
    OP_A2(0x0)

    ChrTalk(    #27
        0xFE,
        (
            "Trino seems to have been on board\x01",
            "the airliner that went missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "I feel a little guilty saying this, but\x01",
            "this may just be my big chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "I figured I'd use this opportunity to\x01",
            "seize all of Trino's deals for myself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "But Mirano's glare was enough\x01",
            "to set me straight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "It's difficult for me to tell if that\x01",
            "father and daughter are on good\x01",
            "terms or not.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B6")

    label("loc_105D")


    ChrTalk(    #32
        0xFE,
        (
            "It's difficult for me to tell if that\x01",
            "father and daughter are on good\x01",
            "terms or not.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B6")

    Jump("loc_1375")

    label("loc_10B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_12AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120B")
    OP_A2(0x0)

    ChrTalk(    #33
        0xFE,
        (
            "My family has been merchants\x01",
            "conducting trade here in Bose\x01",
            "for generations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "I've been at odds with a man named\x01",
            "Trino here for some time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "However, recently Trino's daughter,\x01",
            "Mirano, has begun to amass her\x01",
            "own financial power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Now it's a cutthroat struggle between\x01",
            "the three of us to be on top.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A7")

    label("loc_120B")


    ChrTalk(    #37
        0xFE,
        (
            "Recently, Trino's daughter, Mirano,\x01",
            "has begun to amass her own\x01",
            "financial power from trade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "Now it's a cutthroat struggle\x01",
            "between the three of us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A7")

    Jump("loc_1375")

    label("loc_12AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1375")

    ChrTalk(    #39
        0xFE,
        (
            "Bose merchants enjoy the freedom of\x01",
            "the market system here, but we also\x01",
            "have a rule to always keep our word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "And for that reason alone we are\x01",
            "very strict about meetings and\x01",
            "punctuality.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1375")

    TalkEnd(0x8)
    Return()

    # Function_7_696 end

    def Function_8_1379(): pass

    label("Function_8_1379")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1462")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141E")
    OP_A2(0x1)

    ChrTalk(    #41
        0xFE,
        (
            "So those masked men were the\x01",
            "rumored sky bandits, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "I'm glad they were all arrested.\x01",
            "Now I can get back to focusing\x01",
            "on my work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_145F")

    label("loc_141E")


    ChrTalk(    #43
        0xFE,
        (
            "I'm sure I'm going to sell more\x01",
            "than the Trinos this month!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_145F")

    Jump("loc_1C7D")

    label("loc_1462")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_155C")

    ChrTalk(    #44
        0xFE,
        (
            "I really hope this city will settle\x01",
            "down soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "The stock market's cooling down, and at\x01",
            "this rate I'm going to show a big deficit\x01",
            "this month on my financial report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "And just when I had beaten out\x01",
            "the Trinos last month, too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C7D")

    label("loc_155C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_16D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1659")
    OP_A2(0x1)

    ChrTalk(    #47
        0xFE,
        "I got a real surprise last night.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "When I went to open the window\x01",
            "and let in some fresh air...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "There was some masked man staring\x01",
            "right in at me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "And he wasn't alone, either. There\x01",
            "were a bunch of others with him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16D1")

    label("loc_1659")


    ChrTalk(    #51
        0xFE,
        (
            "When I went to open the window\x01",
            "and let in some fresh air...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "There was some masked man staring\x01",
            "right in at me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D1")

    Jump("loc_1C7D")

    label("loc_16D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1751")
    TurnDirection(0x13, 0x0, 0)

    ChrTalk(    #53
        0x13,
        (
            "We'll be done with our questioning\x01",
            "soon enough, so how about being\x01",
            "good and sitting tight?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 0, 0)
    Jump("loc_1C7D")

    label("loc_1751")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1921")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1874")
    OP_A2(0x1)

    ChrTalk(    #54
        0xFE,
        (
            "My husband proceeds rationally\x01",
            "with his deals and business talks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "But Mr. Trino is the exact opposite.\x01",
            "He pushes with vigor and flair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "However, Ms. Mirano is getting\x01",
            "together with both of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "She's almost like Mayor Maybelle\x01",
            "in a number of ways.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_191E")

    label("loc_1874")


    ChrTalk(    #58
        0xFE,
        (
            "In the near future, Ms. Mirano just\x01",
            "may strip her of the top seat if she's\x01",
            "not careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "But that's not going to make us hold\x01",
            "back on anything, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_191E")

    Jump("loc_1C7D")

    label("loc_1921")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1A99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E7")
    OP_A2(0x1)

    ChrTalk(    #60
        0xFE,
        (
            "I just cannot believe that Mr. Trino\x01",
            "was on that airliner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "No matter how much of a rival he is,\x01",
            "we've still known him for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "I just hope he's safe...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A96")

    label("loc_19E7")


    ChrTalk(    #63
        0xFE,
        (
            "I just cannot believe that Mr. Trino\x01",
            "was on that airliner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "No matter how much of a rival he is,\x01",
            "we've still known him for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "I just hope he's safe...\x02",
    )

    CloseMessageWindow()

    label("loc_1A96")

    Jump("loc_1C7D")

    label("loc_1A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_1BD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B8B")
    OP_A2(0x1)

    ChrTalk(    #66
        0xFE,
        (
            "It wasn't all that long ago that\x01",
            "Ms. Mirano used to be a cute\x01",
            "little girl who came to visit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "But now she's a fierce business rival.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "I sure hope that my little Alvelle will\x01",
            "have that kind of backbone too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD0")

    label("loc_1B8B")


    ChrTalk(    #69
        0xFE,
        (
            "I hope my son will have razor-sharp\x01",
            "business sense like Mirano.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BD0")

    Jump("loc_1C7D")

    label("loc_1BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1C7D")

    ChrTalk(    #70
        0xFE,
        (
            "It's certainly been a while since the\x01",
            "army clamped down on things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "And at this point, because of it,\x01",
            "we're definitely going to be in\x01",
            "the red this month.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C7D")

    TalkEnd(0x9)
    Return()

    # Function_8_1379 end

    def Function_9_1C81(): pass

    label("Function_9_1C81")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1DE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D67")
    OP_A2(0x2)

    ChrTalk(    #72
        0xFE,
        (
            "At the Jenis Royal Academy in Ruan\x01",
            "there's a subject called social studies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "In it you focus exclusively on politics and\x01",
            "economics, so I'm sure even my dad would\x01",
            "understand why I want to go there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE6")

    label("loc_1D67")


    ChrTalk(    #74
        0xFE,
        (
            "I'm sure that even my dad would understand\x01",
            "why I want to go to the royal academy if it\x01",
            "was for the social studies course.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE6")

    Jump("loc_247A")

    label("loc_1DE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1F09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E99")
    OP_A2(0x2)

    ChrTalk(    #75
        0xFE,
        (
            "Umm, I wonder when I should tell my\x01",
            "parents about wanting to enter the\x01",
            "royal academy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "Unfortunately, right now doesn't\x01",
            "seem to be a good time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F06")

    label("loc_1E99")


    ChrTalk(    #77
        0xFE,
        (
            "But if I can't get my parents to\x01",
            "cover my tuition, I can't pay...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "This really puts me in a bind...\x02",
    )

    CloseMessageWindow()

    label("loc_1F06")

    Jump("loc_247A")

    label("loc_1F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_2032")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC7")
    OP_A2(0x2)

    ChrTalk(    #79
        0xFE,
        (
            "There were some burglaries\x01",
            "around here yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "It seems like my mom saw\x01",
            "the culprits, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "The army was asking about it\x01",
            "until just a little while ago.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_202F")

    label("loc_1FC7")


    ChrTalk(    #82
        0xFE,
        (
            "There were some burglaries\x01",
            "around here yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "It seems like my mom saw\x01",
            "the culprits, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_202F")

    Jump("loc_247A")

    label("loc_2032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20AE")
    TurnDirection(0x13, 0x0, 0)

    ChrTalk(    #84
        0x13,
        (
            "We'll be done with our questioning\x01",
            "here soon, so how about sitting\x01",
            "tight until we finish?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 0, 0)
    Jump("loc_247A")

    label("loc_20AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2117")

    ChrTalk(    #85
        0xFE,
        (
            "It seems like my mom saw\x01",
            "the culprits, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "I wonder what Mirano is doing\x01",
            "right now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_247A")

    label("loc_2117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2239")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E3")
    OP_A2(0x2)

    ChrTalk(    #87
        0xFE,
        (
            "I heard that Mister Trino was riding\x01",
            "that airship that went missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "I know he's my dad's business rival,\x01",
            "but he's still Mirano's father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "I'm really worried about him.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2236")

    label("loc_21E3")


    ChrTalk(    #90
        0xFE,
        (
            "I wonder if Mirano is worried about\x01",
            "her father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "I sure hope he's safe...\x02",
    )

    CloseMessageWindow()

    label("loc_2236")

    Jump("loc_247A")

    label("loc_2239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2350")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2314")
    OP_A2(0x2)

    ChrTalk(    #92
        0xFE,
        (
            "My mom and dad are always telling\x01",
            "me to watch and learn from Mirano.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "But...I really don't have any\x01",
            "intention of being a merchant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "I want to go to Ruan and study\x01",
            "at the royal academy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_234D")

    label("loc_2314")


    ChrTalk(    #95
        0xFE,
        (
            "Mirano used to tease me a lot\x01",
            "when I was younger...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_234D")

    Jump("loc_247A")

    label("loc_2350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_247A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2406")
    OP_A2(0x2)

    ChrTalk(    #96
        0xFE,
        "My dad works in the trade business.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "And our family has been doing the\x01",
            "same job for generations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "But...I don't think I'm cut out to\x01",
            "be a merchant.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_247A")

    label("loc_2406")


    ChrTalk(    #99
        0xFE,
        (
            "Our family has been doing the\x01",
            "same job for generations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "But...I don't think I'm cut out to\x01",
            "be a merchant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_247A")

    TalkEnd(0xA)
    Return()

    # Function_9_1C81 end

    def Function_10_247E(): pass

    label("Function_10_247E")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_24C9")

    ChrTalk(    #101
        0xFE,
        (
            "Let's see, I wonder what I should\x01",
            "go fishing for next...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A8E")

    label("loc_24C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2599")

    ChrTalk(    #102
        0xFE,
        (
            "The Kingfisher Inn can be reached by\x01",
            "heading south from town and following\x01",
            "the New Ansel Path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "The structure's been built right on the\x01",
            "lake shore, so you'll know it as soon\x01",
            "as you see it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A8E")

    label("loc_2599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2607")
    OP_A2(0x32D)
    OP_28(0x37, 0x1, 0x1)

    ChrTalk(    #104
        0x12,
        (
            "I'm not trying to be rude, but this\x01",
            "is an official investigation. Move\x01",
            "it along.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A8E")

    label("loc_2607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2762")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26E3")
    OP_A2(0x3)

    ChrTalk(    #105
        0xFE,
        (
            "Men, no matter how old they get,\x01",
            "have a little childish part in them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "A part that makes them always\x01",
            "want to chase after their dreams.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "Too bad that women can't seem\x01",
            "to understand this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_275F")

    label("loc_26E3")


    ChrTalk(    #108
        0xFE,
        (
            "A part that makes them always\x01",
            "want to chase after their dreams.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "Too bad that women can't seem\x01",
            "to understand this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_275F")

    Jump("loc_2A8E")

    label("loc_2762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_28F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2868")
    OP_A2(0x3)

    ChrTalk(    #110
        0xFE,
        (
            "If you head south from Bose,\x01",
            "you'll arrive at the north shore\x01",
            "of Valleria Lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "Valleria Lake is, as you know,\x01",
            "the massive body of water in the\x01",
            "center of the kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "And fish of all kinds swim around\x01",
            "in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "Heehee...\x02",
    )

    CloseMessageWindow()
    Jump("loc_28F5")

    label("loc_2868")


    ChrTalk(    #114
        0xFE,
        (
            "Valleria Lake is, as you know,\x01",
            "the massive body of water in the\x01",
            "center of the kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "And fish of all kinds swim around\x01",
            "in there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F5")

    Jump("loc_2A8E")

    label("loc_28F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2970")

    ChrTalk(    #116
        0xFE,
        "Why do you get angry so easily?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "Don't you realize that high blood-\x01",
            "pressure is bad for your health?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A8E")

    label("loc_2970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2A8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A68")
    OP_A2(0x3)

    ChrTalk(    #118
        0xFE,
        (
            "It's important for people to have\x01",
            "hobbies in their old age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "So I don't see why you have to\x01",
            "get so mad about mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "Don't you realize you're just going\x01",
            "to turn into a wrinkled old prune\x01",
            "getting angry all the time?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A8E")

    label("loc_2A68")


    ChrTalk(    #121
        0xFE,
        "Oh, now that was a scary look...\x02",
    )

    CloseMessageWindow()

    label("loc_2A8E")

    TalkEnd(0xB)
    Return()

    # Function_10_247E end

    def Function_11_2A92(): pass

    label("Function_11_2A92")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2B0C")

    ChrTalk(    #122
        0xFE,
        (
            "All he's been doing for the last\x01",
            "20 years is fishing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "I can't see how he doesn't get\x01",
            "sick of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4286")

    label("loc_2B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2C91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C3D")
    OP_A2(0x4)

    ChrTalk(    #124
        0xFE,
        (
            "No matter how many times I yell at\x01",
            "my husband about his addiction,\x01",
            "he still takes off to go fishing again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "I'm just about ready to give up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "There's something that really gets my goat\x01",
            "about seeing him come walking through the\x01",
            "door with such a carefree look on his face.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C8E")

    label("loc_2C3D")


    ChrTalk(    #127
        0xFE,
        (
            "But I guess it does help out at\x01",
            "the dinner table when he catches\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C8E")

    Jump("loc_4286")

    label("loc_2C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_3F49")
    OP_A2(0x33A)
    OP_28(0x37, 0x1, 0x10)
    OP_28(0x37, 0x1, 0x20)
    OP_28(0x37, 0x1, 0x40)
    OP_28(0x37, 0x1, 0x80)
    OP_28(0x38, 0x4, 0x2)
    OP_28(0x38, 0x4, 0x4)
    EventBegin(0x0)
    OP_69(0xFE, 0x3E8)

    ChrTalk(    #128
        0xFE,
        "Oh, dear me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "Weren't you the bracers who came\x01",
            "to ask questions not that long ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        "#000FOh, right. We did come before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "I'm really sorry I couldn't talk\x01",
            "to you then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "So what you came to ask about is\x01",
            "what happened last night, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x102,
        (
            "#010FYes, that's right. Is this a good\x01",
            "time for you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "Yeah, this is as good a time\x01",
            "as any.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -19910, -150, 1594, 180)
    SetChrPos(0x101, -18365, 0, 850, 270)
    SetChrPos(0x102, -18365, 0, -120, 315)
    SetChrPos(0x103, -20410, 0, -950, 0)
    SetChrPos(0x104, -19334, 0, -950, 0)
    OP_6D(-19459, 0, 700, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #135
        0xFE,
        (
            "It was the middle of the night,\x01",
            "you see, when I heard a noise\x01",
            "coming from outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "And I, of course, thought it was my husband\x01",
            "coming home at such a late hour, so I opened\x01",
            "the door and started yelling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "But it turned out to be a group of\x01",
            "masked men coming out of the\x01",
            "orbal factory across the road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "I thought my heart was plum gonna\x01",
            "stop right then and there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "Although it turned out the burglars\x01",
            "were rather surprised and ran away\x01",
            "to the north.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        (
            "#006FI see...so it was the sky bandits,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x102,
        (
            "#010FSo, what you're saying then, is\x01",
            "that this house didn't incur a\x01",
            "loss of any kind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "Yeah, thanks to the mercy\x01",
            "of the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x103,
        (
            "#020FCan I ask you another thing?\x02\x03",

            "Did your husband coming home late\x01",
            "mean that he went to the bar?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "If it was only that, that would be\x01",
            "forgivable...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "In addition to being a no-good\x01",
            "drinker, he's obsessed with this.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #146
        "\x07\x05Cecile raised her hand in a casting motion.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #147
        0x103,
        "#023F???\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        (
            "#001FOh, I get it!\x02\x03",

            "You mean fishing, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x103,
        "#020FI see now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "That's right! He loves fishing\x01",
            "more than life itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "Just yesterday he said something\x01",
            "about catching some smelt and\x01",
            "took off to the lake in the south.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "And on top of that, he still\x01",
            "hasn't come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        (
            "#004FEh? So what you're saying\x01",
            "is...he doesn't know any-\x01",
            "thing about the incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        "That's exactly what I'm saying.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "And when that good-for-nothing husband\x01",
            "of mine gets home, he's going to get\x01",
            "what-for, let me tell you!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xB, -19980, 0, -5070, 0)

    NpcTalk(    #156
        0xB,
        "Old Man's Voice",
        "#1PHi, honey, I'm home!\x02",
    )

    CloseMessageWindow()

    def lambda_34F5():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_34F5)

    def lambda_3503():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3503)

    def lambda_3511():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3511)

    def lambda_351F():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_351F)
    OP_4A(0xB, 255)
    SetChrFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x80)
    OP_22(0x6, 0x0, 0x64)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_354B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_354B)
    OP_8E(0xB, 0xFFFFAFEC, 0x0, 0xFFFFF5AB, 0x7D0, 0x0)

    def lambda_3571():

        label("loc_3571")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_3571")

    QueueWorkItem2(0x0, 1, lambda_3571)

    def lambda_3582():

        label("loc_3582")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_3582")

    QueueWorkItem2(0x1, 1, lambda_3582)

    def lambda_3593():

        label("loc_3593")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_3593")

    QueueWorkItem2(0x2, 1, lambda_3593)

    def lambda_35A4():

        label("loc_35A4")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_35A4")

    QueueWorkItem2(0x3, 1, lambda_35A4)

    ChrTalk(    #157
        0xB,
        "Whew, what a day I had...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xB,
        (
            "I was fishing patiently all morning,\x01",
            "but I have nothing to show for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xB,
        (
            "Oh, what's this?\x01",
            "Do we have guests?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    def lambda_3666():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3666)

    ChrTalk(    #160
        0xFE,
        "#5SYou senile old man!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #161
        0xB,
        (
            "My goodness, woman!\x01",
            "What kind of fiery tempest\x01",
            "has gotten into you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xB,
        (
            "Don't you know it's rude to act\x01",
            "like that in front of guests?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "If anyone's being rude,\x01",
            "that would be you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "I'm dumbfounded that my own\x01",
            "husband can just take off to do\x01",
            "what he likes at a time like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xB,
        (
            "Huh? What do you meant by\x01",
            "'a time like this'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x102,
        "#010FMaybe I should explain...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #167
        (
            "\x07\x05Joshua gave Mr. Kuwano a brief explanation regarding the burglaries which\x01",
            "transpired the previous night.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrFlags(0xB, 0x40)
    SetChrPos(0xB, -21250, 50, 300, 90)
    SetChrChipByIndex(0xB, 12)
    SetChrSubChip(0xB, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #168
        0xB,
        (
            "Burglaries by sky bandits? You\x01",
            "don't say? Now that IS terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xB,
        (
            "But to think that they hightailed it\x01",
            "out of here after my wife hollered\x01",
            "at them is hilarious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xB,
        (
            "Ha ha ha! Guess they got to experience\x01",
            "the 'Cecile effect' first-hand!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        "What did you just say?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x101,
        "#004FL-Let's all calm down now, shall we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xB,
        (
            "But to think that these sky bandits\x01",
            "came in the night like they did and\x01",
            "then just disappeared like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xB,
        (
            "I wonder if it has anything to do\x01",
            "with that thing he was talking\x01",
            "about the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x102,
        "#014FHe...? What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xB,
        (
            "Oh, right. You don't know him.\x01",
            "'He' is my fishing buddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xB,
        (
            "He's staying at the inn down the\x01",
            "lakeshore to the south of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xB,
        (
            "If I remember right, he said some-\x01",
            "thing about seeing a strange bunch\x01",
            "near the place the other night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        "#002FA strange bunch...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x103,
        (
            "#020FNow, this sounds really interesting.\x01",
            "Can you tell us a little more about\x01",
            "what you've heard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xB,
        (
            "Sure, I don't mind, but I'm just\x01",
            "going to tell you up front that\x01",
            "this is all hearsay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xB,
        (
            "From what I heard, he just happened\x01",
            "to see them by chance as he was\x01",
            "out fishing during the night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xB,
        (
            "He saw them leave by way of\x01",
            "the inn's front door and then\x01",
            "out onto the road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xB,
        (
            "However, when he asked around at the inn\x01",
            "in the morning, it turned out that no one\x01",
            "like that had stayed there the night before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x102,
        (
            "#012FYeah, that is rather odd.\x02\x03",

            "So, was there any type of\x01",
            "burglary at the inn?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xB,
        (
            "No. Nothing of the sort at all,\x01",
            "in fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xB,
        (
            "It's quiet there, the meals are\x01",
            "great, and it's...well, a place\x01",
            "I'd recommend to anyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xB,
        "But best of all, it's a prime fishing spot.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_4286")

    label("loc_3F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FC5")
    OP_A2(0x32D)
    OP_28(0x37, 0x1, 0x1)
    TurnDirection(0x12, 0x0, 0)

    ChrTalk(    #189
        0x12,
        (
            "I'm not trying to be rude, but this\x01",
            "is an official investigation. Move\x01",
            "it along.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 315, 0)
    Jump("loc_4286")

    label("loc_3FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_4032")

    ChrTalk(    #190
        0xFE,
        (
            "Sometimes I wonder why I\x01",
            "ever married my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "This was the worst mistake of\x01",
            "my life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4286")

    label("loc_4032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_40B4")

    ChrTalk(    #192
        0xFE,
        (
            "You should steer clear from\x01",
            "talking to my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "Get him started and he'll just\x01",
            "fill your ear with rubbish.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4286")

    label("loc_40B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_4170")

    ChrTalk(    #194
        0xFE,
        (
            "I swear, my good for nothing\x01",
            "husband...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "He takes off without a word and\x01",
            "doesn't come home for hours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "Whenever he takes off, he's gone,\x01",
            "and who knows for how long!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4286")

    label("loc_4170")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_4286")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4235")
    OP_A2(0x4)
    OP_62(0xFE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #197
        0xFE,
        "But that's not what I'm mad about!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "The thing I'm mad about is the fact\x01",
            "that he doesn't have the decency\x01",
            "to say one word before he leaves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4286")

    label("loc_4235")


    ChrTalk(    #199
        0xFE,
        (
            "How many years does he expect\x01",
            "me to keep yelling at him for\x01",
            "the same thing?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4286")

    TalkEnd(0xC)
    Return()

    # Function_11_2A92 end

    def Function_12_428A(): pass

    label("Function_12_428A")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_4398")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_433A")
    OP_A2(0x5)

    ChrTalk(    #200
        0xFE,
        (
            "My husband who was abducted by\x01",
            "sky bandits came home safely!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        "I am so relieved...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "And thankful to the Goddess\x01",
            "Aidios for his safe return.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4395")

    label("loc_433A")


    ChrTalk(    #203
        0xFE,
        (
            "My husband who was abducted by\x01",
            "sky bandits came home safely!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        "I am so relieved...\x02",
    )

    CloseMessageWindow()

    label("loc_4395")

    Jump("loc_4C52")

    label("loc_4398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_442E")

    ChrTalk(    #205
        0xFE,
        (
            "I know my husband is always out and\x01",
            "about, but not having him around \x01",
            "makes me feel a little insecure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        "Please...come home safely.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C52")

    label("loc_442E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_45C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4523")
    OP_A2(0x5)

    ChrTalk(    #207
        0xFE,
        (
            "Fortunately, this house was\x01",
            "untouched in the burglaries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "But it's at times like this that it\x01",
            "makes you feel uneasy when\x01",
            "there's no man at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "I'm just glad that Mirano brought\x01",
            "Simon over to watch the house.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45C1")

    label("loc_4523")


    ChrTalk(    #210
        0xFE,
        (
            "It's at times like this that it\x01",
            "makes you feel uneasy when\x01",
            "there's no man at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "I'm just glad that Mirano brought\x01",
            "Simon over to watch the house.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45C1")

    Jump("loc_4C52")

    label("loc_45C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_47B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4743")
    OP_A2(0x5)

    ChrTalk(    #212
        0xFE,
        (
            "Borden's wife helps him with\x01",
            "the business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "I have tried to help my husband a few\x01",
            "times with his work, but let's just say\x01",
            "that the results weren't great...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "It looks like I'm best cut out\x01",
            "for supporting my husband and\x01",
            "Mirano here at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "I'm sure that my husband's gonna\x01",
            "walk through that door any minute\x01",
            "with a nonchalant look on his face...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47B1")

    label("loc_4743")


    ChrTalk(    #216
        0xFE,
        (
            "I'm sure that my husband's gonna\x01",
            "walk through that door any minute\x01",
            "with a nonchalant look on his face...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47B1")

    Jump("loc_4C52")

    label("loc_47B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_4A2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4990")
    OP_A2(0x5)

    ChrTalk(    #217
        0xFE,
        (
            "Some people think that Mirano\x01",
            "and my husband are on bad\x01",
            "terms with each other...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "But that's not the case. They are\x01",
            "just competitive, that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "I don't think people should expect\x01",
            "anything less. Mirano is his daughter,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "I know it seems like Mirano is complaining\x01",
            "as she goes about taking on her father's work,\x01",
            "but that's just her way of showing compassion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "I really appreciate her being\x01",
            "considerate at a time like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A2B")

    label("loc_4990")


    ChrTalk(    #222
        0xFE,
        (
            "Some people think that Mirano\x01",
            "and my husband are on bad\x01",
            "terms with each other...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "But that's not the case. They are\x01",
            "just competitive, that's all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A2B")

    Jump("loc_4C52")

    label("loc_4A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_4B0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AB3")
    OP_A2(0x5)

    ChrTalk(    #224
        0xFE,
        "I can't believe it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "My husband was on the\x01",
            "airliner that disappeared...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        "Wh-What should I do...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B08")

    label("loc_4AB3")


    ChrTalk(    #227
        0xFE,
        (
            "My husband was on the\x01",
            "airliner that disappeared...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        "Wh-What should I do...?\x02",
    )

    CloseMessageWindow()

    label("loc_4B08")

    Jump("loc_4C52")

    label("loc_4B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_4C52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BFC")
    OP_A2(0x5)

    ChrTalk(    #229
        0xFE,
        "That's strange...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "I would have thought that my husband\x01",
            "would be home by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "With my daughter at home now, it seems\x01",
            "like we can finally enjoy a meal together\x01",
            "as a family for the first time in ages, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C52")

    label("loc_4BFC")


    ChrTalk(    #232
        0xFE,
        (
            "Could my husband have gotten\x01",
            "in an accident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        "I'm starting to get worried...\x02",
    )

    CloseMessageWindow()

    label("loc_4C52")

    TalkEnd(0xD)
    Return()

    # Function_12_428A end

    def Function_13_4C56(): pass

    label("Function_13_4C56")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_4CE9")

    ChrTalk(    #234
        0xFE,
        (
            "My bossy father made it back\x01",
            "home in one piece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "If I hadn't had to take care of his work,\x01",
            "I could have been in Ruan by now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55C5")

    label("loc_4CE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_4E47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE9")
    OP_A2(0x6)

    ChrTalk(    #236
        0xFE,
        (
            "According to the mayor, the missing\x01",
            "airliner was hijacked by the sky bandits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "If it's a ransom they're after, then\x01",
            "my father is probably still alive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "I hope there's something I can do to\x01",
            "put my mother's worries at ease.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E44")

    label("loc_4DE9")


    ChrTalk(    #239
        0xFE,
        (
            "So you guys are here to\x01",
            "investigate the incident, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        "I'm counting on you guys!\x02",
    )

    CloseMessageWindow()

    label("loc_4E44")

    Jump("loc_55C5")

    label("loc_4E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_4FA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F3F")
    OP_A2(0x6)

    ChrTalk(    #241
        0xFE,
        (
            "Now we've got burglars running\x01",
            "amok in the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        "I swear, what's happening to Bose?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "I'm just glad they left this house alone.\x01",
            "Though I'm baffled as to why! They certainly\x01",
            "didn't do their homework on this city...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F9D")

    label("loc_4F3F")


    ChrTalk(    #244
        0xFE,
        (
            "Now we've got burglars running\x01",
            "amok in the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        "I swear, what's happening to Bose?\x02",
    )

    CloseMessageWindow()

    label("loc_4F9D")

    Jump("loc_55C5")

    label("loc_4FA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_5156")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50BF")
    OP_A2(0x6)

    ChrTalk(    #246
        0xFE,
        (
            "Having the flights stopped has actually\x01",
            "turned out to be good for business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "I'm actually able to earn quite a lot\x01",
            "more with my father temporarily\x01",
            "out of the picture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "But I'll try to pick up as much of\x01",
            "the slack as I can for his work\x01",
            "during this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5153")

    label("loc_50BF")


    ChrTalk(    #249
        0xFE,
        (
            "Because I originally got my own\x01",
            "business started by helping him\x01",
            "out like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "I basically know the way Simon\x01",
            "thinks and how he'll act.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5153")

    Jump("loc_55C5")

    label("loc_5156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_52EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5261")
    OP_A2(0x6)

    ChrTalk(    #251
        0xFE,
        (
            "And this is why I'd like to leave my\x01",
            "father's business deals to him, but\x01",
            "he's still a little inexperienced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "And he might end up playing into\x01",
            "the hands of our rival, Borden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "But I need some help, so I'll\x01",
            "probably call on him later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52EB")

    label("loc_5261")


    ChrTalk(    #254
        0xFE,
        "Trust is the first rule of business.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "And I can't have my own name being\x01",
            "dragged through the mud because\x01",
            "my father's not around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52EB")

    Jump("loc_55C5")

    label("loc_52EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_5413")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53E1")
    OP_A2(0x6)

    ChrTalk(    #256
        0xFE,
        (
            "I heard that my father was on the\x01",
            "airliner that went missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "I wonder what my father is going to\x01",
            "do about his business deals now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        (
            "Maybe we should be worried about\x01",
            "whether or not he's still alive instead...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5410")

    label("loc_53E1")


    ChrTalk(    #259
        0xFE,
        (
            "I swear, making Mother worry\x01",
            "like that...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5410")

    Jump("loc_55C5")

    label("loc_5413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_55C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_553B")
    OP_A2(0x6)

    ChrTalk(    #260
        0xFE,
        (
            "I come all the way back here to\x01",
            "be with the family and my\x01",
            "father's nowhere to be found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "And he's the one who said to come\x01",
            "back to Bose as soon as possible.\x01",
            "What's going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        (
            "My mother's worried, so maybe I'll\x01",
            "just give a call to the place where\x01",
            "he was staying.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55C5")

    label("loc_553B")


    ChrTalk(    #263
        0xFE,
        (
            "I come all the way back here to\x01",
            "be with the family and my\x01",
            "father's nowhere to be found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        "It's not like him to be late like this.\x02",
    )

    CloseMessageWindow()

    label("loc_55C5")

    TalkEnd(0xE)
    Return()

    # Function_13_4C56 end

    def Function_14_55C9(): pass

    label("Function_14_55C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x13, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x13, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x13, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14E)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55EF")
    Call(0, 21)
    Jump("loc_5E4D")

    label("loc_55EF")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_5705")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5681")

    ChrTalk(    #265
        0xFE,
        "I'm so grateful to all of you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        (
            "With the sky bandits behind\x01",
            "bars it looks like I can\x01",
            "finally get back to my life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5702")

    label("loc_5681")


    ChrTalk(    #267
        0xFE,
        (
            "I heard the masked men who broke\x01",
            "into our place were apprehended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        (
            "Do you think I can get back\x01",
            "what they stole from me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5702")

    Jump("loc_5E4A")

    label("loc_5705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_580B")

    ChrTalk(    #269
        0xFE,
        (
            "I had a very important ring taken\x01",
            "by them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "I don't care if it's the army or the\x01",
            "Bracer Guild, I just want to see\x01",
            "those burglars caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        (
            "If these sky bandits are on the loose,\x01",
            "I don't think I can live without being in\x01",
            "fear every day...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E4A")

    label("loc_580B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5870")
    TurnDirection(0x14, 0x0, 0)

    ChrTalk(    #272
        0x14,
        (
            "I'm going to be done here in a minute,\x01",
            "so would you kids butt out?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14, 0, 0)
    Jump("loc_5E4A")

    label("loc_5870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_59FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_597E")
    OP_A2(0x7)

    ChrTalk(    #273
        0xFE,
        (
            "I was putting my son to bed \x01",
            "last night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        (
            "When suddenly some masked\x01",
            "men kicked in the door and\x01",
            "came storming in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        (
            "I didn't tell my husband because\x01",
            "I didn't want him to worry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        (
            "But my ring, which was from\x01",
            "my mother, was taken...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59FB")

    label("loc_597E")


    ChrTalk(    #277
        0xFE,
        (
            "I didn't tell my husband because\x01",
            "I didn't want him to worry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        (
            "But my ring, which was from\x01",
            "my mother, was taken...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59FB")

    Jump("loc_5E4A")

    label("loc_59FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_5A9D")

    ChrTalk(    #279
        0xFE,
        (
            "It looks like my husband's business\x01",
            "is doing better than expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        (
            "Recently I've noticed a vibrant look\x01",
            "in his face, so I'm happy for him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E4A")

    label("loc_5A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_5C75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BD2")
    OP_A2(0x7)

    ChrTalk(    #281
        0xFE,
        (
            "Ever since my husband opened\x01",
            "his business, he's had more\x01",
            "time at home as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "Of course, he keeps the books and\x01",
            "manages his goods at home, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        (
            "When he was in the army he only\x01",
            "managed to get home about once\x01",
            "a week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "My husband opening his store\x01",
            "hasn't been all bad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C72")

    label("loc_5BD2")


    ChrTalk(    #285
        0xFE,
        (
            "Ever since my husband opened\x01",
            "his business, he's had more\x01",
            "time at home as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "When he was in the army he only\x01",
            "managed to get home about once\x01",
            "a week.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C72")

    Jump("loc_5E4A")

    label("loc_5C75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_5E00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D51")
    OP_A2(0x7)

    ChrTalk(    #287
        0xFE,
        (
            "My husband resigned from his post\x01",
            "in the Royal Army and started a\x01",
            "business in the Bose Market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        "But I'm against it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        (
            "I at least wish he would have done\x01",
            "this when Elke was a bit older.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DFD")

    label("loc_5D51")


    ChrTalk(    #290
        0xFE,
        (
            "My husband resigned from his post\x01",
            "in the Royal Army and started a\x01",
            "business in the Bose Market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        (
            "I at least wish he would have done\x01",
            "this when Elke was a bit older.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DFD")

    Jump("loc_5E4A")

    label("loc_5E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_5E4A")

    ChrTalk(    #292
        0xFE,
        "Whew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        (
            "I wonder if my husband's business\x01",
            "is doing well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E4A")

    TalkEnd(0x10)

    label("loc_5E4D")

    Return()

    # Function_14_55C9 end

    def Function_15_5E4E(): pass

    label("Function_15_5E4E")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_5EE8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5E9E")

    ChrTalk(    #294
        0xFE,
        (
            "My mom looks like she's happier\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        "I'm glad.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5EE5")

    label("loc_5E9E")


    ChrTalk(    #296
        0xFE,
        (
            "All the people around town look\x01",
            "happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        "But my mom looks sad.\x02",
    )

    CloseMessageWindow()

    label("loc_5EE5")

    Jump("loc_6253")

    label("loc_5EE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_5F4F")

    ChrTalk(    #298
        0xFE,
        (
            "I wonder if my dad will come\x01",
            "home soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "My mom looks really upset about\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6253")

    label("loc_5F4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FC8")
    TurnDirection(0x14, 0x0, 0)

    ChrTalk(    #300
        0x14,
        (
            "I'll be done here in a minute, so\x01",
            "would you kids mind keeping\x01",
            "your nose out of things?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14, 0, 0)
    Jump("loc_6253")

    label("loc_5FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_606B")
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #301
        0xFE,
        "U-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        (
            "A bunch of strangers came in\x01",
            "the house without asking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0xFE,
        (
            "My mom and I were scared, so\x01",
            "we hid under the bed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6253")

    label("loc_606B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_60C3")

    ChrTalk(    #304
        0xFE,
        (
            "I'm gonna visit my dad's shop\x01",
            "with my mom later on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        "I'm so excited.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6253")

    label("loc_60C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_616C")

    ChrTalk(    #306
        0xFE,
        (
            "My dad plays with me more now\x01",
            "than he did when he was a\x01",
            "soldier in the army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xFE,
        (
            "I like the way my dad is now.\x01",
            "Before he used to get angry\x01",
            "all the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6253")

    label("loc_616C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_61E9")

    ChrTalk(    #308
        0xFE,
        (
            "One day when I get older I'm\x01",
            "gonna help my dad make clothes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        (
            "I'm going to work with my dad\x01",
            "at his store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6253")

    label("loc_61E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_6253")

    ChrTalk(    #310
        0xFE,
        (
            "My dad makes clothes and then\x01",
            "sells them to the people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0xFE,
        (
            "He made my clothes, too.\x01",
            "Seeeee?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6253")

    TalkEnd(0x11)
    Return()

    # Function_15_5E4E end

    def Function_16_6257(): pass

    label("Function_16_6257")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_636B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_630A")
    OP_A2(0x9)

    ChrTalk(    #312
        0xFE,
        (
            "Mirano had an errand and went\x01",
            "to the mayor's residence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0xFE,
        (
            "The mayor and Mirano have actually\x01",
            "been good friends for as long as\x01",
            "anyone can remember.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6368")

    label("loc_630A")


    ChrTalk(    #314
        0xFE,
        (
            "The mayor and Mirano have actually\x01",
            "been good friends for as long as\x01",
            "anyone can remember.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6368")

    Jump("loc_63EF")

    label("loc_636B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_63EF")

    ChrTalk(    #315
        0xFE,
        (
            "I was shocked when I heard about the\x01",
            "south block being hit by burglars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xFE,
        (
            "Mirano's mother was here alone,\x01",
            "you see...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63EF")

    TalkEnd(0xF)
    Return()

    # Function_16_6257 end

    def Function_17_63F3(): pass

    label("Function_17_63F3")

    OP_A2(0x32D)
    OP_28(0x37, 0x1, 0x1)
    TalkBegin(0x12)

    ChrTalk(    #317
        0xFE,
        (
            "I'm trying to ask a few questions here.\x01",
            "Would you mind getting out of the way?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_17_63F3 end

    def Function_18_6457(): pass

    label("Function_18_6457")

    TalkBegin(0x13)

    ChrTalk(    #318
        0xFE,
        (
            "Are you bracers here to ask a\x01",
            "few questions yourselves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0xFE,
        (
            "This is a mess for the both of us,\x01",
            "I tell you.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_18_6457 end

    def Function_19_64CF(): pass

    label("Function_19_64CF")

    TalkBegin(0x14)

    ChrTalk(    #320
        0xFE,
        (
            "The woman living here said that\x01",
            "she had a precious memento\x01",
            "taken by these crooks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xFE,
        (
            "Oops, me and my big mouth...\x01",
            "Let's pretend like I didn't just\x01",
            "tell you that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0xFE,
        (
            "What I mean to say is, why don't\x01",
            "you just ask her about it after I\x01",
            "get done here?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x14)
    Return()

    # Function_19_64CF end

    def Function_20_65D6(): pass

    label("Function_20_65D6")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_66FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66D9")
    OP_A2(0xA)

    ChrTalk(    #323
        0xFE,
        (
            "I finally made it back to my\x01",
            "lovely home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0xFE,
        (
            "After being locked up in a dank\x01",
            "and dirty cell, my home feels\x01",
            "like paradise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0xFE,
        (
            "It looks like Mirano picked up the\x01",
            "slack while I was away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0xFE,
        "So, it's time to get back to work!\x02",
    )

    CloseMessageWindow()
    Jump("loc_66FD")

    label("loc_66D9")


    ChrTalk(    #327
        0xFE,
        "It's time to get back to work!\x02",
    )

    CloseMessageWindow()

    label("loc_66FD")

    TalkEnd(0x15)
    Return()

    # Function_20_65D6 end

    def Function_21_6701(): pass

    label("Function_21_6701")

    EventBegin(0x0)
    SetChrFlags(0x10, 0x10)
    TalkBegin(0x10)
    TurnDirection(0x0, 0x10, 0)
    TurnDirection(0x1, 0x10, 0)

    ChrTalk(    #328
        0x101,
        "#000FExcuse me, you're Launa, right?\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #329
        0x10,
        "Yes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x10,
        (
            "Is there something I can help\x01",
            "you with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x101,
        (
            "#000FActually we found a ring that looks\x01",
            "something like the one mentioned\x01",
            "in the job request at the guild.\x02\x03",

            "If we could, we'd like to have you\x01",
            "take a look at it...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #332
        0x10,
        "Really?! Truly?!\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #333
        "\x07\x00Handed over \x07\x02Jeweled Ring\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10)

    ChrTalk(    #334
        0x10,
        "Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x10,
        (
            "Who would've ever thought this would\x01",
            "have come back to me like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x102,
        (
            "#010FSo there is no doubt that this\x01",
            "is the ring that was stolen?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(    #337
        0x10,
        (
            "No, this is the one that was\x01",
            "stolen, all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x10,
        (
            "It was a memento from my mother.\x01",
            "I would know it anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x101,
        (
            "#000FI see...\x02\x03",

            "It must be really important to\x01",
            "you then, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #340
        0x10,
        (
            "I had almost believed that I would\x01",
            "never see it again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x10,
        (
            "I don't know how I can ever repay\x01",
            "you for finding this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x101,
        (
            "#001FTee hee, I'm just glad we could help.\x02\x03",

            "So I guess our work here is done,\x01",
            "unless there's something else?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x10,
        (
            "No, that's all. And once again,\x01",
            "thank you for finding this for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x102,
        (
            "#010FWell then, if that's all, we'll leave\x01",
            "you to your business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x101,
        "#000FHave a nice day.\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #346
        "\x07\x00Quest \x07\x02[Stolen Ring] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x14E, 1)
    OP_28(0x13, 0x4, 0x10)
    OP_28(0x13, 0x1, 0x1)
    EventEnd(0x1)
    ClearChrFlags(0x10, 0x10)
    TalkEnd(0x10)
    Return()

    # Function_21_6701 end

    SaveToFile()

Try(main)
