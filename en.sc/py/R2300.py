from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R2300   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2300.x',
        MapIndex            = 102,
        MapDefaultBGM       = "ed60021",
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
        'Mickey',                               # 9
        'Blade Cougar',                         # 10
        'Blade Cougar',                         # 11
        'Gull Seaside Way',                     # 12
        'Jenis Royal Academy',                  # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
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
        'ED6_DT09/CH10520 ._CH',             # 00
        'ED6_DT09/CH10521 ._CH',             # 01
        'ED6_DT29/CH12040 ._CH',             # 02
        'ED6_DT29/CH12041 ._CH',             # 03
        'ED6_DT09/CH10340 ._CH',             # 04
        'ED6_DT09/CH10341 ._CH',             # 05
        'ED6_DT09/CH11040 ._CH',             # 06
        'ED6_DT09/CH11041 ._CH',             # 07
        'ED6_DT09/CH11070 ._CH',             # 08
        'ED6_DT09/CH11071 ._CH',             # 09
        'ED6_DT09/CH11080 ._CH',             # 0A
        'ED6_DT09/CH11081 ._CH',             # 0B
        'ED6_DT07/CH01080 ._CH',             # 0C
        'ED6_DT29/CH12900 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT09/CH10520P._CP',             # 00
        'ED6_DT09/CH10521P._CP',             # 01
        'ED6_DT29/CH12040P._CP',             # 02
        'ED6_DT29/CH12041P._CP',             # 03
        'ED6_DT09/CH10340P._CP',             # 04
        'ED6_DT09/CH10341P._CP',             # 05
        'ED6_DT09/CH11040P._CP',             # 06
        'ED6_DT09/CH11041P._CP',             # 07
        'ED6_DT09/CH11070P._CP',             # 08
        'ED6_DT09/CH11071P._CP',             # 09
        'ED6_DT09/CH11080P._CP',             # 0A
        'ED6_DT09/CH11081P._CP',             # 0B
        'ED6_DT07/CH01080P._CP',             # 0C
        'ED6_DT29/CH12900P._CP',             # 0D
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -31370,
        Z                   = 0,
        Y                   = 1980,
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
        X                   = 119440,
        Z                   = 0,
        Y                   = -7810,
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


    DeclMonster(
        X                   = 8930,
        Z                   = 370,
        Y                   = 11870,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x191,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 55220,
        Z                   = -110,
        Y                   = 8450,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x195,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 87920,
        Z                   = 100,
        Y                   = 10050,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x193,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 93230,
        Z                   = 60,
        Y                   = 5930,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x194,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -11190,
        Y                   = -1000,
        Z                   = -5490,
        Range               = -8710,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x189C,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )


    ScpFunction(
        "Function_0_24A",          # 00, 0
        "Function_1_24B",          # 01, 1
        "Function_2_28D",          # 02, 2
        "Function_3_3D2",          # 03, 3
        "Function_4_503",          # 04, 4
        "Function_5_50C",          # 05, 5
        "Function_6_101C",         # 06, 6
        "Function_7_19B0",         # 07, 7
        "Function_8_19D1",         # 08, 8
        "Function_9_19F8",         # 09, 9
        "Function_10_1A8B",        # 0A, 10
        "Function_11_1AE2",        # 0B, 11
        "Function_12_1B47",        # 0C, 12
        "Function_13_1BB5",        # 0D, 13
        "Function_14_1BEA",        # 0E, 14
        "Function_15_1C1F",        # 0F, 15
        "Function_16_1C54",        # 10, 16
        "Function_17_1CDA",        # 11, 17
    )


    def Function_0_24A(): pass

    label("Function_0_24A")

    Return()

    # Function_0_24A end

    def Function_1_24B(): pass

    label("Function_1_24B")

    OP_16(0x2, 0xFA0, 0xFFFEBBC8, 0xFFFE0C00, 0x230029)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x197), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_288")
    Call(0, 3)
    Jump("loc_28C")

    label("loc_288")

    Call(0, 2)

    label("loc_28C")

    Return()

    # Function_1_24B end

    def Function_2_28D(): pass

    label("Function_2_28D")

    OP_D2(0x2601B0, 0x2601B5, 0xE)
    OP_D2(0x2601B0, 0x2601B5, 0xF)
    OP_D2(0x270110, 0x270120, 0x10)
    OP_D2(0x270112, 0x270122, 0x11)
    OP_D2(0x270130, 0x270140, 0x12)
    OP_D2(0x270131, 0x270141, 0x13)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_2E2"),
        (5, "loc_2F9"),
        (6, "loc_310"),
        (7, "loc_327"),
        (SWITCH_DEFAULT, "loc_33E"),
    )


    label("loc_2E2")

    OP_D2(0x701D0, 0x701DC, 0x14)
    OP_D2(0x701D1, 0x701DD, 0x15)
    Jump("loc_33E")

    label("loc_2F9")

    OP_D2(0x70218, 0x70224, 0x14)
    OP_D2(0x70219, 0x70225, 0x15)
    Jump("loc_33E")

    label("loc_310")

    OP_D2(0x70230, 0x7023C, 0x14)
    OP_D2(0x70231, 0x7023D, 0x15)
    Jump("loc_33E")

    label("loc_327")

    OP_D2(0x70248, 0x70254, 0x14)
    OP_D2(0x70249, 0x70255, 0x15)
    Jump("loc_33E")

    label("loc_33E")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_357"),
        (5, "loc_36E"),
        (6, "loc_385"),
        (7, "loc_39C"),
        (SWITCH_DEFAULT, "loc_3B3"),
    )


    label("loc_357")

    OP_D2(0x701D0, 0x701DC, 0x16)
    OP_D2(0x701D1, 0x701DD, 0x17)
    Jump("loc_3B3")

    label("loc_36E")

    OP_D2(0x70218, 0x70224, 0x16)
    OP_D2(0x70219, 0x70225, 0x17)
    Jump("loc_3B3")

    label("loc_385")

    OP_D2(0x70230, 0x7023C, 0x16)
    OP_D2(0x70231, 0x7023D, 0x17)
    Jump("loc_3B3")

    label("loc_39C")

    OP_D2(0x70248, 0x70254, 0x16)
    OP_D2(0x70249, 0x70255, 0x17)
    Jump("loc_3B3")

    label("loc_3B3")

    OP_D2(0x290387, 0x29038B, 0x18)
    OP_D2(0x270111, 0x270121, 0x19)
    OP_D2(0x290389, 0x29038D, 0x1A)
    Return()

    # Function_2_28D end

    def Function_3_3D2(): pass

    label("Function_3_3D2")

    OP_D2(0x270110, 0x270120, 0xE)
    OP_D2(0x270110, 0x270120, 0xF)
    OP_D2(0x270110, 0x270120, 0x10)
    OP_D2(0x270110, 0x270120, 0x11)
    OP_D2(0x270130, 0x270140, 0x12)
    OP_D2(0x270130, 0x270140, 0x13)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_427"),
        (5, "loc_43E"),
        (6, "loc_455"),
        (7, "loc_46C"),
        (SWITCH_DEFAULT, "loc_483"),
    )


    label("loc_427")

    OP_D2(0x701D0, 0x701DC, 0x14)
    OP_D2(0x701D0, 0x701DC, 0x15)
    Jump("loc_483")

    label("loc_43E")

    OP_D2(0x70218, 0x70224, 0x14)
    OP_D2(0x70218, 0x70224, 0x15)
    Jump("loc_483")

    label("loc_455")

    OP_D2(0x70230, 0x7023C, 0x14)
    OP_D2(0x70230, 0x7023C, 0x15)
    Jump("loc_483")

    label("loc_46C")

    OP_D2(0x70248, 0x70254, 0x14)
    OP_D2(0x70248, 0x70254, 0x15)
    Jump("loc_483")

    label("loc_483")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_49C"),
        (5, "loc_4B3"),
        (6, "loc_4CA"),
        (7, "loc_4E1"),
        (SWITCH_DEFAULT, "loc_4F8"),
    )


    label("loc_49C")

    OP_D2(0x701D0, 0x701DC, 0x16)
    OP_D2(0x701D0, 0x701DC, 0x17)
    Jump("loc_4F8")

    label("loc_4B3")

    OP_D2(0x70218, 0x70224, 0x16)
    OP_D2(0x70218, 0x70224, 0x17)
    Jump("loc_4F8")

    label("loc_4CA")

    OP_D2(0x70230, 0x7023C, 0x16)
    OP_D2(0x70230, 0x7023C, 0x17)
    Jump("loc_4F8")

    label("loc_4E1")

    OP_D2(0x70248, 0x70254, 0x16)
    OP_D2(0x70248, 0x70254, 0x17)
    Jump("loc_4F8")

    label("loc_4F8")

    OP_D2(0x290387, 0x29038B, 0x18)
    Return()

    # Function_3_3D2 end

    def Function_4_503(): pass

    label("Function_4_503")

    Call(0, 5)
    Call(0, 6)
    Return()

    # Function_4_503 end

    def Function_5_50C(): pass

    label("Function_5_50C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_519")
    Return()

    label("loc_519")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_539")
    Call(0, 16)
    Call(0, 17)
    FadeToBright(0, 0)

    label("loc_539")

    OP_A3(0x2031)
    OP_A3(0x2032)
    OP_A3(0x2033)
    OP_A3(0x2034)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_555")
    OP_A2(0x2031)

    label("loc_555")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_565")
    OP_A2(0x2032)

    label("loc_565")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_575")
    OP_A2(0x2033)

    label("loc_575")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_585")
    OP_A2(0x2034)

    label("loc_585")

    Fade(1000)
    SetChrPos(0x101, -10370, 0, 1110, 90)
    SetChrPos(0x102, -10310, 0, 90, 90)
    SetChrPos(0xF9, -11900, 0, 1000, 90)
    SetChrPos(0xF8, -11900, 0, -440, 90)
    OP_6D(-10660, 0, 480, 0)
    OP_67(0, 8290, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    SetChrPos(0x8, 6950, -50, 900, 0)

    NpcTalk(    #0
        0x8,
        "Young Man's Voice",
        "#3PAAAAAAAAAAAAAH!\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AB")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6E9")

    label("loc_6AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D2")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6E9")

    label("loc_6D2")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6E9")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_715")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_753")

    label("loc_715")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73C")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_753")

    label("loc_73C")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_753")

    Sleep(1000)
    OP_21()
    OP_1D(0x29)
    Sleep(500)

    ChrTalk(    #1
        0x101,
        "#1004F#6PThat was...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        "#1042F#6PHurry, Estelle!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 25)
    SetChrChipByIndex(0x102, 18)
    SetChrChipByIndex(0xF9, 22)
    SetChrChipByIndex(0xF8, 20)
    SetChrFlags(0x101, 0x1000)

    def lambda_7B7():
        OP_91(0xFE, 0x2710, 0x0, 0x3E8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7B7)
    Sleep(100)

    def lambda_7D7():
        OP_91(0xFE, 0x2710, 0x0, 0x3E8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7D7)
    Sleep(20)

    def lambda_7F7():
        OP_91(0xFE, 0x2710, 0x0, 0x3E8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_7F7)
    Sleep(100)

    def lambda_817():
        OP_91(0xFE, 0x2710, 0x0, 0x3E8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_817)
    Sleep(1000)
    Fade(1000)
    OP_44(0x101, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xF9, 0x0)
    OP_44(0xF8, 0x0)
    SetChrChipByIndex(0x102, 18)
    SetChrChipByIndex(0xF9, 20)
    SetChrChipByIndex(0xF8, 22)
    AddParty(0x4B, 0xFF, 0xFF)
    SetChrFlags(0x14C, 0x8)
    OP_6D(107510, 0, -6820, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x8, 115040, 0, -7820, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x1000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_8CE():
        OP_8E(0xFE, 0x18286, 0x0, 0xFFFFE5DE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8CE)
    OP_0D()

    def lambda_8EA():
        OP_6D(99000, 0, -6480, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8EA)
    WaitChrThread(0x8, 0x1)
    OP_63(0x8)

    def lambda_90A():
        OP_96(0xFE, 0x18060, 0x0, 0xFFFFE5DE, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_90A)
    SetChrChipByIndex(0x8, 14)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x8, 0x1)
    OP_22(0x20C, 0x0, 0x50)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #3
        0x8,
        "#2PNo, no, no...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    SetChrSubChip(0x8, 1)
    OP_0D()

    ChrTalk(    #4
        0x8,
        (
            "#2PD-D-Damn it... Why is this...?\x02\x03",

            "Gotta, gotta hurry and tell someone...\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x193, 0x0, 0x64)
    Sleep(500)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x8, 2)
    Sleep(500)
    Fade(500)
    OP_6D(103940, 0, -7410, 0)
    OP_67(0, 5320, -10000, 0)
    OP_6B(2260, 0)
    OP_6C(98000, 0)
    OP_6E(434, 0)
    OP_43(0x9, 0x1, 0x0, 0xB)
    OP_43(0xA, 0x1, 0x0, 0xC)
    OP_43(0x9, 0x3, 0x0, 0x7)
    SetChrSubChip(0x8, 1)
    SetChrFlags(0x8, 0x20)
    OP_8C(0x8, 90, 500)
    ClearChrFlags(0x8, 0x20)
    SetChrSubChip(0x8, 1)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x9, 0x1)
    OP_62(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #5
        0x8,
        "Oh, no, no, no...\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    LoadEffect(0x0, "scraft\\\\sc000_11.eff")

    def lambda_AAC():
        OP_6D(101140, 500, -5910, 1200)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_AAC)

    def lambda_AC4():
        OP_67(0, 7530, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AC4)

    def lambda_ADC():
        OP_6B(1500, 1200)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_ADC)

    def lambda_AEC():
        OP_6C(45000, 1200)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_AEC)

    def lambda_AFC():
        OP_6E(434, 1200)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AFC)
    OP_43(0x9, 0x1, 0x0, 0xA)
    OP_43(0x9, 0x3, 0x0, 0x7)

    def lambda_B1A():
        OP_6D(101940, 0, -7410, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B1A)
    SetChrPos(0x101, 91500, -10, -5720, 90)
    SetChrPos(0x102, 91120, -30, -6800, 90)
    SetChrPos(0xF9, 90660, 30, -5210, 90)
    SetChrPos(0xF8, 90530, 300, -7050, 90)
    SetChrChipByIndex(0x102, 18)
    SetChrChipByIndex(0xF9, 22)
    SetChrChipByIndex(0xF8, 20)
    OP_43(0x102, 0x1, 0x0, 0xD)
    OP_43(0xF9, 0x1, 0x0, 0xE)
    OP_43(0xF8, 0x1, 0x0, 0xF)
    SetChrSubChip(0x101, 0)

    def lambda_B9F():
        OP_8F(0xFE, 0x17836, 0x0, 0xFFFFE890, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B9F)
    WaitChrThread(0x101, 0x3)
    SetChrChipByIndex(0x101, 17)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_BC9():
        OP_96(0xFE, 0x18A9C, 0x0, 0xFFFFE5AC, 0x9C4, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BC9)
    Sleep(200)

    ChrTalk(    #6 op#5
        0x101,
        "#1005F#1PHYYYAH!\x05\x02",
    )


    def lambda_C02():
        OP_99(0xFE, 0x0, 0x9, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C02)
    OP_22(0x1F4, 0x0, 0x64)
    Sleep(300)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x9, 0, 1000, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_43(0x9, 0x1, 0x0, 0x9)
    WaitChrThread(0x101, 0x2)
    OP_22(0xD5, 0x0, 0x64)

    def lambda_C78():
        OP_99(0xFE, 0x9, 0xC, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C78)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x8, 0x0)
    OP_43(0xA, 0x1, 0x0, 0x8)

    def lambda_C99():
        OP_6D(103750, 0, -6570, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C99)

    def lambda_CB1():
        OP_67(0, 8020, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CB1)

    def lambda_CC9():
        OP_6B(1810, 1500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CC9)

    def lambda_CD9():
        OP_6E(505, 1500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CD9)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0x101, 0x2)
    SetChrSubChip(0x101, 0)
    Sleep(500)

    ChrTalk(    #7
        0x8,
        "Whoa! You're...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1005F#5PAction first, words later!\x01",
            "We'll send these things packing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#1042F#5PStep back. We may not be\x01",
            "able to protect you in a fight.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DF0")

    ChrTalk(    #10
        0x107,
        (
            "#065FWh-Why are there armored\x01",
            "monsters HERE?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E84")

    label("loc_DF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E3B")

    ChrTalk(    #11
        0x103,
        (
            "#022FWhat are Ouroboros' armored\x01",
            "beasts doing HERE?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E84")

    label("loc_E3B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E84")

    ChrTalk(    #12
        0x106,
        (
            "#057FThe hell are Ouroboros' critters\x01",
            "doin' out here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB2")

    ChrTalk(    #13
        0x108,
        "#076FDefend yourselves!\x02",
    )

    CloseMessageWindow()
    Jump("loc_F02")

    label("loc_EB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ED7")

    ChrTalk(    #14
        0x106,
        "#054FBring it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_F02")

    label("loc_ED7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F02")

    ChrTalk(    #15
        0x103,
        "#024FDefend yourselves!\x02",
    )

    CloseMessageWindow()

    label("loc_F02")


    def lambda_F08():
        OP_6D(104360, 0, -6540, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F08)

    def lambda_F20():
        OP_6B(1650, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F20)
    SetChrChipByIndex(0x9, 24)
    OP_43(0x9, 0x3, 0x0, 0x7)

    def lambda_F3C():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_F3C)
    SetChrChipByIndex(0x101, 25)
    SetChrFlags(0x101, 0x1000)

    def lambda_F61():
        OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F61)

    def lambda_F7C():
        OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F7C)
    Sleep(50)
    SetChrChipByIndex(0xA, 24)

    def lambda_FA1():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_FA1)

    def lambda_FBC():
        OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_FBC)

    def lambda_FD7():
        OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_FD7)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x197, 0x0, 0x0, 0x0, 0xFF)
    OP_31(0xFF, 0xF9, 0x0)
    Return()

    # Function_5_50C end

    def Function_6_101C(): pass

    label("Function_6_101C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1029")
    Return()

    label("loc_1029")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    RemoveParty(0x4B, 0xFF)
    OP_44(0x9, 0x0)
    OP_44(0xA, 0x0)
    OP_44(0x101, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xF8, 0x0)
    OP_44(0xF9, 0x0)
    Sleep(500)
    OP_1D(0x15)
    OP_6D(104070, 0, -6980, 0)
    OP_67(0, 8710, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(45000, 0)
    OP_6E(317, 0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0x101, 103920, 0, -6740, 90)
    SetChrPos(0x102, 103800, 0, -8039, 90)
    SetChrPos(0xF9, 102580, 0, -6370, 90)
    SetChrPos(0xF8, 102590, 0, -8440, 90)
    SetChrPos(0x8, 98440, 0, -7170, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x101, 16)
    SetChrChipByIndex(0x102, 18)
    SetChrChipByIndex(0xF9, 22)
    SetChrChipByIndex(0xF8, 20)
    SetChrChipByIndex(0x8, 12)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    SetChrSubChip(0x8, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #16
        0x101,
        "#1007FPhew! That was rough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        (
            "#1035F#6PYes. Glad we managed to\x01",
            "make it in time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        "#1PYou saved me...\x02",
    )

    CloseMessageWindow()

    def lambda_11E2():
        OP_6D(103000, 0, -6950, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11E2)
    OP_8E(0x8, 0x18858, 0x0, 0xFFFFE37C, 0xBB8, 0x0)

    def lambda_120E():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_120E)
    Sleep(50)

    def lambda_1221():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1221)
    Sleep(60)

    def lambda_1234():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1234)
    Sleep(70)
    OP_8C(0x101, 270, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #19
        0x8,
        (
            "#6PEstelle and Joshua, right?\x02\x03",

            "Sorry... You really pulled my\x01",
            "bacon out of the fire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1006F#4PHey, no big.\x01",
            "It's part of the job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        (
            "#1042F#4PMore importantly...what's happened?\x02\x03",

            "Those monsters aren't from this area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        "#6PW-Well...\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(1000)

    ChrTalk(    #23
        0x8,
        (
            "#6PThe academy...\x01",
            "the royal academy's been attacked!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13BE")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_13FC")

    label("loc_13BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E5")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_13FC")

    label("loc_13E5")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_13FC")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1428")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1466")

    label("loc_1428")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144F")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1466")

    label("loc_144F")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1466")

    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x6E)
    Sleep(500)

    ChrTalk(    #24
        0x101,
        "#1005F#4PWHAT?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1507")

    ChrTalk(    #25
        0x103,
        "#022F#4PPlease, calm down and tell us everything.\x02",
    )

    CloseMessageWindow()
    Jump("loc_159F")

    label("loc_1507")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1550")

    ChrTalk(    #26
        0x106,
        (
            "#057F#4POkay, calm down and make\x01",
            "with the details.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_159F")

    label("loc_1550")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_159F")

    ChrTalk(    #27
        0x108,
        (
            "#072F#4PCalm yourself. Deep breaths.\x01",
            "Tell us what happened.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_159F")


    ChrTalk(    #28
        0x8,
        (
            "#6PO-Okay...\x02\x03",

            "I was... I was hanging around behind the\x01",
            "old schoolhouse, ditching class again.\x02\x03",

            "Suddenly, these soldier guys in red\x01",
            "armor break down the front gate!\x02\x03",

            "The janitor came up to ask them what\x01",
            "the hell they were doing, but...but...\x02\x03",

            "But they, they...sh-sh-shot the guy...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16FB")

    ChrTalk(    #29
        0x107,
        "#065F#4PAah...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1020F#4POh, no...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1795")

    label("loc_16FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_173C")

    ChrTalk(    #31
        0x101,
        "#1020F#4POh, no...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x108,
        "#072F#4PAnimals...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1795")

    label("loc_173C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1795")

    ChrTalk(    #33
        0x101,
        "#1020F#4POh, no...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x106,
        "#057F#4PNever thought they'd have the guts...\x02",
    )

    CloseMessageWindow()

    label("loc_1795")


    ChrTalk(    #35
        0x8,
        (
            "#6PWhen I saw that, my...my mind just\x01",
            "went blank...\x02\x03",

            "I ran and ran, like, I wanted to get some\x01",
            "help, but where was I gonna go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        (
            "#1035F#4PAll right, I think we understand the situation.\x02\x03",

            "#1040FListen closely. Can you follow the road\x01",
            "to Ruan and tell the guild secretary there,\x01",
            "Jean, what's happened?\x02\x03",

            "Tell him that Estelle Bright's team is\x01",
            "going to go investigate the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "#6PI'll... I'll try!\x02\x03",

            "They've got these weird, I dunno,\x01",
            "puppet things, too, along with the\x01",
            "monsters.\x02\x03",

            "Be careful, okay?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_101C end

    def Function_7_19B0(): pass

    label("Function_7_19B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19D0")
    OP_22(0x13F, 0x0, 0x50)
    Sleep(150)
    OP_22(0x13F, 0x0, 0x50)
    Sleep(300)
    Jump("Function_7_19B0")

    label("loc_19D0")

    Return()

    # Function_7_19B0 end

    def Function_8_19D1(): pass

    label("Function_8_19D1")

    SetChrChipByIndex(0xFE, 24)
    OP_96(0xFE, 0x1A838, 0x12C, 0xFFFFDE9A, 0x1F4, 0x1388)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_8_19D1 end

    def Function_9_19F8(): pass

    label("Function_9_19F8")

    OP_44(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 26)
    SetChrSubChip(0xFE, 0)

    def lambda_1A11():

        label("loc_1A11")

        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_1A11")

    QueueWorkItem2(0xFE, 3, lambda_1A11)
    OP_96(0xFE, 0x19C94, 0x0, 0xFFFFE69C, 0x64, 0x2710)
    OP_44(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x20)
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)

    def lambda_1A5C():

        label("loc_1A5C")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1A5C")

    QueueWorkItem2(0x9, 2, lambda_1A5C)
    OP_22(0x23B, 0x0, 0x64)
    OP_96(0xFE, 0x1A7D4, 0x12C, 0xFFFFE82C, 0x3E8, 0x1770)
    OP_22(0xA4, 0x0, 0x64)
    Return()

    # Function_9_19F8 end

    def Function_10_1A8B(): pass

    label("Function_10_1A8B")

    SetChrChipByIndex(0xFE, 24)

    def lambda_1A96():

        label("loc_1A96")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_1A96")

    QueueWorkItem2(0xFE, 2, lambda_1A96)
    OP_8F(0xFE, 0x1955A, 0x0, 0xFFFFE5DE, 0x1388, 0x0)
    OP_44(0x9, 0x3)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    OP_22(0x23B, 0x0, 0x64)
    OP_96(0xFE, 0x18A88, 0x0, 0xFFFFE5DE, 0x6A4, 0xFA0)
    Return()

    # Function_10_1A8B end

    def Function_11_1AE2(): pass

    label("Function_11_1AE2")

    SetChrPos(0xFE, 119000, 500, -6800, 270)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 24)

    def lambda_1B08():

        label("loc_1B08")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_1B08")

    QueueWorkItem2(0xFE, 2, lambda_1B08)
    OP_8F(0xFE, 0x1A23E, 0x1F4, 0xFFFFE570, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)

    def lambda_1B39():

        label("loc_1B39")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1B39")

    QueueWorkItem2(0xFE, 2, lambda_1B39)
    Return()

    # Function_11_1AE2 end

    def Function_12_1B47(): pass

    label("Function_12_1B47")

    Sleep(300)
    SetChrPos(0xFE, 119000, 500, -9000, 270)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 24)

    def lambda_1B72():

        label("loc_1B72")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_1B72")

    QueueWorkItem2(0xFE, 2, lambda_1B72)
    OP_8F(0xFE, 0x1A1C6, 0x1F4, 0xFFFFDCD8, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)

    def lambda_1BA3():

        label("loc_1BA3")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1BA3")

    QueueWorkItem2(0xFE, 2, lambda_1BA3)
    OP_44(0x9, 0x3)
    Return()

    # Function_12_1B47 end

    def Function_13_1BB5(): pass

    label("Function_13_1BB5")

    Sleep(1000)
    OP_8E(0xFE, 0x17CAA, 0x0, 0xFFFFE11A, 0x1770, 0x0)
    OP_8E(0xFE, 0x189AC, 0x0, 0xFFFFE0C0, 0x1770, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_13_1BB5 end

    def Function_14_1BEA(): pass

    label("Function_14_1BEA")

    Sleep(500)
    OP_8E(0xFE, 0x17E1C, 0x0, 0xFFFFEDAE, 0x1770, 0x0)
    OP_8E(0xFE, 0x186C8, 0x0, 0xFFFFE926, 0x1770, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_14_1BEA end

    def Function_15_1C1F(): pass

    label("Function_15_1C1F")

    Sleep(1300)
    OP_8E(0xFE, 0x1794E, 0xA, 0xFFFFE188, 0x1770, 0x0)
    OP_8E(0xFE, 0x182FE, 0x0, 0xFFFFE142, 0x1770, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_15_1C1F end

    def Function_16_1C54(): pass

    label("Function_16_1C54")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1CCD"),
        (1, "loc_1CD3"),
        (SWITCH_DEFAULT, "loc_1CD9"),
    )


    label("loc_1CCD")

    OP_A2(0x1200)
    Jump("loc_1CD9")

    label("loc_1CD3")

    OP_A2(0x1201)
    Jump("loc_1CD9")

    label("loc_1CD9")

    Return()

    # Function_16_1C54 end

    def Function_17_1CDA(): pass

    label("Function_17_1CDA")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_17_1CDA end

    SaveToFile()

Try(main)
