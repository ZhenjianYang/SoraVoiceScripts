from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0300   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0300.x',
        MapIndex            = 15,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 24,
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
        'Cassius',                              # 9
        'Lena',                                 # 10
        'Scherazard',                           # 11
        'Kevin',                                # 12
        'Elize Highway',                        # 13
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
        'ED6_DT06/CH20161 ._CH',             # 00
        'ED6_DT07/CH02000 ._CH',             # 01
        'ED6_DT27/CH03740 ._CH',             # 02
        'ED6_DT26/CH20316 ._CH',             # 03
        'ED6_DT26/CH20339 ._CH',             # 04
        'ED6_DT26/CH20325 ._CH',             # 05
        'ED6_DT26/CH20317 ._CH',             # 06
        'ED6_DT26/CH20334 ._CH',             # 07
        'ED6_DT26/CH20319 ._CH',             # 08
        'ED6_DT26/CH20322 ._CH',             # 09
        'ED6_DT27/CH03780 ._CH',             # 0A
        'ED6_DT07/CH02000 ._CH',             # 0B
        'ED6_DT26/CH20239 ._CH',             # 0C
        'ED6_DT27/CH03080 ._CH',             # 0D
        'ED6_DT26/CH20240 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT06/CH20161P._CP',             # 00
        'ED6_DT07/CH02000P._CP',             # 01
        'ED6_DT27/CH03740P._CP',             # 02
        'ED6_DT26/CH20316P._CP',             # 03
        'ED6_DT26/CH20339P._CP',             # 04
        'ED6_DT26/CH20325P._CP',             # 05
        'ED6_DT26/CH20317P._CP',             # 06
        'ED6_DT26/CH20334P._CP',             # 07
        'ED6_DT26/CH20319P._CP',             # 08
        'ED6_DT26/CH20322P._CP',             # 09
        'ED6_DT27/CH03780P._CP',             # 0A
        'ED6_DT07/CH02000P._CP',             # 0B
        'ED6_DT26/CH20239P._CP',             # 0C
        'ED6_DT27/CH03080P._CP',             # 0D
        'ED6_DT26/CH20240P._CP',             # 0E
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 4110,
        Z                   = -1000,
        Y                   = -46140,
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


    DeclEvent(
        X                   = -270,
        Y                   = 0,
        Z                   = -16990,
        Range               = 4310,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFC0CC,
        Unknown_18          = 0x0,
        Unknown_1C          = 14,
    )


    DeclActor(
        TriggerX            = -11800,
        TriggerZ            = 0,
        TriggerY            = 6720,
        TriggerRange        = 1000,
        ActorX              = -14930,
        ActorZ              = -2000,
        ActorY              = 9650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_206",          # 00, 0
        "Function_1_2FE",          # 01, 1
        "Function_2_3B3",          # 02, 2
        "Function_3_530",          # 03, 3
        "Function_4_535",          # 04, 4
        "Function_5_9C7",          # 05, 5
        "Function_6_12EA",         # 06, 6
        "Function_7_13D7",         # 07, 7
        "Function_8_170B",         # 08, 8
        "Function_9_1725",         # 09, 9
        "Function_10_175A",        # 0A, 10
        "Function_11_178F",        # 0B, 11
        "Function_12_17F3",        # 0C, 12
        "Function_13_19B8",        # 0D, 13
        "Function_14_19FD",        # 0E, 14
        "Function_15_2C5E",        # 0F, 15
        "Function_16_2C8E",        # 10, 16
        "Function_17_307F",        # 11, 17
        "Function_18_31E8",        # 12, 18
        "Function_19_326D",        # 13, 19
        "Function_20_34DD",        # 14, 20
        "Function_21_355B",        # 15, 21
        "Function_22_35C7",        # 16, 22
        "Function_23_494D",        # 17, 23
        "Function_24_4CFA",        # 18, 24
        "Function_25_4E88",        # 19, 25
        "Function_26_5EE1",        # 1A, 26
        "Function_27_5F21",        # 1B, 27
        "Function_28_60D3",        # 1C, 28
        "Function_29_616E",        # 1D, 29
        "Function_30_61C0",        # 1E, 30
    )


    def Function_0_206(): pass

    label("Function_0_206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_240")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F")
    SetChrFlags(0x9, 0x10)

    label("loc_21F")

    SetChrPos(0x9, -7530, 0, 2690, 90)
    ClearChrFlags(0x9, 0x80)
    OP_E5(0x9, 0x0, 0x0)
    OP_43(0x9, 0x0, 0x0, 0x2)

    label("loc_240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_251")
    OP_A3(0x10F0)
    Event(0, 6)
    Jump("loc_2FD")

    label("loc_251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_262")
    OP_A3(0x10F1)
    Event(0, 7)
    Jump("loc_2FD")

    label("loc_262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_281")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F2)
    Event(0, 12)
    Jump("loc_2FD")

    label("loc_281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_2A0")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    OP_A3(0x10F3)
    Event(0, 16)
    Jump("loc_2FD")

    label("loc_2A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_2BF")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    OP_A3(0x10F4)
    Event(0, 22)
    Jump("loc_2FD")

    label("loc_2BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DC")
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_2DC")

    Jump("loc_2FD")

    label("loc_2DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FD")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_2FD")

    Return()

    # Function_0_206 end

    def Function_1_2FE(): pass

    label("Function_1_2FE")

    OP_16(0x2, 0xFA0, 0xFFFE17B8, 0xFFFDF878, 0x230003)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_378")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_358")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 7)), scpexpr(EXPR_END)), "loc_343")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    Jump("loc_358")

    label("loc_343")

    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)

    label("loc_358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 3)), scpexpr(EXPR_END)), "loc_378")
    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 4)), scpexpr(EXPR_END)), "loc_378")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_386")
    OP_43(0x101, 0x3, 0x0, 0xD)

    label("loc_386")

    OP_71(0x3, 0x4)
    OP_71(0x6, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 5)), scpexpr(EXPR_END)), "loc_39E")
    OP_6F(0x7, 30)

    label("loc_39E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B2")
    OP_1B(0x0, 0x0, 0x1E)
    OP_82(0x80, 0x2)

    label("loc_3B2")

    Return()

    # Function_1_2FE end

    def Function_2_3B3(): pass

    label("Function_2_3B3")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D8")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_51A")

    label("loc_3D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F1")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_51A")

    label("loc_3F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40A")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_51A")

    label("loc_40A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_423")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_51A")

    label("loc_423")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43C")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_51A")

    label("loc_43C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_455")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_51A")

    label("loc_455")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_51A")

    label("loc_46E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_487")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_51A")

    label("loc_487")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A0")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_51A")

    label("loc_4A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B9")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_51A")

    label("loc_4B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D2")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_51A")

    label("loc_4D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EB")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_51A")

    label("loc_4EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_504")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_51A")

    label("loc_504")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51A")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_51A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_51A")

    label("loc_52F")

    Return()

    # Function_2_3B3 end

    def Function_3_530(): pass

    label("Function_3_530")

    Call(0, 23)
    Return()

    # Function_3_530 end

    def Function_4_535(): pass

    label("Function_4_535")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrPos(0x101, 1890, -1000, -18670, 0)
    SetChrPos(0x142, 3040, -1000, -20140, 0)
    OP_6D(1760, 6700, 2360, 0)
    OP_67(0, 9860, -10000, 0)
    OP_6B(3530, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    OP_C8(0x200, 0x46, "C_PLAC01._CH", 0x0, 0x7D0)
    OP_DE("Bright Family House")
    FadeToBright(2000, 0)

    def lambda_5D4():
        OP_6D(990, 6700, -11410, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5D4)

    def lambda_5EC():
        OP_67(0, 9860, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5EC)

    def lambda_604():
        OP_8E(0x101, 0x7BC, 0x0, 0xFFFFDE18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x142, 0, lambda_604)

    def lambda_61F():
        OP_8E(0x142, 0x97E, 0x0, 0xFFFFD922, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x142, 1, lambda_61F)
    Sleep(5000)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    Fade(1000)
    OP_6D(2550, 0, -8780, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x142, 0x0)
    WaitChrThread(0x142, 0x1)
    Sleep(1000)

    ChrTalk(    #0
        0x142,
        (
            "#1062F#4PHuh, so this is your place, Estelle?\x02\x03",

            "It's got a...how to put this...a warm,\x01",
            "homey feel to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#008F#3PHeh heh. Yeah, I know.\x02\x03",

            "This place holds a lot of memories.\x01",
            "For me, for Dad...\x02\x03",

            "And for Joshua, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x142,
        (
            "#1060F#4PSo I can see!\x02\x03",

            "And you think Joshua's going\x01",
            "to be just inside, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#3P#006FYeah, I'm sure he is.\x02\x03",

            "Come on in! I'll introduce you\x01",
            "to him. He'll like you, I think.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_82F():
        OP_8E(0x101, 0x7D9, 0x1C2, 0xFFFFF0A6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x142, 0, lambda_82F)

    def lambda_84A():
        OP_6D(1750, 450, -4240, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_84A)

    def lambda_862():
        OP_67(0, 9500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_862)
    OP_62(0x142, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x142, 0x0)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)

    def lambda_8A7():
        OP_8E(0x101, 0x8DE, 0x1C2, 0xFFFFFA1A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x142, 0, lambda_8A7)
    Sleep(1200)

    def lambda_8C7():
        OP_6D(1980, 0, -8680, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8C7)

    def lambda_8DF():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8DF)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_63(0x142)
    Sleep(500)

    ChrTalk(    #4
        0x142,
        (
            "#1067F#4PMan, who IS this guy?\x01",
            "The number he's done on her...\x02\x03",

            "#1065FWell...let's get this over with.\x01",
            "Aidios, give her strength...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_991():
        OP_8E(0x142, 0x802, 0x1C2, 0xFFFFF150, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x142, 1, lambda_991)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x142, 0x1)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_535 end

    def Function_5_9C7(): pass

    label("Function_5_9C7")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E7")
    Call(0, 28)
    FadeToBright(0, 0)
    Call(0, 29)

    label("loc_9E7")

    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x101, 1800, -1000, -27820, 0)
    SetChrPos(0x103, 2900, -1000, -27820, 0)
    SetChrPos(0xF8, 1700, -1000, -28820, 0)
    SetChrPos(0xF9, 2800, -1000, -28820, 0)
    OP_6D(5010, 0, 6710, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(48000, 0)
    OP_6E(358, 0)

    def lambda_A82():
        OP_6D(2660, 0, -15230, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A82)

    def lambda_A9A():
        OP_67(0, 9500, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A9A)

    def lambda_AB2():
        OP_6B(1990, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_AB2)

    def lambda_AC2():
        OP_6C(45000, 7000)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AC2)
    OP_C8(0x200, 0x46, "C_PLAC01._CH", 0x0, 0x7D0)
    OP_DE("Bright Family House")
    FadeToBright(2000, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)

    def lambda_B19():
        OP_90(0xFE, 0x0, 0x0, 0x3138, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B19)
    Sleep(200)

    def lambda_B39():
        OP_90(0xFE, 0x0, 0x0, 0x3138, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B39)
    Sleep(200)

    def lambda_B59():
        OP_90(0xFE, 0x0, 0x0, 0x30D4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_B59)
    Sleep(200)

    def lambda_B79():
        OP_90(0xFE, 0x0, 0x0, 0x30D4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_B79)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)

    ChrTalk(    #5
        0x101,
        (
            "#1015F#6PHmmm. Doesn't look like much fog's\x01",
            "gotten here yet.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C64")

    ChrTalk(    #6
        0x107,
        "#560FWooow! Is this your house, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x106,
        (
            "#051FHah, never realized how nice a place\x01",
            "the old man had.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_C64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF1")

    ChrTalk(    #8
        0x104,
        "#033FAh, so this is the Bright home, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x106,
        (
            "#051FHah, never realized how nice a place\x01",
            "the old man had.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_CF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D77")

    ChrTalk(    #10
        0x105,
        (
            "#048FOh, is this your home,\x01",
            "Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x106,
        (
            "#051FHah, never realized how nice a place\x01",
            "the old man had.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_D77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DFD")

    ChrTalk(    #12
        0x106,
        (
            "#051FHah. So this is the old man's place,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x108,
        "#071FHaha. I like it! Simple, but a bit refined.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_DFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E97")

    ChrTalk(    #14
        0x107,
        "#560FWooow! Is this your house, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x104,
        (
            "#031FAh, a place of refined tastes.\x01",
            "Cassius Bright, you do not disappoint.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_E97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F03")

    ChrTalk(    #16
        0x107,
        "#560FWooow! Is this your house, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x105,
        "#041FIt's absolutely lovely.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_F03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F83")

    ChrTalk(    #18
        0x107,
        "#560FWooow! Is this your house, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x108,
        (
            "#071FHaha. I like it!\x01",
            "Simple, but a bit refined.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_F83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1019")

    ChrTalk(    #20
        0x105,
        "#048FOh, is this your home, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x104,
        (
            "#031FAh, a place of refined tastes.\x01",
            "Cassius Bright, you do not disappoint.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_1019")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_109C")

    ChrTalk(    #22
        0x104,
        "#033FAh, so this is the Bright home, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x108,
        (
            "#071FHaha. I like it!\x01",
            "Simple, but a bit refined.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_109C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1115")

    ChrTalk(    #24
        0x105,
        "#048FOh, is this your home, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x108,
        (
            "#071FHaha. I like it!\x01",
            "Simple, but a bit refined.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1115")

    OP_8C(0x101, 180, 400)

    ChrTalk(    #26
        0x101,
        (
            "#1016F#6PUh, you really think so? Thanks!\x02\x03",

            "#1011FWell, anyway, I can fix everyone some\x01",
            "tea or something, at least. Come on inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x103,
        (
            "#026F#4PI'll handle making the tea.\x02\x03",

            "#027FYou head on up to the rooms upstairs.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #28
        0x101,
        "#1004F#6PThe...um, why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x103,
        "#524F#4PLook up, Estelle.\x02",
    )

    CloseMessageWindow()

    def lambda_1242():
        OP_6D(2070, 0, 8140, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1242)

    def lambda_125A():
        OP_6C(9000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_125A)

    def lambda_126A():
        OP_6B(2530, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_126A)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #30
        0x101,
        (
            "#1004F#1POh, right.\x02\x03",

            "#1007FThe house is gonna get pretty\x01",
            "damp in this fog...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T0310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_9C7 end

    def Function_6_12EA(): pass

    label("Function_6_12EA")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(490, 6660, 350, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 420, 6700, 2930, 180)
    ClearChrFlags(0x101, 0x80)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_8E(0x101, 0x1A4, 0x1A2C, 0xFFFFFFC4, 0x7D0, 0x0)
    OP_8C(0x101, 225, 400)
    Sleep(500)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x1E)
    OP_23(0x6)

    def lambda_1398():
        OP_8F(0xFE, 0x262, 0x1A2C, 0x208, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1398)
    Sleep(500)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x7)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T0310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_12EA end

    def Function_7_13D7(): pass

    label("Function_7_13D7")

    EventBegin(0x0)
    OP_22(0x1C2, 0x0, 0x64)
    OP_BB(0x0, 0x1, 0x0)
    AddParty(0x2, 0xF7, 0xFF)
    AddParty(0x6, 0xF8, 0xFF)
    AddParty(0x4, 0xF9, 0xFF)
    OP_6D(2280, 450, -2180, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(38000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrPos(0x101, 2110, 450, -1890, 180)
    SetChrPos(0x103, 2110, 450, -1890, 180)
    SetChrPos(0x107, 2110, 450, -1890, 180)
    SetChrPos(0x105, 2110, 450, -1890, 180)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)
    Sleep(1000)
    OP_43(0x101, 0x1, 0x0, 0x8)
    Sleep(500)
    OP_43(0x103, 0x1, 0x0, 0x9)
    Sleep(500)
    OP_43(0x107, 0x1, 0x0, 0xA)
    Sleep(500)
    OP_43(0x105, 0x1, 0x0, 0xB)

    def lambda_1521():
        OP_6D(2060, 450, -5010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1521)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x101, 0x2)
    OP_23(0x1C2)

    ChrTalk(    #31
        0x101,
        (
            "#1004F#7PWhoa! Is it me or is it thicker than\x01",
            "yesterday?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x105,
        "#043F#6PYes, it's definitely getting worse.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x107,
        "#065F#6PI hope Agate and the others are okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1015F#7PAt this point? Good question.\x02\x03",

            "Even if it was just a patrol,\x01",
            "I'm kind of worried...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x107, 400)

    ChrTalk(    #35
        0x103,
        (
            "#020F#6PLet's get to the guildhouse.\x02\x03",

            "We should be able to hear about\x01",
            "last night, along with anything else.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_16C4():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16C4)
    Sleep(50)

    def lambda_16D7():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_16D7)
    Sleep(400)

    ChrTalk(    #36
        0x101,
        "#1006FGood idea!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x181C)
    OP_28(0x90, 0x1, 0x800)
    OP_28(0x74, 0x4, 0x40)
    EventEnd(0x0)
    Return()

    # Function_7_13D7 end

    def Function_8_170B(): pass

    label("Function_8_170B")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x7E4, 0x1C2, 0xFFFFE89A, 0x7D0, 0x0)
    Return()

    # Function_8_170B end

    def Function_9_1725(): pass

    label("Function_9_1725")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x820, 0x1C2, 0xFFFFF132, 0x7D0, 0x0)
    OP_8E(0xFE, 0x49C, 0x1C2, 0xFFFFEC78, 0x7D0, 0x0)
    OP_8C(0xFE, 226, 400)
    Return()

    # Function_9_1725 end

    def Function_10_175A(): pass

    label("Function_10_175A")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x820, 0x1C2, 0xFFFFF132, 0x7D0, 0x0)
    OP_8E(0xFE, 0xB2C, 0x1C2, 0xFFFFEC78, 0x7D0, 0x0)
    OP_8C(0xFE, 136, 400)
    Return()

    # Function_10_175A end

    def Function_11_178F(): pass

    label("Function_11_178F")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x802, 0x1C2, 0xFFFFF25E, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(200)
    OP_72(0x0, 0x800)
    OP_6F(0x0, 59)
    OP_70(0x0, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x7ED, 0x1C2, 0xFFFFF060, 0x7D0, 0x0)
    Return()

    # Function_11_178F end

    def Function_12_17F3(): pass

    label("Function_12_17F3")

    EventBegin(0x0)
    OP_D6(0x0)
    OP_6D(3370, -1000, -30420, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2990, -1000, -35620, 0)

    def lambda_184B():
        OP_8E(0xFE, 0xCBC, 0xFFFFFC18, 0xFFFF83BE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_184B)
    FadeToBright(4000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #37
        0x101,
        "#1004F#2PHuh?\x02",
    )

    CloseMessageWindow()

    def lambda_188D():
        OP_6D(3360, -1000, -18490, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_188D)

    def lambda_18A5():
        OP_67(0, 8000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18A5)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    Sleep(100)
    Fade(1000)
    OP_6D(3370, -1000, -30420, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #38
        0x101,
        "#1004F#2PThis is...my house?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 500)
    Sleep(500)
    OP_8C(0x101, 270, 500)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    Sleep(1000)

    ChrTalk(    #39
        0x101,
        (
            "#1015F#2PBut I was in Mistwald!\x02\x03",

            "And...when did the fog clear?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1833)
    EventEnd(0x0)
    OP_1D(0xF)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x1)
    OP_43(0x101, 0x3, 0x0, 0xD)
    OP_1B(0x0, 0x0, 0x1E)
    Return()

    # Function_12_17F3 end

    def Function_13_19B8(): pass

    label("Function_13_19B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_19FC")
    Sleep(2000)
    OP_22(0x11A, 0x0, 0x46)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_19FC")

    label("loc_19D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19FC")
    Sleep(4000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E9")
    Jump("loc_19FC")

    label("loc_19E9")

    OP_22(0x11A, 0x0, 0x46)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F9")
    Jump("loc_19FC")

    label("loc_19F9")

    Jump("loc_19D0")

    label("loc_19FC")

    Return()

    # Function_13_19B8 end

    def Function_14_19FD(): pass

    label("Function_14_19FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A0A")
    Return()

    label("loc_1A0A")

    EventBegin(0x0)
    OP_A3(0x1)
    Fade(1000)
    SetChrPos(0x101, 1960, 0, -16680, 0)
    OP_6D(1440, 0, -16329, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_71(0x4, 0x4)
    OP_72(0x3, 0x4)
    OP_72(0x3, 0x20)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 2)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, -8500, 0, -7490, 90)

    def lambda_1ACC():
        OP_6D(-8590, 0, -7270, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1ACC)

    def lambda_1AE4():
        OP_67(0, 5180, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AE4)

    def lambda_1AFC():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1AFC)
    OP_8C(0x101, 315, 400)
    WaitChrThread(0x101, 0x0)
    OP_99(0x8, 0x2, 0x0, 0x5DC)

    def lambda_1B21():
        OP_99(0x8, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1B21)
    Sleep(200)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3C)
    OP_22(0x11A, 0x0, 0x64)
    Sleep(300)
    WaitChrThread(0x8, 0x0)
    OP_99(0x8, 0x4, 0x8, 0x3E8)
    Sleep(500)

    ChrTalk(    #40
        0x8,
        "#085F#6PPhew!! That should be enough.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, -1170, 0, -14210, 323)

    ChrTalk(    #41
        0x101,
        "#5PD-Dad...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x8, 9)

    def lambda_1BCB():
        OP_8E(0xFE, 0xFFFFEC5A, 0x0, 0xFFFFD4F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1BCB)

    def lambda_1BE6():
        OP_6D(-8160, 0, -7840, 2200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BE6)

    def lambda_1BFE():
        OP_6B(3050, 2200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1BFE)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0x3)

    ChrTalk(    #42
        0x8,
        (
            "#080FAh, Estelle.\x02\x03",

            "What's wrong? You're up early.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1004FUh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "#081FHaha, I see now!\x02\x03",

            "You want to spend some time with your\x01",
            "papa who's been gone for so long, huh?\x02\x03",

            "All right then! Leap into Papa's arms,\x01",
            "Estelle! He's ready!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1019FOh, don't treat me like I'm four years old,\x01",
            "Dad.\x02\x03",

            "#1007FAren't you busy with your army work?\x01",
            "How'd you sneak away for time off?\x02\x03",

            "#1009FI mean, c'mon, at least TELL me ahead of\x01",
            "time. We could've matched sched--\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x0, 0x10)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)
    Sleep(500)
    SetChrPos(0x9, 2020, 450, -3650, 225)
    SetChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(    #46
        0x9,
        "Woman's Voice",
        "#1POh, dear. This energetic so early?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_20(0xBB8)

    def lambda_1E7C():
        OP_6D(-3190, 450, -4810, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1E7C)

    def lambda_1E94():
        OP_67(0, 4520, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E94)

    def lambda_1EAC():
        OP_6B(3470, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1EAC)

    def lambda_1EBC():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1EBC)
    TurnDirection(0x101, 0x9, 400)
    SetChrSubChip(0x8, 8)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #47
        0x101,
        "#1004F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#084F#5PAh, Lena!\x02\x03",

            "#081FI think I woke Estelle up with my\x01",
            "log-chopping.\x02\x03",

            "We were just getting some quality\x01",
            "father-daughter time in!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #49
        0x9,
        "Woman",
        (
            "#866F#4POh, really?\x02\x03",

            "Estelle seems a little less enthused\x01",
            "than you, though.\x02\x03",

            "#861FDon't nag her too much, or she'll\x01",
            "get annoyed.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #50
        0x8,
        "#086F#5PWhat? Never!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_2056():
        OP_6D(-5460, 0, -9250, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2056)

    def lambda_206E():
        OP_6C(319000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_206E)
    Fade(250)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 0)
    OP_72(0x4, 0x4)
    OP_0D()
    ClearChrFlags(0x8, 0x800)
    SetChrFlags(0x8, 0x4)
    OP_8E(0x8, 0xFFFFE053, 0x0, 0xFFFFDA44, 0x9C4, 0x0)
    OP_8C(0x8, 90, 0)
    OP_8F(0x8, 0xFFFFE714, 0x0, 0xFFFFD59E, 0x9C4, 0x0)
    ClearChrFlags(0x8, 0x4)
    TurnDirection(0x8, 0x101, 400)
    OP_43(0x9, 0x0, 0x0, 0xF)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #51
        0x8,
        "#084F#6PEstelle...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #52
        0x8,
        (
            "#084F#6PYou don't hate Papa, do you?!\x02\x03",

            "#083FI know I'm not home much because of\x01",
            "my work, but...\x02\x03",

            "#082FRemember, Estelle!\x01",
            "Papa loves you more than anything!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#1026F#4PWait... Wait a...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 0x0)

    NpcTalk(    #54
        0x9,
        "Woman",
        (
            "#861F#4PAww! It's all right.\x02\x03",

            "#866FI think she's a bit shy because she\x01",
            "hasn't seen you in so long, dear.\x02\x03",

            "Isn't that right, Estelle?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)
    Sleep(500)

    ChrTalk(    #55
        0x101,
        (
            "#1026F#6PThat... That... Is that...?\x02\x03",

            "...Mom?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #56
        0x9,
        "Woman",
        (
            "#866F#4PWhy, what's this all of a sudden?\x02\x03",

            "Did you forget Mama's face?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        "#1025F#6PIt's...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_1D(0x53)
    Sleep(300)

    def lambda_230C():
        OP_6B(3190, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_230C)
    Fade(1000)
    OP_BB(0x0, 0x1, 0x44)
    OP_BD()
    OP_0D()
    Sleep(500)

    ChrTalk(    #58
        0x101,
        (
            "#297F#6PMama... It's really Mama...\x02\x03",

            "Mamaaaa...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x9,
        "#864F#4PHmm...?\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #60
        0x101,
        "#298F#6P#4SMAMAAAAAA!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_23AA():
        OP_6D(-4460, 0, -9250, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23AA)
    OP_8E(0x101, 0xFFFFF31C, 0x0, 0xFFFFD634, 0x1388, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 6)
    SetChrSubChip(0x9, 0)

    def lambda_23EF():
        OP_99(0x9, 0x0, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_23EF)
    OP_8F(0x9, 0xFFFFF4AC, 0x0, 0xFFFFD602, 0xBB8, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #61
        0x9,
        (
            "#866F#4POh, goodness!\x01",
            "Estelle, what is it?\x02\x03",

            "Did you have a bad dream?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#298F#6P*sniffle*...Umm...\x02\x03",

            "I don't remember much of it,\x01",
            "but...but...\x02\x03",

            "#297FYou were gone, Mama!\x02\x03",

            "And you couldn't come home\x01",
            "and I was sad and, and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x9,
        (
            "#863F#4PHaha...\x02\x03",

            "#866FWell, don't worry. Mama's right here.\x02\x03",

            "And I'm not going anywhere, either.\x01",
            "I promise.\x02\x03",

            "So just relax, all right, sweetie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#299F#6PO... Okay...\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #65
        0x8,
        (
            "#083F#6PErm.\x02\x03",

            "Papa is feeling a bit lonely over here,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x9,
        "#864F#4POh, darling, you're still there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "#082F#6POuch. An axe through my heart,\x01",
            "Lena.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "#861F#4PAww, come on. Just joking.\x02\x03",

            "#866FHere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        "#085F#6PAh, yes.\x02",
    )

    CloseMessageWindow()
    OP_99(0x9, 0x2, 0x0, 0x5DC)
    SetChrPos(0x101, -3400, 0, -10700, 90)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 2)
    SetChrSubChip(0x9, 0)
    OP_8F(0x101, 0xFFFFF18C, 0x0, 0xFFFFD634, 0x3E8, 0x0)
    OP_8E(0x8, 0xFFFFEB1A, 0x0, 0xFFFFD6D4, 0x3E8, 0x0)
    TurnDirection(0x101, 0x8, 400)
    Sleep(500)

    ChrTalk(    #70
        0x101,
        (
            "#299F#4P*sniffle* Heehee!\x02\x03",

            "#291FG'morning, Daddy!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2757():
        OP_6D(-5460, 0, -9250, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2757)
    OP_8E(0x101, 0xFFFFED2C, 0x0, 0xFFFFD698, 0x1388, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 0)
    OP_8F(0x8, 0xFFFFEAB6, 0x0, 0xFFFFD6D4, 0xBB8, 0x0)

    def lambda_27B0():
        OP_99(0x8, 0x0, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_27B0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #71
        0x8,
        (
            "#081F#6POh-ho! An excellent tackle!\x02\x03",

            "All right! Today, Papa will play\x01",
            "any game you want, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#293F#7PReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        (
            "#080F#6PCassius Bright never goes\x01",
            "back on his word!\x02\x03",

            "I'll play anything you want!\x01",
            "Even house!\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x8, 0x2, 0x0, 0x5DC)
    SetChrPos(0x101, -4920, 0, -10600, 270)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 0)
    OP_8F(0x101, 0xFFFFEE08, 0x0, 0xFFFFD6D4, 0x3E8, 0x0)
    Sleep(500)

    ChrTalk(    #74
        0x101,
        (
            "#290F#7PHmmm, well...\x02\x03",

            "#291FThen I wanna go fishing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        (
            "#081F#6POoh, now that's my daughter!\x01",
            "An excellent choice!\x02\x03",

            "#084FAlthough, most people think of fishing as,\x01",
            "er, a man's hobby.\x02\x03",

            "You're sure you don't want to play house?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#294F#7PNuh-uh! I wanna go fishing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        (
            "#083F#6PUhh... Do you think it's all right,\x01",
            "Lena?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x9,
        (
            "#861F#4Pt'll be fine, darling.\x01",
            "There are plenty of ways to be 'feminine.'\x02\x03",

            "#866FThough unless you brave fishers want\x01",
            "to go fishing for breakfast...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        "#084F#6POh, good idea!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #80
        0x101,
        (
            "#293F#6PBreakfast?! Yeah, yeah!\x02\x03",

            "#291FMama! I'm really hungry!\x02\x03",

            "I wanna eat soon, so I'll be\x01",
            "a big girl and help!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        "#080F#6PWell! Let me go put on some coffee.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        (
            "#861F#4PThank you, you two.\x02\x03",

            "#866FAhhhh, but first... Estelle,\x01",
            "remember to wash your hands!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_20(0xFA0)
    OP_0D()
    OP_21()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #83
        "\x07\x05Those... Those were happy days.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_1D(0x75)
    Sleep(500)
    SetMapFlags(0x2000000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T0310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_19FD end

    def Function_15_2C5E(): pass

    label("Function_15_2C5E")

    OP_8E(0xFE, 0x758, 0x0, 0xFFFFDC2E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF43E, 0x0, 0xFFFFD5EE, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_15_2C5E end

    def Function_16_2C8E(): pass

    label("Function_16_2C8E")

    EventBegin(0x0)
    OP_DB()
    LoadEffect(0x0, "map\\\\mp071_01.eff")
    LoadEffect(0x1, "map\\\\mp071_02.eff")
    LoadEffect(0x2, "map\\\\mp071_03.eff")
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x101, -12380, -200, 7130, 304)
    SetChrPos(0x8, -13750, -200, 4230, 333)
    SetChrChipByIndex(0x101, 4)
    SetChrChipByIndex(0x8, 5)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, -9360, -200, -1530, 314)
    SetChrChipByIndex(0x9, 2)
    ClearChrFlags(0x9, 0x80)
    OP_6D(-12910, -200, 5270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(152000, 0)
    OP_6E(262, 0)

    def lambda_2D6B():

        label("loc_2D6B")

        OP_99(0x101, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_2D6B")

    QueueWorkItem2(0x101, 2, lambda_2D6B)

    def lambda_2D7E():

        label("loc_2D7E")

        OP_99(0x8, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_2D7E")

    QueueWorkItem2(0x8, 2, lambda_2D7E)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1500)
    PlayEffect(0x0, 0x1, 0xFF, -13700, -1800, 7500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_9E(0x101, 0x0, 0x32, 0x12C, 0x3E8)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_2E04():

        label("loc_2E04")

        OP_99(0x101, 0x4, 0x5, 0x3E8)
        OP_48()
        Jump("loc_2E04")

    QueueWorkItem2(0x101, 2, lambda_2E04)
    OP_43(0x101, 0x3, 0x0, 0x11)
    Sleep(500)

    def lambda_2E23():

        label("loc_2E23")

        OP_99(0x8, 0x8, 0xB, 0x5DC)
        OP_48()
        Jump("loc_2E23")

    QueueWorkItem2(0x8, 2, lambda_2E23)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x8, 0x2)
    Fade(500)

    def lambda_2E5B():
        OP_96(0xFE, 0xFFFFCCF2, 0x0, 0x1022, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2E5B)
    ClearChrFlags(0x8, 0x4)
    Sleep(10)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x8, 0x1)
    OP_8E(0x8, 0xFFFFD1AC, 0xFFFFFF38, 0x13F6, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFD062, 0xFFFFFF38, 0x18EC, 0x7D0, 0x0)
    OP_8C(0x8, 293, 400)
    Sleep(500)
    OP_44(0x101, 0x2)
    Sleep(1000)

    def lambda_2ECF():
        OP_99(0xFE, 0x6, 0xE, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2ECF)
    OP_22(0x18, 0x0, 0x64)
    OP_44(0x101, 0x3)
    OP_82(0x1, 0x0)
    PlayEffect(0x2, 0x2, 0xFF, -13700, -1800, 7500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x101, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x101, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    def lambda_2F53():
        OP_6D(-11880, -200, 4500, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F53)

    def lambda_2F6B():
        OP_67(0, 8080, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2F6B)

    def lambda_2F83():
        OP_6C(140000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2F83)
    OP_8E(0x9, 0xFFFFD18E, 0xFFFFFF38, 0xC44, 0x5DC, 0x0)
    TurnDirection(0x9, 0x101, 400)
    Sleep(500)
    TurnDirection(0x8, 0x9, 400)
    Sleep(200)
    OP_99(0x101, 0xE, 0x11, 0x3E8)
    Sleep(100)
    OP_62(0x101, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    OP_DC()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #84
        (
            "\x07\x05Playing among the trees and fields,\x01",
            "watched over by loving parents...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 19)
    Return()

    # Function_16_2C8E end

    def Function_17_307F(): pass

    label("Function_17_307F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31E7")
    PlayEffect(0x1, 0x1, 0xFF, -13700, -1700, 7500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x1, 0x1, 0xFF, -13700, -1700, 7500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x1, 0x1, 0xFF, -13700, -1700, 7500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(350)
    PlayEffect(0x1, 0x1, 0xFF, -13700, -1700, 7500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0x1, 0xFF, -13700, -1700, 7500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(450)
    PlayEffect(0x1, 0x1, 0xFF, -13700, -1700, 7500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    Jump("Function_17_307F")

    label("loc_31E7")

    Return()

    # Function_17_307F end

    def Function_18_31E8(): pass

    label("Function_18_31E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_326C")
    OP_8C(0x101, 338, 0)
    Sleep(200)
    OP_8C(0x101, 293, 0)
    Sleep(200)
    OP_8C(0x101, 248, 0)
    Sleep(200)
    OP_8C(0x101, 293, 0)
    Sleep(500)
    OP_8C(0x101, 248, 0)
    Sleep(200)
    OP_8C(0x101, 293, 0)
    Sleep(200)
    OP_8C(0x101, 338, 0)
    Sleep(200)
    OP_8C(0x101, 293, 0)
    Sleep(500)
    OP_8C(0x101, 338, 0)
    Sleep(200)
    OP_8C(0x101, 293, 0)
    Sleep(500)
    Jump("Function_18_31E8")

    label("loc_326C")

    Return()

    # Function_18_31E8 end

    def Function_19_326D(): pass

    label("Function_19_326D")

    OP_DB()
    OP_6D(21780, 0, 200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(60000, 0)
    OP_6E(262, 0)
    SetChrPos(0x9, 20640, 0, -1190, 90)
    ClearChrFlags(0x9, 0x80)
    OP_72(0x6, 0x20)
    OP_72(0x6, 0x4)
    OP_6F(0x6, 1)
    OP_70(0x6, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x6, 1)
    OP_70(0x6, 0x2)
    OP_73(0x6)
    SetChrChipByIndex(0x9, 7)
    Sleep(500)
    SetChrChipByIndex(0x9, 2)
    Sleep(500)
    OP_8F(0x9, 0x50A0, 0x0, 0xFFFFFDC6, 0x7D0, 0x0)
    OP_6F(0x6, 2)
    OP_70(0x6, 0x3)
    OP_73(0x6)
    SetChrChipByIndex(0x9, 7)
    Sleep(500)
    SetChrChipByIndex(0x9, 2)
    Sleep(500)
    OP_8C(0x9, 45, 400)
    OP_8E(0x9, 0x50A0, 0x0, 0x320, 0x3E8, 0x0)
    OP_43(0x101, 0x0, 0x0, 0x14)
    OP_8C(0x9, 90, 400)

    def lambda_3370():
        OP_6D(19970, 0, 490, 4000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3370)

    def lambda_3388():
        OP_6C(50000, 4000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_3388)
    Sleep(400)
    OP_43(0x8, 0x0, 0x0, 0x15)
    Sleep(1000)

    def lambda_33A9():

        label("loc_33A9")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_33A9")

    QueueWorkItem2(0x9, 1, lambda_33A9)
    WaitChrThread(0x101, 0x0)
    OP_44(0x9, 0x1)
    OP_99(0x101, 0x10, 0x12, 0x3E8)
    Sleep(200)
    OP_8C(0x9, 90, 400)
    OP_6F(0x6, 3)
    OP_70(0x6, 0x4)
    OP_73(0x6)
    SetChrChipByIndex(0x9, 7)
    Sleep(500)
    SetChrChipByIndex(0x9, 2)
    Sleep(500)
    OP_8F(0x9, 0x50A0, 0x0, 0x5C8, 0x7D0, 0x0)
    OP_6F(0x6, 4)
    OP_70(0x6, 0x5)
    OP_73(0x6)
    SetChrChipByIndex(0x9, 7)
    Sleep(500)
    SetChrChipByIndex(0x9, 2)
    Sleep(300)
    OP_8C(0x9, 180, 400)
    OP_62(0x9, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(2000)
    OP_DC()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #85
        (
            "\x07\x05Helping with the chores...\x01",
            "Only when you wanted to, though...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 65535)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T0311   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_19_326D end

    def Function_20_34DD(): pass

    label("Function_20_34DD")

    SetChrChipByIndex(0x101, 9)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrPos(0x101, 12520, 0, 350, 90)

    def lambda_350D():
        OP_8E(0xFE, 0x4F1A, 0x0, 0xFFFFFFC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_350D)

    def lambda_3528():

        label("loc_3528")

        OP_99(0xFE, 0x1, 0x7, 0x5DC)
        OP_48()
        Jump("loc_3528")

    QueueWorkItem2(0x101, 2, lambda_3528)
    Sleep(1300)
    OP_62(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0x2)
    SetChrSubChip(0x101, 0)
    Return()

    # Function_20_34DD end

    def Function_21_355B(): pass

    label("Function_21_355B")

    SetChrChipByIndex(0x8, 9)
    SetChrSubChip(0x8, 8)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 12350, 0, 1350, 90)

    def lambda_3590():
        OP_8E(0xFE, 0x4844, 0x0, 0x3AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3590)

    def lambda_35AB():

        label("loc_35AB")

        OP_99(0xFE, 0x9, 0xF, 0x5DC)
        OP_48()
        Jump("loc_35AB")

    QueueWorkItem2(0x8, 2, lambda_35AB)
    WaitChrThread(0x8, 0x1)
    OP_44(0x8, 0x2)
    SetChrSubChip(0x8, 8)
    Return()

    # Function_21_355B end

    def Function_22_35C7(): pass

    label("Function_22_35C7")

    EventBegin(0x0)
    OP_6D(3070, 0, -13180, 0)
    OP_67(0, 7710, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2590, 0, -13750, 180)
    SetChrPos(0xA, 2450, 0, -15050, 0)
    SetChrPos(0x9, 3100, 0, -12520, 180)
    SetChrPos(0x8, 1980, 0, -12580, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0xA, 10)
    SetChrSubChip(0xA, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #86
        0xA,
        (
            "#870FWell, it's about time I head out.\x02\x03",

            "Estelle, I'll be back to play again in\x01",
            "the spring, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#295F#6PWell, okaaay, but...\x02\x03",

            "You just came by to play and now\x01",
            "you're going home already...\x02\x03",

            "Can't you stay another day, Schera?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xA,
        (
            "#872FUm... Well, I'd really love to, but...\x02\x03",

            "Everyone at the circus is waiting for me,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#295F#6PAwwww, who cares about the circus?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x9,
        (
            "#861F#6PNow, now, Estelle.\x01",
            "Don't be selfish.\x02\x03",

            "#866FSchera, thank you again\x01",
            "for coming over.\x02\x03",

            "You always go out of your\x01",
            "way for Estelle's sake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        (
            "#871FNah, it's okay.\x01",
            "I love playing with her, too.\x02\x03",

            "#875FBesides, Mrs. Bright, your cooking\x01",
            "is AMAZING! Like I'd ever miss that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x9,
        "#861F#6POh, don't flatter me too much!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x8,
        (
            "#080F#6PCome by to play any time you want,\x01",
            "Schera.\x02\x03",

            "#081FI'll even treat you to some of my\x01",
            "special reserve brandy next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xA,
        "#875FWait... REALLY?! SWEET!!!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)
    Sleep(500)

    ChrTalk(    #95
        0x9,
        "#863F#3S#4PDaaaar-liiiiiing...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x8, 0x9, 400)
    Sleep(500)

    ChrTalk(    #96
        0x8,
        "#083F#6PHah, it was a joke. Of course.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)
    OP_8C(0x8, 180, 400)

    ChrTalk(    #97
        0x9,
        (
            "#862F#6PSchera, please don't take Cassius\x01",
            "up on that offer.\x02\x03",

            "I don't care how much you want to\x01",
            "try it, you're only twelve.\x02\x03",

            "Maybe you can have a sip or two,\x01",
            "but absolutely nothing serious until\x01",
            "you're an adult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xA,
        "#873FAww, but--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x9,
        "#861F#3S#6PScheeee-raaaa...\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #100
        0xA,
        (
            "#874FUh, yeah, yeah!\x01",
            "Totally waitin' till I'm older!\x01",
            "Like, totally.\x02\x03",

            "I wish someone would let me try\x01",
            "a little, though...\x02\x03",

            "Mr. Harvey and Luci don't let me\x01",
            "have any, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x9,
        (
            "#866F#6PThat's a good thing.\x01",
            "Trust me.\x02\x03",

            "#861FAnyway, do give our regards to\x01",
            "everyone at the circus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        (
            "#080F#6PInvite Mr. Harvey and everyone\x01",
            "else next time, too, if you wish.\x02\x03",

            "I'd be happy to host a barbecue\x01",
            "in the garden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xA,
        (
            "#875FOkay, I'll be sure to tell them!\x02\x03",

            "#872FWell, goodbye, Estelle. Be good!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#291F#6PI wiiiiill!\x02\x03",

            "Bye-bye, Schera!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)

    def lambda_3DAC():
        OP_6D(3430, -1000, -25690, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DAC)

    def lambda_3DC4():
        OP_8E(0xFE, 0xD34, 0xFFFFFC18, 0xFFFF79BE, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3DC4)
    WaitChrThread(0xA, 0x1)
    SetChrFlags(0xA, 0x80)
    Fade(1000)
    OP_6D(2730, 0, -12880, 0)
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #105
        0x9,
        (
            "#866F#6PHmm... It does feel lonelier,\x01",
            "somehow, whenever she leaves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x8,
        (
            "#080F#6PShe did say she'll be returning in\x01",
            "the spring.\x02\x03",

            "I do have some time off around then,\x01",
            "so we'll make it a big party next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x9,
        "#861FThat would be perfect.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101)
    OP_8C(0x101, 0, 400)

    ChrTalk(    #108
        0x101,
        (
            "#290FDaddy? Mommy?\x02\x03",

            "#291FI... I wanna sib-wing too!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(80)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #109
        0x8,
        "#084F#6PEr, what?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x9,
        "#864F#6POh! Umm, well...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#295FI mean, I only get to play with Schera\x01",
            "sometimes, so...\x02\x03",

            "I wanna sibwing I can always play with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x8,
        (
            "#083F#6PY-You want...um.\x02\x03",

            "That's, um, quite a request, Estelle.\x01",
            "How do I...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x9,
        (
            "#861F#6POh? So you want a little\x01",
            "brother or sister, sweetie?\x02\x03",

            "#860FWell, you know, this is one thing\x01",
            "we can't promise we can give you.\x02\x03",

            "It's up to Aidios to decide when people\x01",
            "are born.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        "#293FReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x9,
        (
            "#866F#6PYes. You see, when the Goddess decides\x01",
            "to give parents a child, She sends a beautiful\x01",
            "bird from the cloud tops, carrying the baby.\x02\x03",

            "And then, often late at night, the bird delivers\x01",
            "the baby to the mama and papa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#290FOoooh, I get it!\x02\x03",

            "#291FI'll pray reeeeeally hard to the Goddess,\x01",
            "then!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x9,
        (
            "#861F#6PWell, that might help, too.\x02\x03",

            "#866FBut perhaps if you're a very good girl,\x01",
            "Estelle, the Goddess will send us one\x01",
            "as a reward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        "#294FI'll be the goodest girl ever, then!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)
    Sleep(500)

    ChrTalk(    #119
        0x8,
        "#080F#6PYou're amazing at this, as always.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #120
        0x9,
        (
            "#866F#4PDarling, don't act like you\x01",
            "have no part in this.\x02\x03",

            "#861FYou'll have some hard work\x01",
            "to do, too, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #121
        0x8,
        (
            "#081F#6PYes indeed!\x02\x03",

            "Welllll, we COULD get to work right now,\x01",
            "if you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x9,
        (
            "#863F#4PHee, perhaps later.\x02\x03",

            "#860FRight now I need to get dinner ready.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #123
        0x8,
        "#083F#6PEr. Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        "#293FHuuuuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x9,
        (
            "#861F#4PHWell, I'll be in the kitchen.\x02\x03",

            "#866FWhat are you two going to be up to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x8,
        "#080F#6PWhat, indeed.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    Sleep(500)

    ChrTalk(    #127
        0x8,
        (
            "#081F#6PEstelle, want to go fishing with\x01",
            "Papa again?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)

    ChrTalk(    #128
        0x101,
        (
            "#290FMmmmm. No, I'm okay.\x02\x03",

            "I think I just wanna play\x01",
            "around here for a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x8,
        (
            "#084F#6P#3S*gasp*!#2S\x02\x03",

            "#083FWell, I suppose I can catch up\x01",
            "on a few things in my office...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x9,
        (
            "#861F#6PPoor thing, to be shut down\x01",
            "by both of the women in his life.\x02\x03",

            "#865FEstelle. Be careful where you play,\x01",
            "all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x8,
        (
            "#080F#6PYes, don't play near the pond\x01",
            "when you're alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        "#291FOkaaay!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_8C(0x8, 0, 400)

    def lambda_473A():
        OP_6D(2040, 0, -9450, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_473A)

    def lambda_4752():
        OP_8E(0xFE, 0x780, 0x1C2, 0xFFFFF1F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4752)
    Sleep(200)
    OP_8C(0x9, 315, 400)

    def lambda_4779():
        OP_8E(0xFE, 0x76C, 0x0, 0xFFFFD8FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4779)
    WaitChrThread(0x9, 0x1)

    def lambda_4799():
        OP_8E(0xFE, 0x76C, 0x1C2, 0xFFFFECAA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4799)
    WaitChrThread(0x8, 0x1)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)

    def lambda_47CF():
        OP_8E(0xFE, 0x8A2, 0x1C2, 0xFFFFFA4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_47CF)
    WaitChrThread(0x9, 0x1)
    Sleep(300)

    def lambda_47F4():
        OP_8E(0xFE, 0x8A2, 0x1C2, 0xFFFFFA4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_47F4)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x80)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x80)
    OP_72(0x0, 0x800)
    OP_6F(0x0, 59)
    OP_70(0x0, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    OP_71(0x0, 0x10)
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_6D(2590, 0, -13750, 2000)
    OP_63(0x101)
    Sleep(600)

    ChrTalk(    #133
        0x101,
        (
            "#290F#6PA sib-wing, huh...?\x02\x03",

            "#293F...\x02\x03",

            "#295FThat's funny...\x01",
            "My heart feels kinda weird...\x02\x03",

            "It's like...I forgot something...somewhere...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 500)
    Sleep(500)
    OP_8C(0x101, 270, 500)
    Sleep(500)
    OP_8C(0x101, 180, 500)
    Sleep(500)

    ChrTalk(    #134
        0x101,
        "#292F#6PG-Gotta find it...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1834)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_22_35C7 end

    def Function_23_494D(): pass

    label("Function_23_494D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CF9")
    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C90")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(-7910, 0, 2760, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -8650, 0, 2630, 90)
    OP_0D()
    Sleep(200)

    ChrTalk(    #135
        0x9,
        (
            "#864F#6PLet's see...\x02\x03",

            "That should be the last of the onions,\x01",
            "and now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        "#291F#6PMama! There you are!\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #137
        0x9,
        (
            "#861F#4POh, Estelle!\x02\x03",

            "#866FTrying to sneak a bit of\x01",
            "food already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        "#290F#6POh, no. Umm, I gotta question, Mama.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x9,
        "#864F#4POh?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #140
        (
            "\x07\x05Estelle explained that she was looking for the\x01",
            "key to the storage room.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #141
        0x9,
        (
            "#864F#4POh, my. You want to explore the storage room?\x02\x03",

            "#863FHmmm. It's all dusty, though.\x01",
            "You'll get very dirty...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        "#295F#6PAwwwww!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x9,
        (
            "#860F#4PHm...\x02\x03",

            "#861FWell, all right.\x02\x03",

            "#865FYou know the small set of drawers\x01",
            "near Mama's bed, right?\x02\x03",

            "The key's in the topmost drawer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        "#291F#6PThanks, Mama!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 400)
    ClearChrFlags(0x9, 0x10)
    OP_A2(0x1837)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Jump("loc_4CF6")

    label("loc_4C90")


    ChrTalk(    #145
        0x9,
        (
            "#865FYou know the small set of drawers\x01",
            "near Mama's bed, right?\x02\x03",

            "The key's in the topmost drawer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CF6")

    TalkEnd(0x9)

    label("loc_4CF9")

    Return()

    # Function_23_494D end

    def Function_24_4CFA(): pass

    label("Function_24_4CFA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x3F9), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D10")
    Return()

    label("loc_4D10")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D21")
    Call(0, 25)
    Return()

    label("loc_4D21")

    SetMapFlags(0x80)
    OP_C2()
    OP_48()
    EventBegin(0x0)
    Fade(500)
    SetChrChipByIndex(0x101, 12)
    SetChrSubChip(0x101, 0)
    OP_0D()
    OP_20(0x5DC)
    OP_21()
    OP_DB()
    OP_22(0x11B, 0x0, 0x64)

    def lambda_4D4C():

        label("loc_4D4C")

        OP_99(0x101, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_4D4C")

    QueueWorkItem2(0x101, 2, lambda_4D4C)
    Sleep(10000)
    Sleep(2000)
    Sleep(1500)
    Sleep(1500)
    OP_44(0x101, 0x2)
    OP_1D(0x75)
    Fade(500)
    SetChrSubChip(0x101, 8)
    OP_0D()
    Sleep(500)
    OP_DC()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E24")

    ChrTalk(    #146
        0x101,
        (
            "#290FThe sound is really pretty!\x01",
            "Kinda hard to play, though.\x02\x03",

            "#296FBut...it's funny...\x02\x03",

            "I think I heard this sound before...\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    OP_A2(0x0)
    Jump("loc_4E80")

    label("loc_4E24")


    ChrTalk(    #147
        0x101,
        (
            "#296FBut...where have I heard it before?\x02\x03",

            "Maybe if I try playing it...\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()

    label("loc_4E80")

    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_24_4CFA end

    def Function_25_4E88(): pass

    label("Function_25_4E88")

    SetMapFlags(0x80)
    OP_C2()
    OP_48()
    EventBegin(0x0)
    OP_20(0x5DC)
    Fade(1000)
    SetChrPos(0x101, -5540, 3450, 2200, 270)
    OP_6D(-5540, 3450, 2200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_4EF0():
        OP_8E(0xFE, 0xFFFFE6A6, 0xD7A, 0x8B6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4EF0)

    def lambda_4F0B():
        OP_6D(-6490, 3450, 2230, 1200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F0B)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x101, 12)
    SetChrSubChip(0x101, 0)
    OP_0D()
    OP_20(0x5DC)
    OP_21()
    OP_22(0x11B, 0x0, 0x64)

    def lambda_4F4D():

        label("loc_4F4D")

        OP_99(0x101, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_4F4D")

    QueueWorkItem2(0x101, 2, lambda_4F4D)
    Sleep(10000)
    Sleep(2000)
    Sleep(1500)
    Sleep(1500)
    OP_44(0x101, 0x2)
    Fade(500)
    SetChrSubChip(0x101, 8)
    OP_0D()
    Sleep(500)

    ChrTalk(    #148
        0x101,
        (
            "#295FAww... I can't play it at all.\x02\x03",

            "#292FThis har-mo-ni-ca thing is hard!\x02\x03",

            "It seems like it should be easy,\x01",
            "but it's waaay too hard...!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #149
        (
            "\x07\x05Compared to what it takes to use a staff,\x01",
            "I think the harmonica is much easier.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #150
        "It's really just a matter of concentration.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #151
        0x101,
        "#293FHuh...?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #152
        (
            "Overall, though, it's a great song.\x01",
            "Cheerful, yet somehow wistful...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #153
        (
            "I like your other songs too, of course,\x01",
            "but this one's my favorite.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #154
        "Er... What's it called again?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(    #155
        0x101,
        (
            "#292F...\x02\x03",

            "It was...where...\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 12)
    SetChrSubChip(0x101, 0)
    OP_0D()
    OP_DB()
    OP_22(0x11C, 0x0, 0x64)

    def lambda_5207():

        label("loc_5207")

        OP_99(0x101, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_5207")

    QueueWorkItem2(0x101, 2, lambda_5207)
    Sleep(20000)
    OP_44(0x101, 0x2)
    Fade(500)
    SetChrSubChip(0x101, 9)
    OP_0D()
    Sleep(500)
    OP_DC()

    ChrTalk(    #156
        0x101,
        (
            "#295FNo, no. That's not it.\x02\x03",

            "#290FNo, it goes like...this.\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    Fade(500)
    SetChrChipByIndex(0x101, 12)
    SetChrSubChip(0x101, 0)
    OP_0D()

    def lambda_5285():
        OP_6B(2600, 15000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5285)

    def lambda_5295():

        label("loc_5295")

        OP_99(0x101, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_5295")

    QueueWorkItem2(0x101, 2, lambda_5295)
    OP_1D(0x46)
    OP_1F(0x50, 0xC8)
    Sleep(10000)
    Fade(5000)
    OP_6D(-18140, 3450, 51220, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -18140, 3450, 51220, 264)
    OP_0D()
    LoadEffect(0x0, "map\\\\mp058_00.eff")
    Fade(2500)
    OP_9F(0x101, 0x0, 0x0, 0x0, 0x96, 0x0)
    SetChrChipByIndex(0x101, 14)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x9C4)
    OP_0D()
    OP_21()
    OP_44(0x101, 0x2)
    Sleep(1000)
    OP_99(0x101, 0x8, 0x9, 0x320)
    Sleep(500)
    Fade(500)
    SetChrSubChip(0x101, 10)
    OP_0D()
    Sleep(500)
    OP_DC()

    ChrTalk(    #157
        0x101,
        (
            "#1012FHey, Joshua...\x02\x03",

            "I... 'The Whereabouts of Light'...\x01",
            "I finally played it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, -14330, 3450, 50770, 270)
    ClearChrFlags(0x9, 0x80)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMessageWindowPos(300, 50, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #158
        "\x07\x05Ahh... That's such a lovely song.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x50)
    OP_BB(0x0, 0x1, 0x0)
    OP_BD()
    SetChrChipByIndex(0x101, 65535)

    def lambda_5452():
        OP_6D(-15800, 3450, 51080, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5452)

    def lambda_546A():
        OP_67(0, 8300, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_546A)

    def lambda_5482():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_5482)
    OP_8C(0x101, 90, 300)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x9, 0x2)

    ChrTalk(    #159
        0x101,
        "#1025F#6PMom...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x9,
        (
            "\x07\x05#866FWell... I'm not really your mother, Estelle.\x02\x03",

            "I'm...a phantom, I suppose.\x01",
            "A memory of the Lena Bright you once knew.\x02\x03",

            "As I suspect you've already realized,\x01",
            "everything that's happened until now\x01",
            "has been a dream.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        (
            "#1016F#6PYeah, I kind of figured.\x02\x03",

            "#1025FEven if it is a dream, though...\x01",
            "you're still my mom, Mom.\x02\x03",

            "This was...maybe the happiest time of my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x9,
        (
            "\x07\x05#861FA lot of people feel that way\x01",
            "about their childhoods, Estelle.\x02\x03",

            "#860FBut even so...you're going, aren't you?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        (
            "#1012F#6PYeah.\x02\x03",

            "#1017FThere are people waiting for me,\x01",
            "and there's something really important\x01",
            "I've got to do, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x9,
        (
            "\x07\x05#863FI see.\x02\x03",

            "#866FJoshua, you said?\x02\x03",

            "He sounds like quite\x01",
            "a handsome young man.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #165
        0x101,
        "#1013F#6POh, Mom!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x9,
        (
            "\x07\x05#861FLook at you! You're beet red, sweetie!\x02\x03",

            "#866FIt's funny.\x02\x03",

            "I'm not truly 'Lena,' and yet,\x01",
            "I feel...peaceful.\x02\x03",

            "My little Estelle is all grown up\x01",
            "and strong...\x02\x03",

            "She's even found true love.\x02\x03",

            "#861FAs a mother, I couldn't be any happier.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        (
            "#1026F#6PMom...\x02\x03",

            "#1027FI... I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x9,
        (
            "\x07\x05#866FNow, now. Don't make that face.\x02\x03",

            "Didn't you remember you have\x01",
            "something you need to do?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 7)

    def lambda_593B():
        OP_6D(-13040, 3450, 52280, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_593B)

    def lambda_5953():
        OP_67(0, 3380, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5953)

    def lambda_596B():
        OP_6C(71000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_596B)

    def lambda_597B():
        OP_6E(500, 4000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_597B)

    def lambda_598B():
        OP_6B(1870, 4000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_598B)
    Sleep(1000)
    PlayEffect(0x0, 0x0, 0xFF, -8090, 4000, 54040, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x11D, 0x1, 0x46)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    ClearChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 0)
    OP_8C(0x9, 306, 0)

    ChrTalk(    #169
        0x9,
        (
            "\x07\x05#863F#4PThat is the end of the dream.\x02\x03",

            "The way back to the waking world.\x02\x03",

            "#866FNow...go on with your head held high.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        "#1025F#5PYeah...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 102, 400)
    Sleep(500)

    ChrTalk(    #171
        0x101,
        (
            "#1016F#1PHaha. I kinda wanted to eat your omelet\x01",
            "again before the end, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x9,
        (
            "\x07\x05#864F#4PReally?\x02\x03",

            "#860FIf you want to have it,\x01",
            "you should try making it yourself.\x02\x03",

            "Your omelet will probably be just as\x01",
            "good as mine, if not better!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        "#1004F#1PWhat do you--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x9,
        (
            "\x07\x05#861F#4PEverything you are as a parent--your skills,\x01",
            "your dreams, your hopes for their future--you\x01",
            "pass down to your children, knowingly or not.\x02\x03",

            "Even if you never have a chance to teach them\x01",
            "directly, everything you do, every thought and\x01",
            "word, they carry with them as long as they live.\x02\x03",

            "#866FYou carry me with you, Estelle.\x01",
            "Omelet and all.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        (
            "#1025F#1PMom...\x02\x03",

            "...\x02\x03",

            "#1012FYeah... I guess I do.\x02\x03",

            "#1017FMom...I'll be going, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x9,
        (
            "\x07\x05#861F#4PGive my regards to your father...\x01",
            "and to Joshua.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#1017F#1PI will... I promise!\x02\x03",

            "#1018FGoodbye...Mom!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 70, 400)
    Sleep(500)

    def lambda_5DE1():
        OP_6D(-9890, 3450, 53440, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5DE1)
    OP_43(0x101, 0x1, 0x0, 0x1A)
    Sleep(500)

    def lambda_5E05():

        label("loc_5E05")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_5E05")

    QueueWorkItem2(0x9, 3, lambda_5E05)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)
    OP_82(0x0, 0x2)
    OP_24(0x11D, 0x3C)
    Sleep(300)
    OP_24(0x11D, 0x32)
    Sleep(300)
    OP_24(0x11D, 0x28)
    Sleep(300)
    OP_24(0x11D, 0x1E)
    Sleep(300)
    OP_24(0x11D, 0x14)
    Sleep(300)
    OP_24(0x11D, 0xA)
    Sleep(300)
    OP_23(0x11D)

    def lambda_5E61():
        OP_6D(-11020, 3450, 52690, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5E61)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #178
        0x9,
        (
            "\x07\x05#866F#5PGoodbye...\x02\x01",

            "#861FMy darling Estelle.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    OP_44(0x101, 0x1)
    ClearMapFlags(0x2000000)
    OP_D6(0x1)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C0303   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_4E88 end

    def Function_26_5EE1(): pass

    label("Function_26_5EE1")

    OP_8E(0xFE, 0xFFFFD6FC, 0xD7A, 0xD066, 0x1388, 0x0)

    def lambda_5EFB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5EFB)
    OP_8E(0xFE, 0xFFFFE066, 0xD7A, 0xD318, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_26_5EE1 end

    def Function_27_5F21(): pass

    label("Function_27_5F21")

    EventBegin(0x1)

    ChrTalk(    #179
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_5F4D():
        OP_6D(-12120, 0, 6790, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5F4D)

    def lambda_5F65():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5F65)

    def lambda_5F75():
        OP_6C(0, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_5F75)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #180
        "\x07\x05Try fishing?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Hook, Line, and Sinker\x01",      # 0
            "Spare the Rod\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60C3")
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0xE, 0x5, 0xFFFFD008, 0x0, 0x19DC, 0x13B, 0xFFFFC478, 0xFFFFF95C, 0x2184)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)), "loc_60BD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60B7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60B4")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x20)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #181
        "\x07\x05Recorded Bright Home fishing spot in Bracer Notebook.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_60B4")

    Jump("loc_60BD")

    label("loc_60B7")

    OP_28(0x73, 0x1, 0x2000)

    label("loc_60BD")

    OP_0D()
    EventEnd(0x1)
    Jump("loc_60D2")

    label("loc_60C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60D2")
    EventEnd(0x1)

    label("loc_60D2")

    Return()

    # Function_27_5F21 end

    def Function_28_60D3(): pass

    label("Function_28_60D3")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
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
        (0, "loc_614F"),
        (1, "loc_6155"),
        (SWITCH_DEFAULT, "loc_615B"),
    )


    label("loc_614F")

    OP_A2(0x1200)
    Jump("loc_615B")

    label("loc_6155")

    OP_A2(0x1201)
    Jump("loc_615B")

    label("loc_615B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_6169")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_616D")

    label("loc_6169")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_616D")

    Return()

    # Function_28_60D3 end

    def Function_29_616E(): pass

    label("Function_29_616E")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_29_616E end

    def Function_30_61C0(): pass

    label("Function_30_61C0")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 4)), scpexpr(EXPR_END)), "loc_6226")

    ChrTalk(    #182
        0x101,
        (
            "#290FI shouldn't go without an adult.\x02\x03",

            "I'd better get home before someone scolds me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6274")

    label("loc_6226")


    ChrTalk(    #183
        0x101,
        (
            "#1011F... I can hear sounds from the house.\x02\x03",

            "I'd better go check it out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6274")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_30_61C0 end

    SaveToFile()

Try(main)
