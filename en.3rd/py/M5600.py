from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M5600   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5600.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        'Kilika',                               # 9
        'Shadow Cougar',                        # 10
        'Shadow Cougar',                        # 11
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02610 ._CH',             # 00
        'ED6_DT27/CH04400 ._CH',             # 01
        'ED6_DT27/CH04401 ._CH',             # 02
        'ED6_DT27/CH04404 ._CH',             # 03
        'ED6_DT27/CH04405 ._CH',             # 04
        'ED6_DT27/CH04405 ._CH',             # 05
        'ED6_DT29/CH14760 ._CH',             # 06
        'ED6_DT29/CH14761 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH02610P._CP',             # 00
        'ED6_DT27/CH04400P._CP',             # 01
        'ED6_DT27/CH04401P._CP',             # 02
        'ED6_DT27/CH04404P._CP',             # 03
        'ED6_DT27/CH04405P._CP',             # 04
        'ED6_DT27/CH04405P._CP',             # 05
        'ED6_DT29/CH14760P._CP',             # 06
        'ED6_DT29/CH14761P._CP',             # 07
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 35980,
        Y                   = -1000,
        Z                   = 10090,
        Range               = 4000,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = 1400,
        TriggerZ            = 8900,
        TriggerY            = -340,
        TriggerRange        = 100,
        ActorX              = 760,
        ActorZ              = 8900,
        ActorY              = -300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 15000,
        TriggerZ            = 10,
        TriggerY            = -4550,
        TriggerRange        = 800,
        ActorX              = 15000,
        ActorZ              = 1010,
        ActorY              = -4250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1B2",          # 00, 0
        "Function_1_254",          # 01, 1
        "Function_2_2C4",          # 02, 2
        "Function_3_3C8",          # 03, 3
        "Function_4_E74",          # 04, 4
        "Function_5_1128",         # 05, 5
        "Function_6_1131",         # 06, 6
        "Function_7_38CE",         # 07, 7
        "Function_8_3968",         # 08, 8
        "Function_9_3A02",         # 09, 9
        "Function_10_3A91",        # 0A, 10
        "Function_11_3B2A",        # 0B, 11
        "Function_12_49FF",        # 0C, 12
        "Function_13_55D4",        # 0D, 13
        "Function_14_567B",        # 0E, 14
        "Function_15_5722",        # 0F, 15
        "Function_16_58B9",        # 10, 16
        "Function_17_5A1D",        # 11, 17
        "Function_18_5B33",        # 12, 18
        "Function_19_5B81",        # 13, 19
        "Function_20_5B88",        # 14, 20
    )


    def Function_0_1B2(): pass

    label("Function_0_1B2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D1")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_1CA"),
        (SWITCH_DEFAULT, "loc_1D1"),
    )


    label("loc_1CA")

    Event(0, 15)
    Jump("loc_1D1")

    label("loc_1D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_1EF")
    OP_A3(0x2505)
    OP_64(0x0, 0x1)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 13)
    Jump("loc_222")

    label("loc_1EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_20D")
    OP_A3(0x2506)
    OP_64(0x0, 0x1)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 14)
    Jump("loc_222")

    label("loc_20D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_222")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    Event(0, 12)

    label("loc_222")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23E")
    Event(0, 5)

    label("loc_23E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_253")
    OP_4F(0x64, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_253")

    Return()

    # Function_0_1B2 end

    def Function_1_254(): pass

    label("Function_1_254")

    OP_16(0x2, 0xFA0, 0xFFFE6DA8, 0xFFFE1F88, 0x2300A7)
    OP_22(0x1C5, 0x0, 0x64)
    OP_1B(0x4, 0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56B, 0)), scpexpr(EXPR_END)), "loc_291")
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 30)
    OP_64(0x1, 0x1)
    Jump("loc_29B")

    label("loc_291")

    OP_72(0x1000, 0x0)
    ExitThread()
    OP_65(0x1, 0x1)

    label("loc_29B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A9")
    OP_72(0x1001, 0x0)
    ExitThread()

    label("loc_2A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x567, 6)), scpexpr(EXPR_END)), "loc_2B4")
    OP_64(0x0, 0x1)

    label("loc_2B4")

    OP_1C(0x1, 0x0, 0x13)
    OP_1C(0x2, 0x0, 0x13)
    OP_1C(0x3, 0x0, 0x13)
    Return()

    # Function_1_254 end

    def Function_2_2C4(): pass

    label("Function_2_2C4")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)
    AddSepith(0x0, 0x3E8)
    AddSepith(0x1, 0x3E8)
    AddSepith(0x2, 0x3E8)
    AddSepith(0x3, 0x3E8)
    AddSepith(0x4, 0x3E8)
    AddSepith(0x5, 0x3E8)
    AddSepith(0x6, 0x3E8)

    AnonymousTalk(    #0
        (
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x1000\x01",
            "#57IWater Sepith x1000\x01",
            "#58IFire Sepith x1000\x01",
            "#59IWind Sepith x1000\x01",
            "#62ITime Sepith x1000\x01",
            "#60ISpace Sepith x1000\x01",
            "#61IMirage Sepith x1000.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2B3E)
    OP_64(0x0, 0x1)
    TalkEnd(0xFF)
    Return()

    # Function_2_2C4 end

    def Function_3_3C8(): pass

    label("Function_3_3C8")

    OP_DE(0x0, 0x4, 0x1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 6350, -6000, -28630, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42D")
    SetChrPos(0xEF, 7130, -6000, -27730, 90)
    SetChrPos(0xF0, 6190, -6000, -26980, 90)
    SetChrPos(0xF1, 5290, -6000, -27840, 90)
    Jump("loc_4B2")

    label("loc_42D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_471")
    SetChrPos(0xF0, 7130, -6000, -27730, 90)
    SetChrPos(0xEF, 6190, -6000, -26980, 90)
    SetChrPos(0xF1, 5290, -6000, -27840, 90)
    Jump("loc_4B2")

    label("loc_471")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B2")
    SetChrPos(0xF1, 7130, -6000, -27730, 90)
    SetChrPos(0xEF, 6190, -6000, -26980, 90)
    SetChrPos(0xF0, 5290, -6000, -27840, 90)

    label("loc_4B2")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(5440, -6000, -27010, 0)
    OP_67(0, 7590, -10000, 0)
    OP_6B(2730, 0)
    OP_6C(314000, 0)
    OP_6E(283, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_621():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_621)

    def lambda_633():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_633)

    def lambda_645():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_645)

    def lambda_657():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_657)
    Sleep(1500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AC")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_713")

    label("loc_6AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D4")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_713")

    label("loc_6D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FC")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_713")

    label("loc_6FC")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_713")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_740")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7A7")

    label("loc_740")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_768")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7A7")

    label("loc_768")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_790")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7A7")

    label("loc_790")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_7A7")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D4")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_83B")

    label("loc_7D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FC")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_83B")

    label("loc_7FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_824")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_83B")

    label("loc_824")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_83B")

    Sleep(1000)

    ChrTalk(    #1
        0x10A,
        "#814F#5POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        "#1079F#5POh, hey. I know this place...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    ClearMapFlags(0x10)
    OP_6D(13650, -6360, -11350, 0)
    OP_67(0, 6350, -10000, 0)
    OP_6B(8680, 0)
    OP_6C(26000, 0)
    OP_6E(394, 0)

    def lambda_8D1():
        OP_6D(13980, 3870, 12100, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_8D1)

    def lambda_8E9():
        OP_67(0, 9730, -10000, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_8E9)

    def lambda_901():
        OP_6B(10170, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_901)

    def lambda_911():
        OP_6C(21000, 7000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_911)

    def lambda_921():
        OP_6E(380, 7000)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_921)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BC")

    def lambda_944():
        OP_8F(0xFE, 0x32E6, 0xFFFFE89A, 0xFFFF9610, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_944)
    Sleep(300)

    def lambda_964():
        OP_8F(0xFE, 0x34D0, 0xFFFFE8E0, 0xFFFF90A2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_964)
    Sleep(300)

    def lambda_984():
        OP_8F(0xFE, 0x2BB6, 0xFFFFE8CC, 0xFFFF920A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_984)
    Sleep(300)

    def lambda_9A4():
        OP_8F(0xFE, 0x2D6E, 0xFFFFE8FE, 0xFFFF8CF6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_9A4)
    Jump("loc_AD1")

    label("loc_9BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A48")

    def lambda_9D0():
        OP_8F(0xFE, 0x32E6, 0xFFFFE89A, 0xFFFF9610, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_9D0)
    Sleep(300)

    def lambda_9F0():
        OP_8F(0xFE, 0x34D0, 0xFFFFE8E0, 0xFFFF90A2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9F0)
    Sleep(300)

    def lambda_A10():
        OP_8F(0xFE, 0x2BB6, 0xFFFFE8CC, 0xFFFF920A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_A10)
    Sleep(300)

    def lambda_A30():
        OP_8F(0xFE, 0x2D6E, 0xFFFFE8FE, 0xFFFF8CF6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_A30)
    Jump("loc_AD1")

    label("loc_A48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD1")

    def lambda_A5C():
        OP_8F(0xFE, 0x32E6, 0xFFFFE89A, 0xFFFF9610, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_A5C)
    Sleep(300)

    def lambda_A7C():
        OP_8F(0xFE, 0x34D0, 0xFFFFE8E0, 0xFFFF90A2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A7C)
    Sleep(300)

    def lambda_A9C():
        OP_8F(0xFE, 0x2BB6, 0xFFFFE8CC, 0xFFFF920A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_A9C)
    Sleep(300)

    def lambda_ABC():
        OP_8F(0xFE, 0x2D6E, 0xFFFFE8FE, 0xFFFF8CF6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_ABC)

    label("loc_AD1")

    OP_C8(0x200, 0x46, "C_PLAC35._CH", 0x0, 0x3E8)
    WaitChrThread(0xEE, 0x0)

    def lambda_AF1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_AF1)
    WaitChrThread(0xEF, 0x0)

    def lambda_B04():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_B04)
    WaitChrThread(0xF0, 0x0)

    def lambda_B17():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_B17)
    WaitChrThread(0xF1, 0x0)

    def lambda_B2A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_B2A)
    WaitChrThread(0x109, 0x1)
    Sleep(1000)
    Sleep(300)
    Fade(1000)
    SetMapFlags(0x10)
    OP_6D(13790, -6020, -26390, 0)
    OP_67(0, 5960, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(45000, 0)
    OP_6E(300, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C38")

    ChrTalk(    #3
        0x101,
        "#1002F#6PThis is that lakeside laboratory, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        (
            "#1063F#6PYeah. The one that Ouroboros used as its\x01",
            "base of operations in Liberl at one point.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CBF")

    label("loc_C38")


    ChrTalk(    #5
        0x109,
        (
            "#1065F#6PIt's the lakeside laboratory.\x02\x03",

            "#1063FYeah. The one that Ouroboros used as its\x01",
            "base of operations in Liberl at one point.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D0B")

    ChrTalk(    #6
        0x10F,
        (
            "#1443F#6PYou'd mentioned this place in your report,\x01",
            "yes?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D65")

    ChrTalk(    #7
        0x102,
        (
            "#1502F#6P...This is the place where Weissmann\x01",
            "abducted Estelle, is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D65")


    ChrTalk(    #8
        0x10A,
        (
            "#812F#5PCan't say I'm excited to be back here.\x02\x03",

            "#813FSomething seems kind of...odd about it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DF3")

    ChrTalk(    #9
        0x110,
        "#1305F#6P(Well, well...)\x02",
    )

    CloseMessageWindow()

    label("loc_DF3")


    ChrTalk(    #10
        0x109,
        (
            "#1063F#6PI get that same feeling. Well, let's go and get\x01",
            "a closer look. Maybe we'll figure out what it is.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B0A)
    OP_28(0x38, 0x1, 0x4)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_3_3C8 end

    def Function_4_E74(): pass

    label("Function_4_E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 4)), scpexpr(EXPR_END)), "loc_E7C")
    Return()

    label("loc_E7C")

    EventBegin(0x0)
    Fade(500)
    OP_6D(38130, -40, 10900, 0)
    OP_67(0, 6210, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(314000, 0)
    OP_6E(276, 0)
    SetChrPos(0x109, 39130, -40, 9220, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F15")
    SetChrPos(0xEF, 39560, -50, 10470, 270)
    SetChrPos(0xF0, 40800, -70, 8790, 270)
    SetChrPos(0xF1, 40980, -70, 10390, 270)
    Jump("loc_F9A")

    label("loc_F15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F59")
    SetChrPos(0xF0, 39560, -50, 10470, 270)
    SetChrPos(0xEF, 40800, -70, 8790, 270)
    SetChrPos(0xF1, 40980, -70, 10390, 270)
    Jump("loc_F9A")

    label("loc_F59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F9A")
    SetChrPos(0xF1, 39560, -50, 10470, 270)
    SetChrPos(0xEF, 40800, -70, 8790, 270)
    SetChrPos(0xF0, 40980, -70, 10390, 270)

    label("loc_F9A")

    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_104C")

    ChrTalk(    #11
        0x101,
        (
            "#1020F#6PW-Wait a second...\x02\x03",

            "Wasn't this door on the left side of the building\x01",
            "last time we were here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10A,
        "#1317F#6PActually, yeah. I'm sure of it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_10B8")

    label("loc_104C")


    ChrTalk(    #13
        0x10A,
        (
            "#1317F#6PW-Wait a second...\x02\x03",

            "Wasn't this door on the left side of the building\x01",
            "last time we were here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B8")


    ChrTalk(    #14
        0x109,
        (
            "#1065F#6PYou're right.\x02\x03",

            "#1063FHmm... I wonder...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1117")

    ChrTalk(    #15
        0x110,
        "#263F#6P(Thought so.)\x02",
    )

    CloseMessageWindow()

    label("loc_1117")

    OP_A2(0x2B0C)
    OP_71(0x1001, 0x0)
    ExitThread()
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_4_E74 end

    def Function_5_1128(): pass

    label("Function_5_1128")

    Call(0, 6)
    Call(0, 11)
    Return()

    # Function_5_1128 end

    def Function_6_1131(): pass

    label("Function_6_1131")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    LoadEffect(0x2, "monster\\msc1000.eff")
    OP_E0(238, 0x4C, 0x2)
    OP_E0(238, 0x4D, 0x3)
    OP_E0(239, 0x4E, 0x2)
    OP_E0(239, 0x4F, 0x3)
    OP_E0(240, 0x50, 0x2)
    OP_E0(240, 0x51, 0x3)
    OP_E0(241, 0x52, 0x2)
    OP_E0(241, 0x53, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32369, 15000, -1810, 315)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x109, 6510, 15000, 20470, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1211")
    SetChrPos(0xEF, 5580, 15000, 20600, 180)
    SetChrPos(0xF0, 6400, 15000, 21300, 180)
    SetChrPos(0xF1, 5840, 15000, 21310, 180)
    Jump("loc_1296")

    label("loc_1211")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1255")
    SetChrPos(0xF0, 5580, 15000, 20600, 180)
    SetChrPos(0xEF, 6400, 15000, 21300, 180)
    SetChrPos(0xF1, 5840, 15000, 21310, 180)
    Jump("loc_1296")

    label("loc_1255")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1296")
    SetChrPos(0xF1, 5580, 15000, 20600, 180)
    SetChrPos(0xEF, 6400, 15000, 21300, 180)
    SetChrPos(0xF0, 5840, 15000, 21310, 180)

    label("loc_1296")

    OP_6D(7150, 15400, 16600, 0)
    OP_67(0, 5280, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(45000, 0)
    OP_6E(309, 0)
    OP_72(0x1002, 0x0)
    ExitThread()
    OP_6F(0x2, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x2, 0)
    OP_70(0x2, 0x1E)
    OP_73(0x2)

    def lambda_1301():
        OP_8F(0xFE, 0x19F0, 0x3A98, 0x37FA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1301)
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1387")

    def lambda_132F():
        OP_8F(0xFE, 0x13EC, 0x3A98, 0x382C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_132F)
    Sleep(230)

    def lambda_134F():
        OP_8F(0xFE, 0x1B08, 0x3A98, 0x3E58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_134F)
    Sleep(300)

    def lambda_136F():
        OP_8F(0xFE, 0x150E, 0x3A98, 0x3F3E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_136F)
    Jump("loc_145C")

    label("loc_1387")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F3")

    def lambda_139B():
        OP_8F(0xFE, 0x13EC, 0x3A98, 0x382C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_139B)
    Sleep(230)

    def lambda_13BB():
        OP_8F(0xFE, 0x1B08, 0x3A98, 0x3E58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_13BB)
    Sleep(300)

    def lambda_13DB():
        OP_8F(0xFE, 0x150E, 0x3A98, 0x3F3E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_13DB)
    Jump("loc_145C")

    label("loc_13F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_145C")

    def lambda_1407():
        OP_8F(0xFE, 0x13EC, 0x3A98, 0x382C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1407)
    Sleep(230)

    def lambda_1427():
        OP_8F(0xFE, 0x1B08, 0x3A98, 0x3E58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1427)
    Sleep(300)

    def lambda_1447():
        OP_8F(0xFE, 0x150E, 0x3A98, 0x3F3E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1447)

    label("loc_145C")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    NpcTalk(    #16
        0x10,
        "Female Voice",
        "#3PYou certainly took your time.\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F1")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1558")

    label("loc_14F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1519")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1558")

    label("loc_1519")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1541")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1558")

    label("loc_1541")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1558")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1585")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_15EC")

    label("loc_1585")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15AD")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_15EC")

    label("loc_15AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D5")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_15EC")

    label("loc_15D5")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_15EC")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1619")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1680")

    label("loc_1619")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1641")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1680")

    label("loc_1641")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1669")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1680")

    label("loc_1669")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1680")

    Sleep(1000)

    def lambda_168B():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_168B)
    Sleep(50)

    def lambda_169E():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_169E)
    Sleep(50)

    def lambda_16B1():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_16B1)
    Sleep(50)
    OP_8C(0xF0, 135, 400)
    Fade(1000)
    OP_6D(29020, 15000, -560, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2190, 0)
    OP_6C(179000, 0)
    OP_6E(418, 0)

    def lambda_170D():
        OP_6D(32000, 15000, -2860, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_170D)

    def lambda_1725():
        OP_67(0, 5660, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1725)

    def lambda_173D():
        OP_6B(1850, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_173D)

    def lambda_174D():
        OP_6E(411, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_174D)
    WaitChrThread(0x109, 0x0)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17C3")

    ChrTalk(    #17
        0x10A,
        "#1317F#1PUh-oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x108,
        "#075F#1P*sigh* I hit the nail on the head this time.\x02",
    )

    CloseMessageWindow()
    Jump("loc_17FB")

    label("loc_17C3")


    ChrTalk(    #19
        0x10A,
        "#1317F#1PUh-oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x109,
        "#1063F#1PI knew it was you.\x02",
    )

    CloseMessageWindow()

    label("loc_17FB")

    Sleep(300)
    Fade(1000)
    OP_6D(28910, 15000, 590, 0)
    OP_67(0, 5580, -10000, 0)
    OP_6B(2220, 0)
    OP_6C(179000, 0)
    OP_6E(400, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C63")
    SetChrPos(0x109, 21520, 15000, 10120, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18E6")
    SetChrPos(0xEF, 22090, 15000, 7690, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18B3")
    SetChrPos(0xF0, 20070, 15000, 9160, 135)
    SetChrPos(0xF1, 19250, 15000, 10970, 135)
    Jump("loc_18E3")

    label("loc_18B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18E3")
    SetChrPos(0xF1, 20070, 15000, 9160, 135)
    SetChrPos(0xF0, 19250, 15000, 10970, 135)

    label("loc_18E3")

    Jump("loc_19ED")

    label("loc_18E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_196B")
    SetChrPos(0xF0, 22090, 15000, 7690, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1938")
    SetChrPos(0xEF, 20070, 15000, 9160, 135)
    SetChrPos(0xF1, 19250, 15000, 10970, 135)
    Jump("loc_1968")

    label("loc_1938")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1968")
    SetChrPos(0xF1, 20070, 15000, 9160, 135)
    SetChrPos(0xEF, 19250, 15000, 10970, 135)

    label("loc_1968")

    Jump("loc_19ED")

    label("loc_196B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19ED")
    SetChrPos(0xF1, 22090, 15000, 7690, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19BD")
    SetChrPos(0xEF, 20070, 15000, 9160, 135)
    SetChrPos(0xF0, 19250, 15000, 10970, 135)
    Jump("loc_19ED")

    label("loc_19BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19ED")
    SetChrPos(0xF0, 20070, 15000, 9160, 135)
    SetChrPos(0xEF, 19250, 15000, 10970, 135)

    label("loc_19ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ABF")

    def lambda_1A01():
        OP_8F(0xFE, 0x6A7C, 0x3A98, 0xFF0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1A01)

    def lambda_1A1C():
        OP_8F(0xFE, 0x6AC2, 0x3A98, 0x15FE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1A1C)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A78")

    def lambda_1A45():
        OP_8F(0xFE, 0x654A, 0x3A98, 0xFAA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1A45)

    def lambda_1A60():
        OP_8F(0xFE, 0x6518, 0x3A98, 0x1752, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1A60)
    Jump("loc_1ABC")

    label("loc_1A78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ABC")

    def lambda_1A8C():
        OP_8F(0xFE, 0x654A, 0x3A98, 0xFAA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1A8C)

    def lambda_1AA7():
        OP_8F(0xFE, 0x6518, 0x3A98, 0x1752, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1AA7)

    label("loc_1ABC")

    Jump("loc_1C60")

    label("loc_1ABF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B91")

    def lambda_1AD3():
        OP_8F(0xFE, 0x6A7C, 0x3A98, 0xFF0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1AD3)

    def lambda_1AEE():
        OP_8F(0xFE, 0x6AC2, 0x3A98, 0x15FE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1AEE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B4A")

    def lambda_1B17():
        OP_8F(0xFE, 0x654A, 0x3A98, 0xFAA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1B17)

    def lambda_1B32():
        OP_8F(0xFE, 0x6518, 0x3A98, 0x1752, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1B32)
    Jump("loc_1B8E")

    label("loc_1B4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B8E")

    def lambda_1B5E():
        OP_8F(0xFE, 0x654A, 0x3A98, 0xFAA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1B5E)

    def lambda_1B79():
        OP_8F(0xFE, 0x6518, 0x3A98, 0x1752, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1B79)

    label("loc_1B8E")

    Jump("loc_1C60")

    label("loc_1B91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C60")

    def lambda_1BA5():
        OP_8F(0xFE, 0x6A7C, 0x3A98, 0xFF0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1BA5)

    def lambda_1BC0():
        OP_8F(0xFE, 0x6AC2, 0x3A98, 0x15FE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1BC0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C1C")

    def lambda_1BE9():
        OP_8F(0xFE, 0x654A, 0x3A98, 0xFAA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1BE9)

    def lambda_1C04():
        OP_8F(0xFE, 0x6518, 0x3A98, 0x1752, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1C04)
    Jump("loc_1C60")

    label("loc_1C1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C60")

    def lambda_1C30():
        OP_8F(0xFE, 0x654A, 0x3A98, 0xFAA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1C30)

    def lambda_1C4B():
        OP_8F(0xFE, 0x6518, 0x3A98, 0x1752, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1C4B)

    label("loc_1C60")

    Jump("loc_1E80")

    label("loc_1C63")

    SetChrPos(0x109, 22200, 15000, 9050, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CB8")
    SetChrPos(0xEF, 20590, 15000, 8730, 135)
    SetChrPos(0xF0, 20580, 15000, 11460, 135)
    SetChrPos(0xF1, 19070, 15000, 10770, 135)
    Jump("loc_1D3D")

    label("loc_1CB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CFC")
    SetChrPos(0xF0, 20590, 15000, 8730, 135)
    SetChrPos(0xEF, 20580, 15000, 11460, 135)
    SetChrPos(0xF1, 19070, 15000, 10770, 135)
    Jump("loc_1D3D")

    label("loc_1CFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D3D")
    SetChrPos(0xF1, 20590, 15000, 8730, 135)
    SetChrPos(0xEF, 20580, 15000, 11460, 135)
    SetChrPos(0xF0, 19070, 15000, 10770, 135)

    label("loc_1D3D")


    def lambda_1D43():
        OP_8F(0xFE, 0x6BC6, 0x3A98, 0x1068, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1D43)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DBF")

    def lambda_1D71():
        OP_8F(0xFE, 0x6784, 0x3A98, 0xCBC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1D71)

    def lambda_1D8C():
        OP_8F(0xFE, 0x68D8, 0x3A98, 0x15EA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1D8C)

    def lambda_1DA7():
        OP_8F(0xFE, 0x637E, 0x3A98, 0x113A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1DA7)
    Jump("loc_1E80")

    label("loc_1DBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E21")

    def lambda_1DD3():
        OP_8F(0xFE, 0x6784, 0x3A98, 0xCBC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1DD3)

    def lambda_1DEE():
        OP_8F(0xFE, 0x68D8, 0x3A98, 0x15EA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1DEE)

    def lambda_1E09():
        OP_8F(0xFE, 0x637E, 0x3A98, 0x113A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1E09)
    Jump("loc_1E80")

    label("loc_1E21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E80")

    def lambda_1E35():
        OP_8F(0xFE, 0x6784, 0x3A98, 0xCBC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1E35)

    def lambda_1E50():
        OP_8F(0xFE, 0x68D8, 0x3A98, 0x15EA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1E50)

    def lambda_1E6B():
        OP_8F(0xFE, 0x637E, 0x3A98, 0x113A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1E6B)

    label("loc_1E80")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_252B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FAA")

    ChrTalk(    #21
        0x10,
        (
            "#792F#5PLeaving that oaf over there aside for the time\x01",
            "being...\x02\x03",

            "#791FI'm happy to see you two again, Estelle, Anelace.\x02\x03",

            "I hope you've been doing well since I left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10A,
        "#819F#12PA-Ahaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1025F#12PIt's great seeing you, Kilika.\x02",
    )

    CloseMessageWindow()
    Jump("loc_23A1")

    label("loc_1FAA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20B4")

    ChrTalk(    #24
        0x10,
        (
            "#792F#5PLeaving that oaf over there aside for the time\x01",
            "being...\x02\x03",

            "#791FIt's good to see you again, Anelace, Joshua.\x02\x03",

            "I hope you've been doing well since I left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10A,
        "#819F#12PA-Ahaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        "#1501F#12P...It's good to see you again, too, Kilika.\x02",
    )

    CloseMessageWindow()
    Jump("loc_23A1")

    label("loc_20B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21B4")

    ChrTalk(    #27
        0x10,
        (
            "#792F#5PLeaving that oaf over there aside for the time\x01",
            "being...\x02\x03",

            "#791FIt's good to see you again, Anelace, Scherazard.\x02\x03",

            "I hope you've been doing well since I left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10A,
        "#819F#12PA-Ahaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x103,
        "#1534F#12P*sigh* Does nothing faze you?\x02",
    )

    CloseMessageWindow()
    Jump("loc_23A1")

    label("loc_21B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22DB")

    ChrTalk(    #30
        0x10,
        (
            "#792F#5PLeaving that oaf over there aside for the\x01",
            "time being...\x02\x03",

            "#791FIt's good to see you again, Anelace, Agate.\x02\x03",

            "I hope you've been doing well since I left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10A,
        "#819F#12PA-Ahaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x106,
        (
            "#051F#12PTypical Kilika--you get copied into a strange\x01",
            "world and barely bat an eye.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23A1")

    label("loc_22DB")


    ChrTalk(    #33
        0x10,
        (
            "#792F#5PLeaving that oaf over there aside for\x01",
            "the time being...\x02\x03",

            "#791FIt's good to see you again, Anelace.\x02\x03",

            "I hope you've been doing well since I left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10A,
        "#819F#12PA-Ahaha... I have. Thanks.\x02",
    )

    CloseMessageWindow()

    label("loc_23A1")

    OP_62(0x108, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #35
        0x108,
        (
            "#075F#6PDamn. Talk about harsh.\x01",
            "#072FI've got a name, you know.\x02\x03",

            "Can you not spare a word of greeting for me, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10,
        (
            "#792F#5PI see you all the time in Calvard as it is. It hasn't\x01",
            "even been that long since we last met.\x02\x03",

            "#791FOr were you hoping this would be a moving reunion \x01",
            "where I dived into your arms with tears in my eyes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x108,
        "#071F#6PI-I'm good, thanks.\x02",
    )

    CloseMessageWindow()
    Jump("loc_27B7")

    label("loc_252B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_272C")

    ChrTalk(    #38
        0x10,
        (
            "#792F#5PIt's good to be reunited with so many bracers\x01",
            "from Liberl in one place.\x02\x03",

            "#791FI hope you've been doing well since I left for\x01",
            "the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10A,
        "#819F#12PA-Ahaha...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2643")

    ChrTalk(    #40
        0x101,
        "#1025F#12PWe sure have. Thanks...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2729")

    label("loc_2643")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2684")

    ChrTalk(    #41
        0x102,
        "#1501F#12PIt's good to see you again, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2729")

    label("loc_2684")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26C2")

    ChrTalk(    #42
        0x103,
        "#1534F#12P*sigh* Does nothing faze you?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2729")

    label("loc_26C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2729")

    ChrTalk(    #43
        0x106,
        (
            "#051F#12PTypical Kilika. You get copied into a strange\x01",
            "world and barely bat an eye.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2729")

    Jump("loc_27B7")

    label("loc_272C")


    ChrTalk(    #44
        0x10,
        (
            "#792F#5PIt's good to see you again, Anelace.\x02\x03",

            "#791FI hope you've been doing well since I left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10A,
        "#819F#12PA-Ahaha... Yeah, thanks.\x02",
    )

    CloseMessageWindow()

    label("loc_27B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2861")

    ChrTalk(    #46
        0x10,
        (
            "#790F#5PI wasn't expecting to see you here,\x01",
            "though, Tita.\x02\x03",

            "#792FYour mother must be very worried about\x01",
            "you right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x107,
        "#067F#12PAhaha... Probably.\x02",
    )

    CloseMessageWindow()

    label("loc_2861")

    Sleep(500)

    ChrTalk(    #48
        0x10,
        (
            "#792F#5PNow, right down to business, Kevin.\x02\x03",

            "#790FI take it you understand the situation without\x01",
            "me needing to explain it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x109,
        (
            "#1065F#6PI think so. I assume you're the second guardian,\x01",
            "Phillip being the first.\x02\x03",

            "#1063FWe'll need to defeat you in order to advance to\x01",
            "the next area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10,
        (
            "#791F#5PCorrect.\x02\x03",

            "#792FI can't say I'm that fond of having to fight in\x01",
            "an old Ouroboros base of all things.\x02\x03",

            "#794FOh, well. I suppose it will have to do this time.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0x1F5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A90")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2AF7")

    label("loc_2A90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AB8")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2AF7")

    label("loc_2AB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE0")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2AF7")

    label("loc_2AE0")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2AF7")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B24")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2B8B")

    label("loc_2B24")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B4C")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2B8B")

    label("loc_2B4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B74")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2B8B")

    label("loc_2B74")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2B8B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BB8")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2C1F")

    label("loc_2BB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BE0")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2C1F")

    label("loc_2BE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C08")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2C1F")

    label("loc_2C08")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2C1F")

    Sleep(1000)

    ChrTalk(    #51
        0x10A,
        "#812F#12PThose are chakrams!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x109,
        (
            "#1069F#6PWatch out, guys! Those are really deadly as \x01",
            "throwing weapons!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E4F")

    ChrTalk(    #53
        0x10,
        (
            "#792F#5PIt's been a few years since we last had the joy\x01",
            "of battling one another, Zin.\x02\x03",

            "#791FI've no intention of holding back this time--\x01",
            "which means I'll be using my chakrams against\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x108,
        (
            "#070F#6PI wouldn't have it any other way.\x02\x03",

            "#074FWith one of those, you were stronger than even\x01",
            "Walter, so I'd love to see how I fare against you\x01",
            "these days.\x02\x03",

            "#072FShow us all what the Flying Swallow can do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        "#791F#5PGladly.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E93")

    label("loc_2E4F")


    ChrTalk(    #56
        0x10,
        (
            "#792F#5PThey can be used as more than simple\x01",
            "throwing weapons.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E93")

    Sleep(300)
    OP_20(0x7D0)
    Fade(1000)
    OP_6D(33720, 15000, -3050, 0)
    OP_67(0, 5490, -10000, 0)
    OP_6B(3360, 0)
    OP_6C(135000, 0)
    OP_6E(256, 0)

    def lambda_2EE5():
        OP_6B(3100, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2EE5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_309D")
    SetChrPos(0x109, 26690, 15000, 5320, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F93")
    SetChrPos(0xEF, 26610, 15000, 3880, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F60")
    SetChrPos(0xF0, 24890, 15000, 3890, 135)
    SetChrPos(0xF1, 25320, 15000, 5060, 135)
    Jump("loc_2F90")

    label("loc_2F60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F90")
    SetChrPos(0xF1, 24890, 15000, 3890, 135)
    SetChrPos(0xF0, 25320, 15000, 5060, 135)

    label("loc_2F90")

    Jump("loc_309A")

    label("loc_2F93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3018")
    SetChrPos(0xF0, 26610, 15000, 3880, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FE5")
    SetChrPos(0xEF, 24890, 15000, 3890, 135)
    SetChrPos(0xF1, 25320, 15000, 5060, 135)
    Jump("loc_3015")

    label("loc_2FE5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3015")
    SetChrPos(0xF1, 24890, 15000, 3890, 135)
    SetChrPos(0xEF, 25320, 15000, 5060, 135)

    label("loc_3015")

    Jump("loc_309A")

    label("loc_3018")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_309A")
    SetChrPos(0xF1, 26610, 15000, 3880, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_306A")
    SetChrPos(0xEF, 24890, 15000, 3890, 135)
    SetChrPos(0xF0, 25320, 15000, 5060, 135)
    Jump("loc_309A")

    label("loc_306A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_309A")
    SetChrPos(0xF0, 24890, 15000, 3890, 135)
    SetChrPos(0xEF, 25320, 15000, 5060, 135)

    label("loc_309A")

    Jump("loc_3177")

    label("loc_309D")

    SetChrPos(0x109, 27460, 15000, 3770, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30F2")
    SetChrPos(0xEF, 26580, 15000, 2950, 135)
    SetChrPos(0xF0, 26300, 15000, 5560, 135)
    SetChrPos(0xF1, 24600, 15000, 4260, 135)
    Jump("loc_3177")

    label("loc_30F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3136")
    SetChrPos(0xF0, 26580, 15000, 2950, 135)
    SetChrPos(0xEF, 26300, 15000, 5560, 135)
    SetChrPos(0xF1, 24600, 15000, 4260, 135)
    Jump("loc_3177")

    label("loc_3136")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3177")
    SetChrPos(0xF1, 26580, 15000, 2950, 135)
    SetChrPos(0xEF, 26300, 15000, 5560, 135)
    SetChrPos(0xF0, 24600, 15000, 4260, 135)

    label("loc_3177")

    SetChrChipByIndex(0x10, 5)

    def lambda_3182():

        label("loc_3182")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_3182")

    QueueWorkItem2(0x10, 3, lambda_3182)
    PlayEffect(0x2, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_0D()
    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, 34710, 15100, -1380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 31880, 15100, -4130, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    WaitChrThread(0x109, 0x2)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, 34710, 12000, -1380, 315)
    SetChrPos(0x12, 31880, 12000, -4130, 315)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_22(0x85, 0x1, 0x64)

    def lambda_3296():

        label("loc_3296")

        OP_7C(0x32, 0x32, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_3296")

    QueueWorkItem2(0x109, 3, lambda_3296)
    OP_43(0x11, 0x0, 0x0, 0x9)
    OP_43(0x12, 0x0, 0x0, 0xA)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    OP_23(0x85)
    OP_44(0x109, 0x3)
    OP_82(0x0, 0x2)
    OP_44(0x10, 0x3)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)

    def lambda_32E1():
        OP_6D(31020, 14900, -430, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_32E1)

    def lambda_32F9():
        OP_67(0, 5030, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_32F9)

    def lambda_3311():
        OP_6B(3610, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_3311)

    def lambda_3321():
        OP_6C(135000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_3321)

    def lambda_3331():
        OP_6E(256, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3331)
    WaitChrThread(0xEE, 0x0)
    OP_1D(0x99)
    Sleep(500)

    ChrTalk(    #57
        0x10,
        (
            "#792F#5PAs the second guardian...\x02\x03",

            "#790F...I, Kilika Rouran, master-level student of the \x01",
            "Taito school, will serve as your opponent.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEE, 12)
    SetChrSubChip(0xEE, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 14)
    SetChrSubChip(0xEF, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 16)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 18)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3458")

    ChrTalk(    #58
        0x101,
        "#1005F#5PBring it on!\x02",
    )

    CloseMessageWindow()
    Jump("loc_34AC")

    label("loc_3458")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3483")

    ChrTalk(    #59
        0x106,
        "#054F#5PBring it on!\x02",
    )

    CloseMessageWindow()
    Jump("loc_34AC")

    label("loc_3483")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34AC")

    ChrTalk(    #60
        0x103,
        "#1524F#5PBring it on!\x02",
    )

    CloseMessageWindow()

    label("loc_34AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34D3")

    ChrTalk(    #61
        0x107,
        "#065F#5PK-Kilika...\x02",
    )

    CloseMessageWindow()

    label("loc_34D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_351E")

    ChrTalk(    #62
        0x110,
        "#1306F#5PI'm curious to see how you match up to Walter!\x02",
    )

    CloseMessageWindow()

    label("loc_351E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_356A")

    ChrTalk(    #63
        0x10B,
        "#216F#5PTh-This seems like it's gonna be a real doozy...\x02",
    )

    CloseMessageWindow()

    label("loc_356A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35A8")

    ChrTalk(    #64
        0x10F,
        "#1443F#5PShe'll be quite a formidable foe.\x02",
    )

    CloseMessageWindow()

    label("loc_35A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35F3")

    ChrTalk(    #65
        0x102,
        "#1506F#5PI'd be happy to test my skills against you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3690")

    label("loc_35F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_363E")

    ChrTalk(    #66
        0x105,
        "#1162F#5PI'd be happy to test my skills against you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3690")

    label("loc_363E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3690")

    ChrTalk(    #67
        0x104,
        "#1540F#5PIt would be a pleasure to test my skills against you!\x02",
    )

    CloseMessageWindow()

    label("loc_3690")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36BD")

    ChrTalk(    #68
        0x10E,
        "#177F#5PThen let's begin!\x02",
    )

    CloseMessageWindow()

    label("loc_36BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36E1")

    ChrTalk(    #69
        0x10C,
        "#114F#5PTo arms!\x02",
    )

    CloseMessageWindow()

    label("loc_36E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3717")

    ChrTalk(    #70
        0x10D,
        "#271F#5PLet's see what you've got!\x02",
    )

    CloseMessageWindow()

    label("loc_3717")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3744")

    ChrTalk(    #71
        0x108,
        "#076F#5PLet's do this!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3761")

    label("loc_3744")


    ChrTalk(    #72
        0x109,
        "#1069F#5PLet's do this!\x02",
    )

    CloseMessageWindow()

    label("loc_3761")


    ChrTalk(    #73
        0x10A,
        "#815F#5PI'll give this all I've got!\x02",
    )

    CloseMessageWindow()

    def lambda_3791():
        OP_6D(30040, 15000, 390, 220)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_3791)

    def lambda_37A9():
        OP_67(0, 5690, -10000, 220)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_37A9)

    def lambda_37C1():
        OP_6B(3130, 220)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_37C1)

    def lambda_37D1():
        OP_6E(224, 220)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_37D1)
    SetChrChipByIndex(0x10, 2)

    def lambda_37E6():
        OP_8F(0xFE, 0x7080, 0x3A98, 0x5DC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_37E6)
    Sleep(30)

    def lambda_3806():
        OP_91(0xFE, 0x1F40, 0x0, 0xFFFFE0C0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3806)

    def lambda_3821():
        OP_91(0xFE, 0x1F40, 0x0, 0xFFFFE0C0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_3821)

    def lambda_383C():
        OP_91(0xFE, 0x1F40, 0x0, 0xFFFFE0C0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_383C)

    def lambda_3857():
        OP_91(0xFE, 0x1F40, 0x0, 0xFFFFE0C0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_3857)
    Sleep(30)

    def lambda_3877():
        OP_8E(0xFE, 0x7468, 0x3A98, 0x730, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3877)
    Sleep(30)

    def lambda_3897():
        OP_8E(0xFE, 0x6F2C, 0x3A98, 0x1D6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3897)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x2A5, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_6_1131 end

    def Function_7_38CE(): pass

    label("Function_7_38CE")

    SetChrFlags(0xFE, 0x800)
    OP_82(0x1, 0x0)
    OP_22(0x99, 0x0, 0x64)

    def lambda_38E1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_38E1)

    def lambda_38F3():

        label("loc_38F3")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_38F3")

    QueueWorkItem2(0xFE, 3, lambda_38F3)
    PlayEffect(0x1, 0x4, 0xFF, 34410, 17000, -1400, -58, 90, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_393B():
        OP_96(0xFE, 0x7F12, 0x3A98, 0xFFFFFFE2, 0xC8, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_393B)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x4)
    OP_22(0x193, 0x0, 0x64)
    Return()

    # Function_7_38CE end

    def Function_8_3968(): pass

    label("Function_8_3968")

    SetChrFlags(0xFE, 0x800)
    OP_82(0x2, 0x0)
    OP_22(0x99, 0x0, 0x64)

    def lambda_397B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_397B)

    def lambda_398D():

        label("loc_398D")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_398D")

    QueueWorkItem2(0xFE, 3, lambda_398D)
    PlayEffect(0x1, 0x5, 0xFF, 32170, 17000, -3770, -58, 90, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_39D5():
        OP_96(0xFE, 0x7774, 0x3A98, 0xFFFFF74A, 0xC8, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39D5)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x4)
    OP_22(0x193, 0x0, 0x64)
    Return()

    # Function_8_3968 end

    def Function_9_3A02(): pass

    label("Function_9_3A02")

    OP_51(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3A13():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A13)

    def lambda_3A25():

        label("loc_3A25")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_3A25")

    QueueWorkItem2(0xFE, 3, lambda_3A25)
    PlayEffect(0x1, 0x4, 0xFF, 34710, 15100, -1380, 0, 0, 0, 1000, 1300, 1000, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    SetChrFlags(0xFE, 0x800)
    OP_82(0x1, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    OP_22(0x193, 0x0, 0x64)
    Return()

    # Function_9_3A02 end

    def Function_10_3A91(): pass

    label("Function_10_3A91")

    Sleep(50)
    OP_51(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3AA7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3AA7)

    def lambda_3AB9():

        label("loc_3AB9")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_3AB9")

    QueueWorkItem2(0xFE, 3, lambda_3AB9)
    PlayEffect(0x1, 0x5, 0xFF, 31880, 15100, -4130, 0, 0, 0, 1000, 1300, 1000, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    SetChrFlags(0xFE, 0x800)
    OP_82(0x2, 0x2)
    OP_82(0x5, 0x2)
    ClearChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x4)
    OP_22(0x193, 0x0, 0x64)
    Return()

    # Function_10_3A91 end

    def Function_11_3B2A(): pass

    label("Function_11_3B2A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x3)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x3)
    OP_44(0xEE, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32369, 15000, -1810, 315)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 3)
    LoadEffect(0x0, "map\\mp259_02.eff")
    LoadEffect(0x1, "map\\mp256_00.eff")
    OP_22(0x146, 0x1, 0x3C)
    PlayEffect(0x0, 0x0, 0x10, 0, 600, 100, 0, 0, 0, 2200, 2400, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D96")
    SetChrPos(0x109, 29740, 15000, 2690, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C8C")
    SetChrPos(0xEF, 29750, 15000, 960, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C59")
    SetChrPos(0xF0, 28470, 15000, 1060, 135)
    SetChrPos(0xF1, 28360, 15000, 2600, 135)
    Jump("loc_3C89")

    label("loc_3C59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C89")
    SetChrPos(0xF1, 28470, 15000, 1060, 135)
    SetChrPos(0xF0, 28360, 15000, 2600, 135)

    label("loc_3C89")

    Jump("loc_3D93")

    label("loc_3C8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D11")
    SetChrPos(0xF0, 29750, 15000, 960, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CDE")
    SetChrPos(0xEF, 28470, 15000, 1060, 135)
    SetChrPos(0xF1, 28360, 15000, 2600, 135)
    Jump("loc_3D0E")

    label("loc_3CDE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D0E")
    SetChrPos(0xF1, 28470, 15000, 1060, 135)
    SetChrPos(0xEF, 28360, 15000, 2600, 135)

    label("loc_3D0E")

    Jump("loc_3D93")

    label("loc_3D11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D93")
    SetChrPos(0xF1, 29750, 15000, 960, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D63")
    SetChrPos(0xEF, 28470, 15000, 1060, 135)
    SetChrPos(0xF0, 28360, 15000, 2600, 135)
    Jump("loc_3D93")

    label("loc_3D63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D93")
    SetChrPos(0xF0, 28470, 15000, 1060, 135)
    SetChrPos(0xEF, 28360, 15000, 2600, 135)

    label("loc_3D93")

    Jump("loc_3E70")

    label("loc_3D96")

    SetChrPos(0x109, 30710, 15000, 1530, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DEB")
    SetChrPos(0xEF, 29660, 15000, 540, 135)
    SetChrPos(0xF0, 29900, 15000, 3020, 135)
    SetChrPos(0xF1, 28620, 15000, 1700, 135)
    Jump("loc_3E70")

    label("loc_3DEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E2F")
    SetChrPos(0xF0, 29660, 15000, 540, 135)
    SetChrPos(0xEF, 29900, 15000, 3020, 135)
    SetChrPos(0xF1, 28620, 15000, 1700, 135)
    Jump("loc_3E70")

    label("loc_3E2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E70")
    SetChrPos(0xF1, 29660, 15000, 540, 135)
    SetChrPos(0xEF, 29900, 15000, 3020, 135)
    SetChrPos(0xF0, 28620, 15000, 1700, 135)

    label("loc_3E70")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    OP_6D(30790, 15000, -1150, 0)
    OP_67(0, 5370, -10000, 0)
    OP_6B(2009, 0)
    OP_6C(179000, 0)
    OP_6E(416, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42A9")

    ChrTalk(    #74
        0x10,
        (
            "#792F#5PWhew... I should have known that wouldn't go\x01",
            "quite like our fights always used to.\x02\x03",

            "#794FYou've refined your skills beautifully over the\x01",
            "years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x108,
        (
            "#573F#6PI could say the same to you...\x02\x03",

            "#070FIt's hard to believe you were spending the time\x01",
            "serving as a guild receptionist instead of doing\x01",
            "some kind of intensive training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x10,
        (
            "#792F#5PThere's no need to flatter me. My skills still\x01",
            "need plenty of refining if I want to reach the\x01",
            "heights of the Taito school.\x02\x03",

            "#791FBut if my real self remembers this defeat, \x01",
            "I'm quite sure she's going to be frustrated\x01",
            "enough to want to get back to training.\x02\x03",

            "...Be certain you're ready to serve as her\x01",
            "opponent when she does, Zin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x108,
        (
            "#075F#6PYou got it.\x02\x03",

            "Although if you ask me, I think you're strong\x01",
            "enough as you are...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x10A,
        "#812F#12PY-You're tellin' me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x109,
        (
            "#1068F#6PI'd be scared outta my wits to fight you again\x01",
            "if you ever reached 'the heights of the Taito\x01",
            "school,' personally.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4436")

    label("loc_42A9")


    ChrTalk(    #80
        0x10,
        (
            "#792F#5POh, dear... I see taking a break on my training\x01",
            "has finally caught up with me.\x02\x03",

            "#794FI thought I was sure to win if I didn't hold back,\x01",
            "but I've overestimated my own abilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10A,
        (
            "#819F#12PI-I wouldn't be so sure of that... You really gave\x01",
            "us one crazy fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x109,
        (
            "#1068F#6PIf this is what you're like after a break,\x01",
            "I dread to think what kind of a monster\x01",
            "you were at your peak...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4436")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4492")

    ChrTalk(    #83
        0x101,
        (
            "#1007F#12PTh-That was some kinda learning experience,\x01",
            "if nothing else...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4492")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44D5")

    ChrTalk(    #84
        0x106,
        "#551F#12PD-Damn. You really are unbelievable...\x02",
    )

    CloseMessageWindow()

    label("loc_44D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4525")

    ChrTalk(    #85
        0x103,
        (
            "#1534F#12PYou were every bit as tough as I figured\x01",
            "you'd be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4525")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4555")

    ChrTalk(    #86
        0x107,
        "#066F#12PThat was amazing...\x02",
    )

    CloseMessageWindow()

    label("loc_4555")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_459B")

    ChrTalk(    #87
        0x10B,
        "#413F#12PWh-What was up with those crazy dragons?!\x02",
    )

    CloseMessageWindow()

    label("loc_459B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45FF")

    ChrTalk(    #88
        0x104,
        (
            "#1544F#12PPerhaps it was for the best that I never\x01",
            "seriously tried to woo her...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4661")

    ChrTalk(    #89
        0x10E,
        (
            "#176F#12PI'm astounded by how well you were able\x01",
            "to use your chi in battle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46C0")

    label("loc_4661")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46C0")

    ChrTalk(    #90
        0x10C,
        (
            "#115F#12PI'm astounded by how well you were able\x01",
            "to use your chi in battle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46FA")

    ChrTalk(    #91
        0x10F,
        "#1806F#12PYou fought spectacularly.\x02",
    )

    CloseMessageWindow()
    Jump("loc_477B")

    label("loc_46FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_473C")

    ChrTalk(    #92
        0x102,
        "#1514F#12PYou fought spectacularly, Kilika.\x02",
    )

    CloseMessageWindow()
    Jump("loc_477B")

    label("loc_473C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_477B")

    ChrTalk(    #93
        0x105,
        "#1382F#12PYou fought spectacularly, Kilika.\x02",
    )

    CloseMessageWindow()

    label("loc_477B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47F7")

    ChrTalk(    #94
        0x110,
        (
            "#1305F#12PI see there are more formidable warriors out\x01",
            "there that I didn't know about than I thought.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_483A")

    label("loc_47F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_483A")

    ChrTalk(    #95
        0x10D,
        "#278F#12PThe world really is full of surprises.\x02",
    )

    CloseMessageWindow()

    label("loc_483A")


    ChrTalk(    #96
        0x10,
        (
            "#792F#5PWell...the time to say our goodbyes has come.\x02\x03",

            "#791FWith my defeat, you're now halfway through\x01",
            "the trials of this sixth plane.\x02\x03",

            "Just be sure not to let your guards down.\x01",
            "I'm sure the greatest challenges are very\x01",
            "much still to come.\x02\x03",

            "#792FFarewell. Let us meet again one day.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x138, 0x0, 0x64)

    def lambda_496A():
        OP_6B(3000, 7000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_496A)
    PlayEffect(0x1, 0x1, 0x10, -100, -700, 0, 0, 0, 0, 1900, 1900, 1900, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_23(0x146)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_44(0x10, 0x3)

    def lambda_49C5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_49C5)
    Sleep(800)
    Fade(1000)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_0D()
    SetChrFlags(0x10, 0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/M4112   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_3B2A end

    def Function_12_49FF(): pass

    label("Function_12_49FF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BB9")
    SetChrPos(0x109, 30780, 15000, 1680, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AAF")
    SetChrPos(0xEF, 30820, 15000, 10, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A7C")
    SetChrPos(0xF0, 29340, 15000, -50, 135)
    SetChrPos(0xF1, 29440, 15000, 2090, 135)
    Jump("loc_4AAC")

    label("loc_4A7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AAC")
    SetChrPos(0xF1, 29340, 15000, -50, 135)
    SetChrPos(0xF0, 29440, 15000, 2090, 135)

    label("loc_4AAC")

    Jump("loc_4BB6")

    label("loc_4AAF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B34")
    SetChrPos(0xF0, 30820, 15000, 10, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B01")
    SetChrPos(0xEF, 29340, 15000, -50, 135)
    SetChrPos(0xF1, 29440, 15000, 2090, 135)
    Jump("loc_4B31")

    label("loc_4B01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B31")
    SetChrPos(0xF1, 29340, 15000, -50, 135)
    SetChrPos(0xEF, 29440, 15000, 2090, 135)

    label("loc_4B31")

    Jump("loc_4BB6")

    label("loc_4B34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BB6")
    SetChrPos(0xF1, 30820, 15000, 10, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B86")
    SetChrPos(0xEF, 29340, 15000, -50, 135)
    SetChrPos(0xF0, 29440, 15000, 2090, 135)
    Jump("loc_4BB6")

    label("loc_4B86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BB6")
    SetChrPos(0xF0, 29340, 15000, -50, 135)
    SetChrPos(0xEF, 29440, 15000, 2090, 135)

    label("loc_4BB6")

    Jump("loc_4C93")

    label("loc_4BB9")

    SetChrPos(0x109, 30850, 15000, 1020, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C0E")
    SetChrPos(0xEF, 29650, 15000, 270, 135)
    SetChrPos(0xF0, 29890, 15000, 2560, 135)
    SetChrPos(0xF1, 28620, 15000, 1560, 135)
    Jump("loc_4C93")

    label("loc_4C0E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C52")
    SetChrPos(0xF0, 29650, 15000, 270, 135)
    SetChrPos(0xEF, 29890, 15000, 2560, 135)
    SetChrPos(0xF1, 28620, 15000, 1560, 135)
    Jump("loc_4C93")

    label("loc_4C52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C93")
    SetChrPos(0xF1, 29650, 15000, 270, 135)
    SetChrPos(0xEF, 29890, 15000, 2560, 135)
    SetChrPos(0xF0, 28620, 15000, 1560, 135)

    label("loc_4C93")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(29850, 15000, -1090, 0)
    OP_67(0, 5120, -10000, 0)
    OP_6B(2060, 0)
    OP_6C(179000, 0)
    OP_6E(396, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D4F")

    ChrTalk(    #97
        0x108,
        "#075F#5PMan... She's never been one to hold back.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DF6")

    label("loc_4D4F")


    ChrTalk(    #98
        0x10A,
        (
            "#1316F#5PWhew... She's just as merciless a fighter as\x01",
            "she is a guild receptionist.\x02\x03",

            "#1314FThat was my first time fighting her, but I can\x01",
            "only hope it's the last.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DF6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E4C")

    ChrTalk(    #99
        0x101,
        (
            "#1008F#6PIt's hard to believe that wasn't even\x01",
            "the real Kilika.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F92")

    label("loc_4E4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EA2")

    ChrTalk(    #100
        0x103,
        (
            "#1534F#6PIt's hard to believe that wasn't even\x01",
            "the real Kilika.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F92")

    label("loc_4EA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EF7")

    ChrTalk(    #101
        0x106,
        (
            "#556F#6PIt's hard to believe that wasn't even\x01",
            "the real Kilika.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F92")

    label("loc_4EF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F4D")

    ChrTalk(    #102
        0x109,
        (
            "#1066F#6PIt's hard to believe that wasn't even\x01",
            "the real Kilika.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F92")

    label("loc_4F4D")


    ChrTalk(    #103
        0x109,
        (
            "#1066F#5PIt's hard to believe that wasn't even\x01",
            "the real Kilika.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50FE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5010")

    def lambda_4FB4():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4FB4)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FE0")

    def lambda_4FD5():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_4FD5)
    Jump("loc_4FFC")

    label("loc_4FE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FFC")

    def lambda_4FF4():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_4FF4)

    label("loc_4FFC")

    Sleep(100)
    OP_8C(0xEF, 293, 400)
    Sleep(300)
    Jump("loc_50FB")

    label("loc_5010")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5080")

    def lambda_5024():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5024)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5050")

    def lambda_5045():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_5045)
    Jump("loc_506C")

    label("loc_5050")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_506C")

    def lambda_5064():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_5064)

    label("loc_506C")

    Sleep(100)
    OP_8C(0xF0, 293, 400)
    Sleep(300)
    Jump("loc_50FB")

    label("loc_5080")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50FB")

    def lambda_5094():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5094)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50C0")

    def lambda_50B5():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_50B5)
    Jump("loc_50DC")

    label("loc_50C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50DC")

    def lambda_50D4():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_50D4)

    label("loc_50DC")


    def lambda_50E2():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_50E2)
    Sleep(100)
    OP_8C(0xF1, 293, 400)
    Sleep(300)

    label("loc_50FB")

    Jump("loc_511D")

    label("loc_50FE")


    def lambda_5104():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5104)
    Sleep(100)
    OP_8C(0x10A, 0, 400)
    Sleep(300)

    label("loc_511D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51E1")

    ChrTalk(    #104
        0x109,
        (
            "#1075F#6PAnyway, we should be able to enter the next\x01",
            "area now.\x02\x03",

            "#1840FI don't know about you guys, but I'm exhausted.\x01",
            "What say we go back to the garden before we\x01",
            "keep going?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5294")

    label("loc_51E1")


    ChrTalk(    #105
        0x109,
        (
            "#1075F#5PAnyway, we should be able to enter the next\x01",
            "area now.\x02\x03",

            "#1840FI don't know about you guys, but I'm exhausted.\x01",
            "What say we go back to the garden before we\x01",
            "keep going?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5294")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52D0")

    ChrTalk(    #106
        0x10F,
        "#1447F#6PWith pleasure. I'm starving.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5586")

    label("loc_52D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52F9")

    ChrTalk(    #107
        0x10B,
        "#210F#6PMe, too...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5586")

    label("loc_52F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5324")

    ChrTalk(    #108
        0x105,
        "#1160F#6PUnderstood.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5586")

    label("loc_5324")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_536E")

    ChrTalk(    #109
        0x10E,
        "#170F#6PI think that's the wisest course of action.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5586")

    label("loc_536E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_539C")

    ChrTalk(    #110
        0x104,
        "#1540F#6PI quite agree.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5586")

    label("loc_539C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53C6")

    ChrTalk(    #111
        0x10D,
        "#277F#6PUnderstood.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5586")

    label("loc_53C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53FC")

    ChrTalk(    #112
        0x10C,
        "#110F#6PThat sounds wise to me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5586")

    label("loc_53FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5434")

    ChrTalk(    #113
        0x102,
        "#1500F#6PThat sounds like a plan.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5586")

    label("loc_5434")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_546E")

    ChrTalk(    #114
        0x110,
        "#261F#6PI think that's a good idea.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5586")

    label("loc_546E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5497")

    ChrTalk(    #115
        0x107,
        "#560F#6PMe, too...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5586")

    label("loc_5497")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54CF")

    ChrTalk(    #116
        0x106,
        "#051F#6PSounds like a plan to me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5586")

    label("loc_54CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5515")

    ChrTalk(    #117
        0x103,
        "#1520F#6PThat sounds like the best thing to do.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5586")

    label("loc_5515")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5553")

    ChrTalk(    #118
        0x101,
        "#1025F#6PYeah... I'm pretty tired, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5586")

    label("loc_5553")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5586")

    ChrTalk(    #119
        0x108,
        "#070F#6PThat sounds good to me.\x02",
    )

    CloseMessageWindow()

    label("loc_5586")

    OP_A2(0x2B15)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_559A")
    OP_A2(0x2641)

    label("loc_559A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55AB")
    OP_A2(0x2642)

    label("loc_55AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55BC")
    OP_A2(0x2643)

    label("loc_55BC")

    OP_28(0x39, 0x4, 0x4)
    OP_28(0x39, 0x4, 0x8)
    OP_28(0x39, 0x1, 0x1)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_12_49FF end

    def Function_13_55D4(): pass

    label("Function_13_55D4")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(15560, 10, -2580, 0)
    OP_67(0, 8100, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(17000, 0)
    OP_6E(262, 0)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1E)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x0)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M5610   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_55D4 end

    def Function_14_567B(): pass

    label("Function_14_567B")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(15560, 10, -2580, 0)
    OP_67(0, 8100, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(17000, 0)
    OP_6E(262, 0)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 30)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_6F(0x0, 30)
    OP_70(0x0, 0x0)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x0)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M5610   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_567B end

    def Function_15_5722(): pass

    label("Function_15_5722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5733")
    Call(0, 3)
    Return()

    label("loc_5733")

    OP_DE(0x0, 0x4, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 7130, -6000, -27730, 90)
    SetChrPos(0x1, 6350, -6000, -28630, 90)
    SetChrPos(0x2, 6190, -6000, -26980, 90)
    SetChrPos(0x3, 5290, -6000, -27840, 90)
    OP_69(0x0, 0x0)
    OP_6C(315000, 0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 17)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xFD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_15_5722 end

    def Function_16_58B9(): pass

    label("Function_16_58B9")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 7130, -6000, -27730, 270)
    SetChrPos(0x2, 6350, -6000, -28630, 270)
    SetChrPos(0x1, 6190, -6000, -26980, 270)
    SetChrPos(0x0, 5290, -6000, -27840, 270)
    OP_69(0x0, 0x0)
    OP_6C(315000, 0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 18)
    NewScene("ED6_DT21/M4111   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_16_58B9 end

    def Function_17_5A1D(): pass

    label("Function_17_5A1D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A46")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_5A3A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5A3A)

    label("loc_5A46")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A6F")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_5A63():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5A63)

    label("loc_5A6F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A98")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_5A8C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_5A8C)

    label("loc_5A98")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AC1")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_5AB5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_5AB5)

    label("loc_5AC1")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AED")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_5AED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B04")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_5B04")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B1B")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_5B1B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B32")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_5B32")

    Return()

    # Function_17_5A1D end

    def Function_18_5B33(): pass

    label("Function_18_5B33")


    def lambda_5B39():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5B39)

    def lambda_5B4B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5B4B)

    def lambda_5B5D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_5B5D)

    def lambda_5B6F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_5B6F)
    Sleep(1000)
    Return()

    # Function_18_5B33 end

    def Function_19_5B81(): pass

    label("Function_19_5B81")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_19_5B81 end

    def Function_20_5B88(): pass

    label("Function_20_5B88")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #120
        "\x07\x05The doors are sealed shut.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_20_5B88 end

    SaveToFile()

Try(main)
