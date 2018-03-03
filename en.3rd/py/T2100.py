from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2100   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T2100   ._SN',
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
        'Target Camera',                        # 9
        'Eletta',                               # 10
        'Renzo',                                # 11
        'Kuper',                                # 12
        'Santos',                               # 13
        'Ruvie',                                # 14
        'Atget',                                # 15
        'Lytton',                               # 16
        'Phelio',                               # 17
        'Matilda',                              # 18
        'Herio',                                # 19
        'Lloyd',                                # 20
        'Thelma',                               # 21
        'Lechter',                              # 22
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
        'ED6_DT07/CH02070 ._CH',             # 01
        'ED6_DT07/CH01200 ._CH',             # 02
        'ED6_DT07/CH01040 ._CH',             # 03
        'ED6_DT07/CH01220 ._CH',             # 04
        'ED6_DT07/CH01680 ._CH',             # 05
        'ED6_DT07/CH01460 ._CH',             # 06
        'ED6_DT07/CH01500 ._CH',             # 07
        'ED6_DT07/CH01020 ._CH',             # 08
        'ED6_DT07/CH01030 ._CH',             # 09
        'ED6_DT07/CH01050 ._CH',             # 0A
        'ED6_DT07/CH01070 ._CH',             # 0B
        'ED6_DT07/CH01100 ._CH',             # 0C
        'ED6_DT07/CH01120 ._CH',             # 0D
        'ED6_DT07/CH01140 ._CH',             # 0E
        'ED6_DT07/CH01150 ._CH',             # 0F
        'ED6_DT07/CH01210 ._CH',             # 10
        'ED6_DT07/CH01130 ._CH',             # 11
        'ED6_DT07/CH01250 ._CH',             # 12
        'ED6_DT06/CH20092 ._CH',             # 13
        'ED6_DT07/CH01090 ._CH',             # 14
        'ED6_DT07/CH01153 ._CH',             # 15
        'ED6_DT07/CH01170 ._CH',             # 16
        'ED6_DT07/CH01000 ._CH',             # 17
        'ED6_DT07/CH01410 ._CH',             # 18
        'ED6_DT07/CH01663 ._CH',             # 19
        'ED6_DT07/CH01290 ._CH',             # 1A
        'ED6_DT07/CH02670 ._CH',             # 1B
    )

    AddCharChipPat(
        'ED6_DT07/CH02060P._CP',             # 00
        'ED6_DT07/CH02070P._CP',             # 01
        'ED6_DT07/CH01200P._CP',             # 02
        'ED6_DT07/CH01040P._CP',             # 03
        'ED6_DT07/CH01220P._CP',             # 04
        'ED6_DT07/CH01680P._CP',             # 05
        'ED6_DT07/CH01460P._CP',             # 06
        'ED6_DT07/CH01500P._CP',             # 07
        'ED6_DT07/CH01020P._CP',             # 08
        'ED6_DT07/CH01030P._CP',             # 09
        'ED6_DT07/CH01050P._CP',             # 0A
        'ED6_DT07/CH01070P._CP',             # 0B
        'ED6_DT07/CH01100P._CP',             # 0C
        'ED6_DT07/CH01120P._CP',             # 0D
        'ED6_DT07/CH01140P._CP',             # 0E
        'ED6_DT07/CH01150P._CP',             # 0F
        'ED6_DT07/CH01210P._CP',             # 10
        'ED6_DT07/CH01130P._CP',             # 11
        'ED6_DT07/CH01250P._CP',             # 12
        'ED6_DT06/CH20092P._CP',             # 13
        'ED6_DT07/CH01090P._CP',             # 14
        'ED6_DT07/CH01153P._CP',             # 15
        'ED6_DT07/CH01170P._CP',             # 16
        'ED6_DT07/CH01000P._CP',             # 17
        'ED6_DT07/CH01410P._CP',             # 18
        'ED6_DT07/CH01663P._CP',             # 19
        'ED6_DT07/CH01290P._CP',             # 1A
        'ED6_DT07/CH02670P._CP',             # 1B
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

    DeclNpc(
        X                   = 29170,
        Z                   = 0,
        Y                   = 89110,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 52980,
        Z                   = 0,
        Y                   = 95770,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 46730,
        Z                   = 0,
        Y                   = 78510,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 39560,
        Z                   = -1770,
        Y                   = 69520,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 26280,
        Z                   = 0,
        Y                   = 88370,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 24400,
        Z                   = 0,
        Y                   = 93520,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 28500,
        Z                   = 0,
        Y                   = 82470,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 46320,
        Z                   = 0,
        Y                   = 79740,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 23580,
        Z                   = 2160,
        Y                   = 102820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 54940,
        Z                   = 0,
        Y                   = 78510,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 22310,
        Z                   = 0,
        Y                   = 76950,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 21840,
        Z                   = 0,
        Y                   = 70280,
        Direction           = 60,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_34A",          # 00, 0
        "Function_1_3B3",          # 01, 1
        "Function_2_40A",          # 02, 2
        "Function_3_587",          # 03, 3
        "Function_4_6DA",          # 04, 4
        "Function_5_717",          # 05, 5
        "Function_6_FD2",          # 06, 6
        "Function_7_122F",         # 07, 7
    )


    def Function_0_34A(): pass

    label("Function_0_34A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_395")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_36C")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 7)
    Jump("loc_395")

    label("loc_36C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_382")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_395")

    label("loc_382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_395")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_395")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B2")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_3B2")

    Return()

    # Function_0_34A end

    def Function_1_3B3(): pass

    label("Function_1_3B3")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFF5420, 0x230047)
    OP_22(0x1C5, 0x1, 0x64)
    OP_82(0x86, 0x0)
    OP_71(0x1B, 0x0)
    ExitThread()
    OP_71(0x41B, 0x0)
    ExitThread()
    OP_71(0x1C, 0x0)
    ExitThread()
    OP_71(0x41C, 0x0)
    ExitThread()
    OP_71(0x1D, 0x0)
    ExitThread()
    OP_71(0x41D, 0x0)
    ExitThread()
    OP_71(0x1E, 0x0)
    ExitThread()
    OP_71(0x41E, 0x0)
    ExitThread()
    OP_71(0x1F, 0x0)
    ExitThread()
    OP_71(0x41F, 0x0)
    ExitThread()
    Return()

    # Function_1_3B3 end

    def Function_2_40A(): pass

    label("Function_2_40A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_571")

    label("loc_42F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_448")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_571")

    label("loc_448")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_461")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_571")

    label("loc_461")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47A")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_571")

    label("loc_47A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_493")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_571")

    label("loc_493")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AC")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_571")

    label("loc_4AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C5")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_571")

    label("loc_4C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DE")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_571")

    label("loc_4DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F7")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_571")

    label("loc_4F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_510")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_571")

    label("loc_510")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_529")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_571")

    label("loc_529")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_542")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_571")

    label("loc_542")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_571")

    label("loc_55B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_571")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_571")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_586")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_571")

    label("loc_586")

    Return()

    # Function_2_40A end

    def Function_3_587(): pass

    label("Function_3_587")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x14E, 0x8)
    OP_6D(31260, 0, 102800, 0)
    OP_67(0, 9400, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(45000, 0)
    OP_6E(508, 0)
    SetChrPos(0x1A, 22420, 0, 68800, 180)
    SetChrPos(0x15, 45540, 0, 83100, 270)
    SetChrPos(0x16, 24860, 1050, 102800, 270)
    OP_43(0x15, 0x3, 0x0, 0x4)

    def lambda_615():
        OP_6D(31260, 0, 81300, 8000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_615)

    def lambda_62D():
        OP_67(0, 6280, -10000, 16000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_62D)

    def lambda_645():
        OP_6B(2800, 16000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_645)

    def lambda_655():
        OP_6E(408, 16000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_655)

    def lambda_665():
        OP_6C(145000, 16000)
        ExitThread()

    QueueWorkItem(0x14E, 3, lambda_665)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x1, 0x7D0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10, 0x0)

    def lambda_699():
        OP_6D(61260, 0, 74000, 8000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_699)
    WaitChrThread(0x10, 0x0)

    def lambda_6B6():
        OP_6B(2700, 3000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_6B6)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x14E, 0x8)
    NewScene("ED6_DT21/T2120   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_587 end

    def Function_4_6DA(): pass

    label("Function_4_6DA")

    OP_8E(0x15, 0x8048, 0x0, 0x1449C, 0x7D0, 0x0)
    OP_8E(0x15, 0x6590, 0x0, 0x16AE4, 0x7D0, 0x0)
    OP_8E(0x15, 0x6590, 0x0, 0x19708, 0x7D0, 0x0)
    Return()

    # Function_4_6DA end

    def Function_5_717(): pass

    label("Function_5_717")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6F(0x11, 1500)
    OP_72(0x21A, 0x0)
    ExitThread()
    OP_6D(26520, 0, 106980, 0)
    OP_67(0, 9900, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(390, 0)
    SetChrPos(0x15, 26690, 0, 86030, 225)
    SetChrPos(0x16, 25540, 0, 87170, 225)
    SetChrPos(0x1A, 22420, 0, 68800, 180)
    SetChrPos(0x105, 26000, 0, 122800, 180)

    def lambda_7B7():
        OP_8E(0xFE, 0x6590, 0x0, 0x17AFC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7B7)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x1, 0x7D0)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_7F1():
        OP_6D(25500, 0, 97520, 10000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_7F1)

    def lambda_809():
        OP_67(0, 6580, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_809)

    def lambda_821():
        OP_6C(315000, 10000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_821)

    def lambda_831():
        OP_6E(275, 10000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_831)
    WaitChrThread(0x105, 0x1)
    Sleep(300)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x105)
    Sleep(500)
    OP_8C(0x105, 270, 500)
    Sleep(800)
    OP_8C(0x105, 90, 500)
    Sleep(800)
    OP_8C(0x105, 180, 500)
    Sleep(800)

    ChrTalk(    #0
        0x105,
        (
            "#040F#5PWell, here I am.\x02\x03",

            "This is the first time I've had the chance\x01",
            "to walk through here like this...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8FA():
        OP_6D(25500, 0, 93520, 3000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_8FA)

    def lambda_912():
        OP_8E(0xFE, 0x6590, 0x0, 0x162C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_912)
    Sleep(500)

    ChrTalk(    #1 op#A
        0x105,
        (
            "#047F#20A#5P(Not like I could before...)\x02\x03",

            "#35A(The last time I came was during the\x01",
            "Hundred Days War.)\x02",
        )
    )

    WaitChrThread(0x105, 0x1)

    def lambda_9A1():
        OP_8E(0xFE, 0x7D00, 0x0, 0x14B54, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9A1)
    WaitChrThread(0x105, 0x1)
    Fade(1000)
    OP_6D(49460, 0, 73360, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(3260, 0)
    OP_6C(225000, 0)
    OP_6E(310, 0)
    SetChrPos(0x105, 47000, 0, 83360, 180)
    Sleep(1000)

    def lambda_A19():
        OP_8E(0xFE, 0xC6E8, 0x0, 0x1368C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A19)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 180, 400)
    Sleep(300)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #2
        0x105,
        "#044FWhoops...\x02",
    )

    CloseMessageWindow()

    def lambda_A75():
        OP_6D(48700, 0, 66700, 5000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_A75)

    def lambda_A8D():
        OP_67(0, 9100, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A8D)

    def lambda_AA5():
        OP_6C(315000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_AA5)

    def lambda_AB5():
        OP_6E(460, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_AB5)

    def lambda_AC5():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_AC5)
    WaitChrThread(0x10, 0x0)
    Sleep(800)

    ChrTalk(    #3
        0x105,
        (
            "#044F#12P(I forgot that you can't cross the bridge at\x01",
            "this time of day.)\x02\x03",

            "#047F(Guess I'll try heading to the mayor's mansion\x01",
            "later.)\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(50600, 0, 79820, 0)
    OP_67(0, 8300, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    Sleep(1300)
    OP_8C(0x105, 0, 400)
    Sleep(300)

    ChrTalk(    #4
        0x105,
        (
            "#045FIt's no big deal, anyway.\x02\x03",

            "Lechter didn't make it seem too urgent.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 90, 500)
    Sleep(500)
    OP_8C(0x105, 315, 500)
    Sleep(1000)

    ChrTalk(    #5
        0x105,
        (
            "#543FIt's so nice to see this town so lively...\x02\x03",

            "It really has changed in atmosphere since\x01",
            "then...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(500)
    OP_8C(0x105, 270, 500)
    Sleep(1000)

    def lambda_CB8():
        OP_6D(42780, 0, 78200, 4000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_CB8)

    def lambda_CD0():
        OP_67(0, 6260, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_CD0)

    def lambda_CE8():
        OP_6C(220000, 4000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_CE8)

    def lambda_CF8():
        OP_6E(404, 4000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_CF8)
    Sleep(2000)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x40)
    SetChrPos(0x1D, 30260, 0, 86160, 130)

    def lambda_D28():
        OP_8E(0xFE, 0x9470, 0x0, 0x1381C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_D28)
    WaitChrThread(0x1D, 0x1)

    def lambda_D48():
        OP_8E(0xFE, 0x9470, 0x0, 0x132AE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_D48)
    WaitChrThread(0x1D, 0x1)
    OP_8C(0x1D, 180, 500)
    Sleep(300)
    Fade(1000)
    OP_6D(38740, 0, 77550, 0)
    OP_6B(2180, 0)
    OP_0D()
    OP_72(0x100C, 0x0)
    ExitThread()
    OP_70(0xC, 0x1E)
    OP_73(0xC)
    Sleep(200)

    def lambda_DA9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_DA9)

    def lambda_DBB():
        OP_8E(0xFE, 0x9470, 0x0, 0x12AD4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_DBB)
    WaitChrThread(0x1D, 0x1)
    OP_72(0xC, 0x8)
    ExitThread()
    OP_6F(0xC, 30)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0xC, 0x0)
    Sleep(1500)

    ChrTalk(    #6
        0x105,
        "#044F#2PIsn't that...a casino?!\x02",
    )

    CloseMessageWindow()

    def lambda_E1E():
        OP_6D(44870, 0, 77610, 1500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_E1E)
    WaitChrThread(0x10, 0x0)
    Sleep(500)
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #7
        0x105,
        (
            "#047FPlease tell me he isn't in there for the reason\x01",
            "I think he is...\x02\x03",

            "#042FHe better not be!\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x81, 0x0)

    def lambda_EC2():
        OP_6D(38000, 500, 73700, 2800)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_EC2)

    def lambda_EDA():
        OP_67(0, 4920, -10000, 2800)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_EDA)

    def lambda_EF2():
        OP_6C(180000, 2800)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_EF2)

    def lambda_F02():
        OP_8E(0xFE, 0x9858, 0x0, 0x1368C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F02)
    WaitChrThread(0x105, 0x1)

    def lambda_F22():
        OP_8E(0xFE, 0x9470, 0x0, 0x132A4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F22)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 180, 500)
    OP_71(0xC, 0x8)
    ExitThread()
    OP_6F(0xC, 0)
    OP_70(0xC, 0x1E)
    OP_73(0xC)
    Sleep(200)

    def lambda_F65():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_F65)

    def lambda_F77():
        OP_8E(0xFE, 0x9470, 0x0, 0x12AD4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F77)
    WaitChrThread(0x105, 0x1)
    OP_72(0xC, 0x8)
    ExitThread()
    OP_6F(0xC, 30)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0xC, 0x0)

    def lambda_FB0():
        OP_6B(2700, 2000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_FB0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2131   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_717 end

    def Function_6_FD2(): pass

    label("Function_6_FD2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(51000, 500, 52320, 0)
    OP_67(0, 8200, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(180000, 0)
    OP_6E(398, 0)
    SetChrPos(0x1A, 22420, 0, 68800, 180)
    SetChrPos(0x105, 51000, 0, 38000, 0)

    def lambda_1043():
        OP_8E(0xFE, 0xC738, 0x0, 0x13F88, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1043)
    FadeToBright(2000, 0)

    def lambda_1067():
        OP_6D(51000, 0, 65459, 8000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1067)

    def lambda_107F():
        OP_67(0, 4000, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_107F)

    def lambda_1097():
        OP_6B(3420, 8000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1097)
    WaitChrThread(0x105, 0x1)
    Fade(1000)
    OP_6D(38000, 500, 75400, 0)
    OP_67(0, 4920, -10000, 0)
    OP_6C(180000, 0)
    OP_6B(2800, 0)
    OP_6E(404, 0)
    SetChrPos(0x105, 50000, 0, 79500, 0)

    def lambda_10FF():
        OP_8E(0xFE, 0x9470, 0x0, 0x1368C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10FF)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 180, 500)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #8
        0x105,
        (
            "#042FI wonder if he's actually still here like I told\x01",
            "him to be...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_118D():
        OP_8E(0xFE, 0x9470, 0x0, 0x132A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_118D)
    WaitChrThread(0x105, 0x1)
    OP_72(0x100C, 0x0)
    ExitThread()
    OP_70(0xC, 0x1E)
    OP_73(0xC)
    Sleep(300)

    def lambda_11C2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_11C2)

    def lambda_11D4():
        OP_8E(0xFE, 0x9470, 0x0, 0x12AD4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11D4)
    WaitChrThread(0x105, 0x1)
    OP_72(0xC, 0x8)
    ExitThread()
    OP_6F(0xC, 30)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0xC, 0x0)

    def lambda_120D():
        OP_6B(2700, 2000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_120D)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T2131   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_FD2 end

    def Function_7_122F(): pass

    label("Function_7_122F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(37260, 0, 78560, 0)
    OP_67(0, 7020, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x1A, 22420, 0, 68800, 180)
    SetChrPos(0x105, 38000, 0, 76500, 0)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_12AB():
        OP_6B(3100, 3000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_12AB)
    FadeToBright(1000, 0)
    OP_0D()
    OP_72(0x100C, 0x0)
    ExitThread()
    OP_70(0xC, 0x1E)
    OP_73(0xC)

    def lambda_12D5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_12D5)

    def lambda_12E7():
        OP_8E(0xFE, 0x9470, 0x0, 0x132A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12E7)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 180, 400)
    Sleep(300)
    OP_72(0xC, 0x8)
    ExitThread()
    OP_6F(0xC, 30)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0xC, 0x0)
    OP_73(0xC)
    Sleep(300)
    OP_8C(0x105, 0, 400)

    def lambda_133B():
        OP_8E(0xFE, 0x9470, 0x0, 0x135C4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_133B)
    WaitChrThread(0x105, 0x1)
    Sleep(500)

    ChrTalk(    #9
        0x105,
        (
            "#047F...I'm exhausted.\x02\x03",

            "I can't believe he's even an active gambler...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 315, 300)

    def lambda_13B3():
        OP_8E(0xFE, 0x6B30, 0x0, 0x14F28, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_13B3)
    Sleep(1000)

    ChrTalk(    #10 op#A
        0x105,
        (
            "#049F#30A#3PHe's so far gone, I'm not sure how to begin\x01",
            "trying to get him to turn over a new leaf...\x02",
        )
    )

    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    OP_44(0x105, 0xFF)
    NewScene("ED6_DT21/R2202   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_122F end

    SaveToFile()

Try(main)
