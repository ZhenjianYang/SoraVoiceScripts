from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '雾香',                                 # 9
        '阴影豹',                               # 10
        '阴影豹',                               # 11
        '',                                     # 12
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
        "Function_3_3E8",          # 03, 3
        "Function_4_E01",          # 04, 4
        "Function_5_10A4",         # 05, 5
        "Function_6_10AD",         # 06, 6
        "Function_7_361B",         # 07, 7
        "Function_8_36B5",         # 08, 8
        "Function_9_374F",         # 09, 9
        "Function_10_37DE",        # 0A, 10
        "Function_11_3877",        # 0B, 11
        "Function_12_43C3",        # 0C, 12
        "Function_13_4F12",        # 0D, 13
        "Function_14_4FB9",        # 0E, 14
        "Function_15_5060",        # 0F, 15
        "Function_16_51F7",        # 10, 16
        "Function_17_535B",        # 11, 17
        "Function_18_5471",        # 12, 18
        "Function_19_54BF",        # 13, 19
        "Function_20_54C6",        # 14, 20
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
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×１０００\x01",
            "\x07\x02#57I水之耀晶片×１０００\x01",
            "\x07\x02#58I火之耀晶片×１０００\x01",
            "\x07\x02#59I风之耀晶片×１０００\x01",
            "\x07\x02#62I时之耀晶片×１０００\x01",
            "\x07\x02#60I空之耀晶片×１０００\x01",
            "\x07\x02#61I幻之耀晶片×１０００\x07\x00\x02",
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

    def Function_3_3E8(): pass

    label("Function_3_3E8")

    OP_DE(0x0, 0x4, 0x1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 6350, -6000, -28630, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44D")
    SetChrPos(0xEF, 7130, -6000, -27730, 90)
    SetChrPos(0xF0, 6190, -6000, -26980, 90)
    SetChrPos(0xF1, 5290, -6000, -27840, 90)
    Jump("loc_4D2")

    label("loc_44D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_491")
    SetChrPos(0xF0, 7130, -6000, -27730, 90)
    SetChrPos(0xEF, 6190, -6000, -26980, 90)
    SetChrPos(0xF1, 5290, -6000, -27840, 90)
    Jump("loc_4D2")

    label("loc_491")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D2")
    SetChrPos(0xF1, 7130, -6000, -27730, 90)
    SetChrPos(0xEF, 6190, -6000, -26980, 90)
    SetChrPos(0xF0, 5290, -6000, -27840, 90)

    label("loc_4D2")

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

    def lambda_641():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_641)

    def lambda_653():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_653)

    def lambda_665():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_665)

    def lambda_677():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_677)
    Sleep(1500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CC")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_733")

    label("loc_6CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F4")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_733")

    label("loc_6F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71C")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_733")

    label("loc_71C")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_733")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_760")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7C7")

    label("loc_760")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_788")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7C7")

    label("loc_788")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B0")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7C7")

    label("loc_7B0")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_7C7")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F4")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_85B")

    label("loc_7F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81C")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_85B")

    label("loc_81C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_844")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_85B")

    label("loc_844")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_85B")

    Sleep(1000)

    ChrTalk(    #1
        0x10A,
        "#814F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1079F#5P哦……\x01",
            "难不成这里是……\x02",
        )
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

    def lambda_8FA():
        OP_6D(13980, 3870, 12100, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_8FA)

    def lambda_912():
        OP_67(0, 9730, -10000, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_912)

    def lambda_92A():
        OP_6B(10170, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_92A)

    def lambda_93A():
        OP_6C(21000, 7000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_93A)

    def lambda_94A():
        OP_6E(380, 7000)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_94A)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E5")

    def lambda_96D():
        OP_8F(0xFE, 0x32E6, 0xFFFFE89A, 0xFFFF9610, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_96D)
    Sleep(300)

    def lambda_98D():
        OP_8F(0xFE, 0x34D0, 0xFFFFE8E0, 0xFFFF90A2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_98D)
    Sleep(300)

    def lambda_9AD():
        OP_8F(0xFE, 0x2BB6, 0xFFFFE8CC, 0xFFFF920A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_9AD)
    Sleep(300)

    def lambda_9CD():
        OP_8F(0xFE, 0x2D6E, 0xFFFFE8FE, 0xFFFF8CF6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_9CD)
    Jump("loc_AFA")

    label("loc_9E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A71")

    def lambda_9F9():
        OP_8F(0xFE, 0x32E6, 0xFFFFE89A, 0xFFFF9610, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_9F9)
    Sleep(300)

    def lambda_A19():
        OP_8F(0xFE, 0x34D0, 0xFFFFE8E0, 0xFFFF90A2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A19)
    Sleep(300)

    def lambda_A39():
        OP_8F(0xFE, 0x2BB6, 0xFFFFE8CC, 0xFFFF920A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_A39)
    Sleep(300)

    def lambda_A59():
        OP_8F(0xFE, 0x2D6E, 0xFFFFE8FE, 0xFFFF8CF6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_A59)
    Jump("loc_AFA")

    label("loc_A71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFA")

    def lambda_A85():
        OP_8F(0xFE, 0x32E6, 0xFFFFE89A, 0xFFFF9610, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_A85)
    Sleep(300)

    def lambda_AA5():
        OP_8F(0xFE, 0x34D0, 0xFFFFE8E0, 0xFFFF90A2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AA5)
    Sleep(300)

    def lambda_AC5():
        OP_8F(0xFE, 0x2BB6, 0xFFFFE8CC, 0xFFFF920A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_AC5)
    Sleep(300)

    def lambda_AE5():
        OP_8F(0xFE, 0x2D6E, 0xFFFFE8FE, 0xFFFF8CF6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_AE5)

    label("loc_AFA")

    OP_C8(0x200, 0x46, "C_PLAC35._CH", 0x0, 0x3E8)
    WaitChrThread(0xEE, 0x0)

    def lambda_B1A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_B1A)
    WaitChrThread(0xEF, 0x0)

    def lambda_B2D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_B2D)
    WaitChrThread(0xF0, 0x0)

    def lambda_B40():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_B40)
    WaitChrThread(0xF1, 0x0)

    def lambda_B53():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_B53)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C3C")

    ChrTalk(    #3
        0x101,
        (
            "#1002F#6P这里……\x01",
            "是湖畔的研究所……对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        (
            "#1063F#6P嗯，\x01",
            "是『噬身之蛇』暂时作为据点的设施。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C9A")

    label("loc_C3C")


    ChrTalk(    #5
        0x109,
        (
            "#1065F#6P湖畔的研究所……\x02\x03",

            "#1063F好像是『噬身之蛇』暂时\x01",
            "作为据点的设施啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD6")

    ChrTalk(    #6
        0x10F,
        "#1443F#6P这里就是报告书中说的……\x02",
    )

    CloseMessageWindow()

    label("loc_CD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D19")

    ChrTalk(    #7
        0x102,
        (
            "#1502F#6P……是教授设置了\x01",
            "陷阱的地方吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D19")


    ChrTalk(    #8
        0x10A,
        (
            "#812F#5P呃，嗯……\x01",
            "我想没错。\x02\x03",

            "#813F不过真奇怪呢……\x01",
            "好像有哪里不对劲……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DB0")

    ChrTalk(    #9
        0x110,
        "#1305F#6P（………嗯……………）\x02",
    )

    CloseMessageWindow()

    label("loc_DB0")


    ChrTalk(    #10
        0x109,
        (
            "#1063F#6P……唔。\x01",
            "总之先在设施周围\x01",
            "调查一遍看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B0A)
    OP_28(0x38, 0x1, 0x4)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_3_3E8 end

    def Function_4_E01(): pass

    label("Function_4_E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 4)), scpexpr(EXPR_END)), "loc_E09")
    Return()

    label("loc_E09")

    EventBegin(0x0)
    Fade(500)
    OP_6D(38130, -40, 10900, 0)
    OP_67(0, 6210, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(314000, 0)
    OP_6E(276, 0)
    SetChrPos(0x109, 39130, -40, 9220, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA2")
    SetChrPos(0xEF, 39560, -50, 10470, 270)
    SetChrPos(0xF0, 40800, -70, 8790, 270)
    SetChrPos(0xF1, 40980, -70, 10390, 270)
    Jump("loc_F27")

    label("loc_EA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE6")
    SetChrPos(0xF0, 39560, -50, 10470, 270)
    SetChrPos(0xEF, 40800, -70, 8790, 270)
    SetChrPos(0xF1, 40980, -70, 10390, 270)
    Jump("loc_F27")

    label("loc_EE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F27")
    SetChrPos(0xF1, 39560, -50, 10470, 270)
    SetChrPos(0xEF, 40800, -70, 8790, 270)
    SetChrPos(0xF0, 40980, -70, 10390, 270)

    label("loc_F27")

    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FC7")

    ChrTalk(    #11
        0x101,
        (
            "#1020F#6P等、等一下……\x02\x03",

            "这个研究所的后门\x01",
            "不是在左手边的吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10A,
        (
            "#1317F#6P呃，嗯……\x01",
            "记得确实应该是这样的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101D")

    label("loc_FC7")


    ChrTalk(    #13
        0x10A,
        (
            "#1317F#6P咦、咦……！？\x02\x03",

            "这个研究所的后门\x01",
            "原来好像是在左手边的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_101D")


    ChrTalk(    #14
        0x109,
        (
            "#1065F#6P嗯……不会错。\x02\x03",

            "#1063F这难道是……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1093")

    ChrTalk(    #15
        0x110,
        "#263F#6P（……原来如此啊。）\x02",
    )

    CloseMessageWindow()

    label("loc_1093")

    OP_A2(0x2B0C)
    OP_71(0x1001, 0x0)
    ExitThread()
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_4_E01 end

    def Function_5_10A4(): pass

    label("Function_5_10A4")

    Call(0, 6)
    Call(0, 11)
    Return()

    # Function_5_10A4 end

    def Function_6_10AD(): pass

    label("Function_6_10AD")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118D")
    SetChrPos(0xEF, 5580, 15000, 20600, 180)
    SetChrPos(0xF0, 6400, 15000, 21300, 180)
    SetChrPos(0xF1, 5840, 15000, 21310, 180)
    Jump("loc_1212")

    label("loc_118D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D1")
    SetChrPos(0xF0, 5580, 15000, 20600, 180)
    SetChrPos(0xEF, 6400, 15000, 21300, 180)
    SetChrPos(0xF1, 5840, 15000, 21310, 180)
    Jump("loc_1212")

    label("loc_11D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1212")
    SetChrPos(0xF1, 5580, 15000, 20600, 180)
    SetChrPos(0xEF, 6400, 15000, 21300, 180)
    SetChrPos(0xF0, 5840, 15000, 21310, 180)

    label("loc_1212")

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

    def lambda_127D():
        OP_8F(0xFE, 0x19F0, 0x3A98, 0x37FA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_127D)
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1303")

    def lambda_12AB():
        OP_8F(0xFE, 0x13EC, 0x3A98, 0x382C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_12AB)
    Sleep(230)

    def lambda_12CB():
        OP_8F(0xFE, 0x1B08, 0x3A98, 0x3E58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_12CB)
    Sleep(300)

    def lambda_12EB():
        OP_8F(0xFE, 0x150E, 0x3A98, 0x3F3E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_12EB)
    Jump("loc_13D8")

    label("loc_1303")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_136F")

    def lambda_1317():
        OP_8F(0xFE, 0x13EC, 0x3A98, 0x382C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1317)
    Sleep(230)

    def lambda_1337():
        OP_8F(0xFE, 0x1B08, 0x3A98, 0x3E58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1337)
    Sleep(300)

    def lambda_1357():
        OP_8F(0xFE, 0x150E, 0x3A98, 0x3F3E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1357)
    Jump("loc_13D8")

    label("loc_136F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13D8")

    def lambda_1383():
        OP_8F(0xFE, 0x13EC, 0x3A98, 0x382C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1383)
    Sleep(230)

    def lambda_13A3():
        OP_8F(0xFE, 0x1B08, 0x3A98, 0x3E58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_13A3)
    Sleep(300)

    def lambda_13C3():
        OP_8F(0xFE, 0x150E, 0x3A98, 0x3F3E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_13C3)

    label("loc_13D8")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    NpcTalk(    #16
        0x10,
        "女性的声音",
        "#3P……真晚啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1461")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_14C8")

    label("loc_1461")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1489")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_14C8")

    label("loc_1489")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B1")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_14C8")

    label("loc_14B1")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_14C8")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F5")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_155C")

    label("loc_14F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_151D")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_155C")

    label("loc_151D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1545")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_155C")

    label("loc_1545")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_155C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1589")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_15F0")

    label("loc_1589")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B1")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_15F0")

    label("loc_15B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D9")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_15F0")

    label("loc_15D9")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_15F0")

    Sleep(1000)

    def lambda_15FB():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_15FB)
    Sleep(50)

    def lambda_160E():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_160E)
    Sleep(50)

    def lambda_1621():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1621)
    Sleep(50)
    OP_8C(0xF0, 135, 400)
    Fade(1000)
    OP_6D(29020, 15000, -560, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2190, 0)
    OP_6C(179000, 0)
    OP_6E(418, 0)

    def lambda_167D():
        OP_6D(32000, 15000, -2860, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_167D)

    def lambda_1695():
        OP_67(0, 5660, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1695)

    def lambda_16AD():
        OP_6B(1850, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_16AD)

    def lambda_16BD():
        OP_6E(411, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_16BD)
    WaitChrThread(0x109, 0x0)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1732")

    ChrTalk(    #17
        0x10A,
        "#1317F#1P哎、哎呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x108,
        (
            "#075F#1P……唉。\x01",
            "果然不出所料啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_177C")

    label("loc_1732")


    ChrTalk(    #19
        0x10A,
        "#1317F#1P哎、哎呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x109,
        "#1063F#1P果然不出所料吗……\x02",
    )

    CloseMessageWindow()

    label("loc_177C")

    Sleep(300)
    Fade(1000)
    OP_6D(28910, 15000, 590, 0)
    OP_67(0, 5580, -10000, 0)
    OP_6B(2220, 0)
    OP_6C(179000, 0)
    OP_6E(400, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BE4")
    SetChrPos(0x109, 21520, 15000, 10120, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1867")
    SetChrPos(0xEF, 22090, 15000, 7690, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1834")
    SetChrPos(0xF0, 20070, 15000, 9160, 135)
    SetChrPos(0xF1, 19250, 15000, 10970, 135)
    Jump("loc_1864")

    label("loc_1834")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1864")
    SetChrPos(0xF1, 20070, 15000, 9160, 135)
    SetChrPos(0xF0, 19250, 15000, 10970, 135)

    label("loc_1864")

    Jump("loc_196E")

    label("loc_1867")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18EC")
    SetChrPos(0xF0, 22090, 15000, 7690, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18B9")
    SetChrPos(0xEF, 20070, 15000, 9160, 135)
    SetChrPos(0xF1, 19250, 15000, 10970, 135)
    Jump("loc_18E9")

    label("loc_18B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18E9")
    SetChrPos(0xF1, 20070, 15000, 9160, 135)
    SetChrPos(0xEF, 19250, 15000, 10970, 135)

    label("loc_18E9")

    Jump("loc_196E")

    label("loc_18EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_196E")
    SetChrPos(0xF1, 22090, 15000, 7690, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_193E")
    SetChrPos(0xEF, 20070, 15000, 9160, 135)
    SetChrPos(0xF0, 19250, 15000, 10970, 135)
    Jump("loc_196E")

    label("loc_193E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_196E")
    SetChrPos(0xF0, 20070, 15000, 9160, 135)
    SetChrPos(0xEF, 19250, 15000, 10970, 135)

    label("loc_196E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A40")

    def lambda_1982():
        OP_8F(0xFE, 0x6A7C, 0x3A98, 0xFF0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1982)

    def lambda_199D():
        OP_8F(0xFE, 0x6AC2, 0x3A98, 0x15FE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_199D)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19F9")

    def lambda_19C6():
        OP_8F(0xFE, 0x654A, 0x3A98, 0xFAA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_19C6)

    def lambda_19E1():
        OP_8F(0xFE, 0x6518, 0x3A98, 0x1752, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_19E1)
    Jump("loc_1A3D")

    label("loc_19F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A3D")

    def lambda_1A0D():
        OP_8F(0xFE, 0x654A, 0x3A98, 0xFAA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1A0D)

    def lambda_1A28():
        OP_8F(0xFE, 0x6518, 0x3A98, 0x1752, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1A28)

    label("loc_1A3D")

    Jump("loc_1BE1")

    label("loc_1A40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B12")

    def lambda_1A54():
        OP_8F(0xFE, 0x6A7C, 0x3A98, 0xFF0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1A54)

    def lambda_1A6F():
        OP_8F(0xFE, 0x6AC2, 0x3A98, 0x15FE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1A6F)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ACB")

    def lambda_1A98():
        OP_8F(0xFE, 0x654A, 0x3A98, 0xFAA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1A98)

    def lambda_1AB3():
        OP_8F(0xFE, 0x6518, 0x3A98, 0x1752, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1AB3)
    Jump("loc_1B0F")

    label("loc_1ACB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B0F")

    def lambda_1ADF():
        OP_8F(0xFE, 0x654A, 0x3A98, 0xFAA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1ADF)

    def lambda_1AFA():
        OP_8F(0xFE, 0x6518, 0x3A98, 0x1752, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1AFA)

    label("loc_1B0F")

    Jump("loc_1BE1")

    label("loc_1B12")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BE1")

    def lambda_1B26():
        OP_8F(0xFE, 0x6A7C, 0x3A98, 0xFF0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1B26)

    def lambda_1B41():
        OP_8F(0xFE, 0x6AC2, 0x3A98, 0x15FE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1B41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B9D")

    def lambda_1B6A():
        OP_8F(0xFE, 0x654A, 0x3A98, 0xFAA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1B6A)

    def lambda_1B85():
        OP_8F(0xFE, 0x6518, 0x3A98, 0x1752, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1B85)
    Jump("loc_1BE1")

    label("loc_1B9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BE1")

    def lambda_1BB1():
        OP_8F(0xFE, 0x654A, 0x3A98, 0xFAA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1BB1)

    def lambda_1BCC():
        OP_8F(0xFE, 0x6518, 0x3A98, 0x1752, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1BCC)

    label("loc_1BE1")

    Jump("loc_1E01")

    label("loc_1BE4")

    SetChrPos(0x109, 22200, 15000, 9050, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C39")
    SetChrPos(0xEF, 20590, 15000, 8730, 135)
    SetChrPos(0xF0, 20580, 15000, 11460, 135)
    SetChrPos(0xF1, 19070, 15000, 10770, 135)
    Jump("loc_1CBE")

    label("loc_1C39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C7D")
    SetChrPos(0xF0, 20590, 15000, 8730, 135)
    SetChrPos(0xEF, 20580, 15000, 11460, 135)
    SetChrPos(0xF1, 19070, 15000, 10770, 135)
    Jump("loc_1CBE")

    label("loc_1C7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CBE")
    SetChrPos(0xF1, 20590, 15000, 8730, 135)
    SetChrPos(0xEF, 20580, 15000, 11460, 135)
    SetChrPos(0xF0, 19070, 15000, 10770, 135)

    label("loc_1CBE")


    def lambda_1CC4():
        OP_8F(0xFE, 0x6BC6, 0x3A98, 0x1068, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1CC4)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D40")

    def lambda_1CF2():
        OP_8F(0xFE, 0x6784, 0x3A98, 0xCBC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1CF2)

    def lambda_1D0D():
        OP_8F(0xFE, 0x68D8, 0x3A98, 0x15EA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1D0D)

    def lambda_1D28():
        OP_8F(0xFE, 0x637E, 0x3A98, 0x113A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1D28)
    Jump("loc_1E01")

    label("loc_1D40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DA2")

    def lambda_1D54():
        OP_8F(0xFE, 0x6784, 0x3A98, 0xCBC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1D54)

    def lambda_1D6F():
        OP_8F(0xFE, 0x68D8, 0x3A98, 0x15EA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1D6F)

    def lambda_1D8A():
        OP_8F(0xFE, 0x637E, 0x3A98, 0x113A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1D8A)
    Jump("loc_1E01")

    label("loc_1DA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E01")

    def lambda_1DB6():
        OP_8F(0xFE, 0x6784, 0x3A98, 0xCBC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1DB6)

    def lambda_1DD1():
        OP_8F(0xFE, 0x68D8, 0x3A98, 0x15EA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1DD1)

    def lambda_1DEC():
        OP_8F(0xFE, 0x637E, 0x3A98, 0x113A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1DEC)

    label("loc_1E01")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_239C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F0F")

    ChrTalk(    #21
        0x10,
        (
            "#792F#5P那边那个男人\x01",
            "暂且不理……\x02\x03",

            "#791F好久不见了。\x01",
            "艾丝蒂尔，还有亚妮拉丝。\x02\x03",

            "自从我回到共和国以后就没见过面了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10A,
        "#819F#12P啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1025F#12P雾香姐姐……\x02",
    )

    CloseMessageWindow()
    Jump("loc_22A1")

    label("loc_1F0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FF7")

    ChrTalk(    #24
        0x10,
        (
            "#792F#5P那边那个男人\x01",
            "暂且不理……\x02\x03",

            "#791F好久不见了。\x01",
            "亚妮拉丝，还有约修亚。\x02\x03",

            "自从我回到共和国以后就没见过面了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10A,
        "#819F#12P啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        "#1501F#12P……好久不见了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22A1")

    label("loc_1FF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20F0")

    ChrTalk(    #27
        0x10,
        (
            "#792F#5P那边那个男人\x01",
            "暂且不理……\x02\x03",

            "#791F好久不见了。\x01",
            "亚妮拉丝，还有雪拉扎德。\x02\x03",

            "自从我回到共和国以后就没见过面了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10A,
        "#819F#12P啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x103,
        (
            "#1534F#12P呵呵……\x01",
            "雾香小姐也是老样子呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22A1")

    label("loc_20F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21E2")

    ChrTalk(    #30
        0x10,
        (
            "#792F#5P那边那个男人\x01",
            "暂且不理……\x02\x03",

            "#791F好久不见了。\x01",
            "阿加特，还有亚妮拉丝。\x02\x03",

            "自从我回到共和国以后就没见过面了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10A,
        "#819F#12P啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x106,
        (
            "#051F#12P呵呵……\x01",
            "你还是那么冷静啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22A1")

    label("loc_21E2")


    ChrTalk(    #33
        0x10,
        (
            "#792F#5P那边那个男人\x01",
            "暂且不理……\x02\x03",

            "#791F好久不见了。\x01",
            "亚妮拉丝·艾尔菲德。\x02\x03",

            "自从我回到共和国以后就没见过面了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10A,
        (
            "#819F#12P啊、啊哈哈……\x01",
            "真是好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22A1")

    OP_62(0x108, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #35
        0x108,
        (
            "#075F#6P喂喂……\x01",
            "#072F不要暂且不理啊。\x02\x03",

            "对我也说一句如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10,
        (
            "#792F#5P反正和你在共和国\x01",
            "也经常碰面。\x02\x03",

            "#791F难道你感动得热泪盈眶，\x01",
            "想来个拥抱？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x108,
        (
            "#071F#6P不、不是……\x01",
            "这个就免了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D7")

    label("loc_239C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_253A")

    ChrTalk(    #38
        0x10,
        (
            "#792F#5P好久不见了。\x01",
            "利贝尔的游击士们。\x02\x03",

            "#791F自从我回到共和国以后就没见过面了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10A,
        "#819F#12P啊、啊哈哈……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2489")

    ChrTalk(    #40
        0x101,
        "#1025F#12P雾香姐姐……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2537")

    label("loc_2489")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C1")

    ChrTalk(    #41
        0x102,
        "#1501F#12P……好久不见了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2537")

    label("loc_24C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2500")

    ChrTalk(    #42
        0x103,
        (
            "#1534F#12P呵呵……\x01",
            "还是老样子呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2537")

    label("loc_2500")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2537")

    ChrTalk(    #43
        0x106,
        (
            "#051F#12P哼……\x01",
            "冷静的女人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2537")

    Jump("loc_25D7")

    label("loc_253A")


    ChrTalk(    #44
        0x10,
        (
            "#792F#5P好久不见了。\x01",
            "亚妮拉丝·艾尔菲德。\x02\x03",

            "#791F自从我回到共和国以后就没见过面了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10A,
        (
            "#819F#12P啊、啊哈哈……\x01",
            "真是好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2665")

    ChrTalk(    #46
        0x10,
        (
            "#790F#5P哎呀……\x01",
            "提妲也来了吗。\x02\x03",

            "#792F艾莉卡博士\x01",
            "也一定很担心吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x107,
        (
            "#067F#12P啊哈哈……\x01",
            "可能是吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2665")

    Sleep(500)

    ChrTalk(    #48
        0x10,
        (
            "#792F#5P那么……\x01",
            "您是凯文神父对吧。\x02\x03",

            "#790F既然来到这里，\x01",
            "应该已经清楚规则了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x109,
        (
            "#1065F#6P嗯，我想你应该就是\x01",
            "继管家先生之后的『守护者』……\x02\x03",

            "#1063F阻挡在通往下一个领域路上的\x01",
            "『敌人』对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10,
        (
            "#791F#5P呵呵，回答正确。\x02\x03",

            "#792F虽然在这种低级趣味的舞台上决一胜负\x01",
            "实在让人提不起劲……\x02\x03",

            "#794F唉，就做个了断吧。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2839")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_28A0")

    label("loc_2839")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2861")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_28A0")

    label("loc_2861")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2889")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_28A0")

    label("loc_2889")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_28A0")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28CD")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2934")

    label("loc_28CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28F5")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2934")

    label("loc_28F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_291D")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2934")

    label("loc_291D")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2934")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2961")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_29C8")

    label("loc_2961")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2989")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_29C8")

    label("loc_2989")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29B1")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_29C8")

    label("loc_29B1")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_29C8")

    Sleep(1000)

    ChrTalk(    #51
        0x10A,
        "#812F#12P『偃月轮』……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x109,
        (
            "#1069F#6P东方武术所使用的\x01",
            "左右一对的投掷道具吗……！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BAF")

    ChrTalk(    #53
        0x10,
        (
            "#792F#5P金……\x01",
            "好多年没和你\x01",
            "直接交手了吧。\x02\x03",

            "#791F不好意思，\x01",
            "我就不客气地使用自己擅长的武器了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x108,
        (
            "#070F#6P无所谓，反正原本\x01",
            "『泰斗流』就不是仅仅使用空手的流派啊。\x02\x03",

            "#074F只要有擅长的武器在手，\x01",
            "甚至能够凌驾门下第一天才瓦鲁特的\x01",
            "『飞燕红儿』的实力……\x02\x03",

            "#072F时隔多日再让我见识见识吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        (
            "#791F#5P呵呵……\x01",
            "如你所愿。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BEE")

    label("loc_2BAF")


    ChrTalk(    #56
        0x10,
        (
            "#792F#5P呵呵……\x01",
            "不过这个可不仅能\x01",
            "用作投掷武器啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BEE")

    Sleep(300)
    OP_20(0x7D0)
    Fade(1000)
    OP_6D(33720, 15000, -3050, 0)
    OP_67(0, 5490, -10000, 0)
    OP_6B(3360, 0)
    OP_6C(135000, 0)
    OP_6E(256, 0)

    def lambda_2C40():
        OP_6B(3100, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2C40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DF8")
    SetChrPos(0x109, 26690, 15000, 5320, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CEE")
    SetChrPos(0xEF, 26610, 15000, 3880, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CBB")
    SetChrPos(0xF0, 24890, 15000, 3890, 135)
    SetChrPos(0xF1, 25320, 15000, 5060, 135)
    Jump("loc_2CEB")

    label("loc_2CBB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CEB")
    SetChrPos(0xF1, 24890, 15000, 3890, 135)
    SetChrPos(0xF0, 25320, 15000, 5060, 135)

    label("loc_2CEB")

    Jump("loc_2DF5")

    label("loc_2CEE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D73")
    SetChrPos(0xF0, 26610, 15000, 3880, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D40")
    SetChrPos(0xEF, 24890, 15000, 3890, 135)
    SetChrPos(0xF1, 25320, 15000, 5060, 135)
    Jump("loc_2D70")

    label("loc_2D40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D70")
    SetChrPos(0xF1, 24890, 15000, 3890, 135)
    SetChrPos(0xEF, 25320, 15000, 5060, 135)

    label("loc_2D70")

    Jump("loc_2DF5")

    label("loc_2D73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DF5")
    SetChrPos(0xF1, 26610, 15000, 3880, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DC5")
    SetChrPos(0xEF, 24890, 15000, 3890, 135)
    SetChrPos(0xF0, 25320, 15000, 5060, 135)
    Jump("loc_2DF5")

    label("loc_2DC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DF5")
    SetChrPos(0xF0, 24890, 15000, 3890, 135)
    SetChrPos(0xEF, 25320, 15000, 5060, 135)

    label("loc_2DF5")

    Jump("loc_2ED2")

    label("loc_2DF8")

    SetChrPos(0x109, 27460, 15000, 3770, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E4D")
    SetChrPos(0xEF, 26580, 15000, 2950, 135)
    SetChrPos(0xF0, 26300, 15000, 5560, 135)
    SetChrPos(0xF1, 24600, 15000, 4260, 135)
    Jump("loc_2ED2")

    label("loc_2E4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E91")
    SetChrPos(0xF0, 26580, 15000, 2950, 135)
    SetChrPos(0xEF, 26300, 15000, 5560, 135)
    SetChrPos(0xF1, 24600, 15000, 4260, 135)
    Jump("loc_2ED2")

    label("loc_2E91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ED2")
    SetChrPos(0xF1, 26580, 15000, 2950, 135)
    SetChrPos(0xEF, 26300, 15000, 5560, 135)
    SetChrPos(0xF0, 24600, 15000, 4260, 135)

    label("loc_2ED2")

    SetChrChipByIndex(0x10, 5)

    def lambda_2EDD():

        label("loc_2EDD")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_2EDD")

    QueueWorkItem2(0x10, 3, lambda_2EDD)
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

    def lambda_2FF1():

        label("loc_2FF1")

        OP_7C(0x32, 0x32, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_2FF1")

    QueueWorkItem2(0x109, 3, lambda_2FF1)
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

    def lambda_303C():
        OP_6D(31020, 14900, -430, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_303C)

    def lambda_3054():
        OP_67(0, 5030, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_3054)

    def lambda_306C():
        OP_6B(3610, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_306C)

    def lambda_307C():
        OP_6C(135000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_307C)

    def lambda_308C():
        OP_6E(256, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_308C)
    WaitChrThread(0xEE, 0x0)
    OP_1D(0x99)
    Sleep(500)

    ChrTalk(    #57
        0x10,
        (
            "#792F#5P泰斗流弟子──\x01",
            "奥义传人雾香·楼兰。\x02\x03",

            "#790F身为第二『守护者』\x01",
            "担当你们的对手。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_319B")

    ChrTalk(    #58
        0x101,
        "#1005F#5P求之不得……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3203")

    label("loc_319B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31D1")

    ChrTalk(    #59
        0x106,
        "#054F#5P哦哦，求之不得！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3203")

    label("loc_31D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3203")

    ChrTalk(    #60
        0x103,
        "#1524F#5P求之不得……！\x02",
    )

    CloseMessageWindow()

    label("loc_3203")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3236")

    ChrTalk(    #61
        0x107,
        "#065F#5P雾、雾香姐姐……\x02",
    )

    CloseMessageWindow()

    label("loc_3236")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3275")

    ChrTalk(    #62
        0x110,
        (
            "#1306F#5P嘻嘻……\x01",
            "是瓦鲁特的同门呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3275")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32B3")

    ChrTalk(    #63
        0x10B,
        (
            "#216F#5P好、好像\x01",
            "不是一般的厉害……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32F4")

    ChrTalk(    #64
        0x10F,
        (
            "#1443F#5P……看来可不是\x01",
            "普通的对手呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3338")

    ChrTalk(    #65
        0x102,
        (
            "#1506F#5P那么……\x01",
            "受教了！\x02",
        )
    )

    Jump("loc_3334")

    label("loc_3334")

    CloseMessageWindow()
    Jump("loc_33B3")

    label("loc_3338")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_337C")

    ChrTalk(    #66
        0x105,
        (
            "#1162F#5P那么……\x01",
            "受教了！\x02",
        )
    )

    Jump("loc_3378")

    label("loc_3378")

    CloseMessageWindow()
    Jump("loc_33B3")

    label("loc_337C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33B3")

    ChrTalk(    #67
        0x104,
        (
            "#1540F#5P呼……\x01",
            "那就受教了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33EA")

    ChrTalk(    #68
        0x10E,
        "#177F#5P那就堂堂正正地……！\x02",
    )

    CloseMessageWindow()

    label("loc_33EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3417")

    ChrTalk(    #69
        0x10C,
        "#114F#5P上吧……！\x02",
    )

    CloseMessageWindow()

    label("loc_3417")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3444")

    ChrTalk(    #70
        0x10D,
        "#271F#5P上吧……！\x02",
    )

    CloseMessageWindow()

    label("loc_3444")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_347C")

    ChrTalk(    #71
        0x108,
        "#076F#5P一决胜负……雾香！\x02",
    )

    CloseMessageWindow()
    Jump("loc_34A8")

    label("loc_347C")


    ChrTalk(    #72
        0x109,
        "#1069F#5P一决胜负吧，雾香小姐！\x02",
    )

    CloseMessageWindow()

    label("loc_34A8")


    ChrTalk(    #73
        0x10A,
        (
            "#815F#5P……我会尽全力\x01",
            "向你挑战的！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_34DE():
        OP_6D(30040, 15000, 390, 220)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_34DE)

    def lambda_34F6():
        OP_67(0, 5690, -10000, 220)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_34F6)

    def lambda_350E():
        OP_6B(3130, 220)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_350E)

    def lambda_351E():
        OP_6E(224, 220)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_351E)
    SetChrChipByIndex(0x10, 2)

    def lambda_3533():
        OP_8F(0xFE, 0x7080, 0x3A98, 0x5DC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_3533)
    Sleep(30)

    def lambda_3553():
        OP_91(0xFE, 0x1F40, 0x0, 0xFFFFE0C0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3553)

    def lambda_356E():
        OP_91(0xFE, 0x1F40, 0x0, 0xFFFFE0C0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_356E)

    def lambda_3589():
        OP_91(0xFE, 0x1F40, 0x0, 0xFFFFE0C0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_3589)

    def lambda_35A4():
        OP_91(0xFE, 0x1F40, 0x0, 0xFFFFE0C0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_35A4)
    Sleep(30)

    def lambda_35C4():
        OP_8E(0xFE, 0x7468, 0x3A98, 0x730, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_35C4)
    Sleep(30)

    def lambda_35E4():
        OP_8E(0xFE, 0x6F2C, 0x3A98, 0x1D6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_35E4)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x2A5, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_6_10AD end

    def Function_7_361B(): pass

    label("Function_7_361B")

    SetChrFlags(0xFE, 0x800)
    OP_82(0x1, 0x0)
    OP_22(0x99, 0x0, 0x64)

    def lambda_362E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_362E)

    def lambda_3640():

        label("loc_3640")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_3640")

    QueueWorkItem2(0xFE, 3, lambda_3640)
    PlayEffect(0x1, 0x4, 0xFF, 34410, 17000, -1400, -58, 90, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_3688():
        OP_96(0xFE, 0x7F12, 0x3A98, 0xFFFFFFE2, 0xC8, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3688)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x4)
    OP_22(0x193, 0x0, 0x64)
    Return()

    # Function_7_361B end

    def Function_8_36B5(): pass

    label("Function_8_36B5")

    SetChrFlags(0xFE, 0x800)
    OP_82(0x2, 0x0)
    OP_22(0x99, 0x0, 0x64)

    def lambda_36C8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_36C8)

    def lambda_36DA():

        label("loc_36DA")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_36DA")

    QueueWorkItem2(0xFE, 3, lambda_36DA)
    PlayEffect(0x1, 0x5, 0xFF, 32170, 17000, -3770, -58, 90, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_3722():
        OP_96(0xFE, 0x7774, 0x3A98, 0xFFFFF74A, 0xC8, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3722)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x4)
    OP_22(0x193, 0x0, 0x64)
    Return()

    # Function_8_36B5 end

    def Function_9_374F(): pass

    label("Function_9_374F")

    OP_51(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3760():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3760)

    def lambda_3772():

        label("loc_3772")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_3772")

    QueueWorkItem2(0xFE, 3, lambda_3772)
    PlayEffect(0x1, 0x4, 0xFF, 34710, 15100, -1380, 0, 0, 0, 1000, 1300, 1000, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    SetChrFlags(0xFE, 0x800)
    OP_82(0x1, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    OP_22(0x193, 0x0, 0x64)
    Return()

    # Function_9_374F end

    def Function_10_37DE(): pass

    label("Function_10_37DE")

    Sleep(50)
    OP_51(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_37F4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_37F4)

    def lambda_3806():

        label("loc_3806")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_3806")

    QueueWorkItem2(0xFE, 3, lambda_3806)
    PlayEffect(0x1, 0x5, 0xFF, 31880, 15100, -4130, 0, 0, 0, 1000, 1300, 1000, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    SetChrFlags(0xFE, 0x800)
    OP_82(0x2, 0x2)
    OP_82(0x5, 0x2)
    ClearChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x4)
    OP_22(0x193, 0x0, 0x64)
    Return()

    # Function_10_37DE end

    def Function_11_3877(): pass

    label("Function_11_3877")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AE3")
    SetChrPos(0x109, 29740, 15000, 2690, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39D9")
    SetChrPos(0xEF, 29750, 15000, 960, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39A6")
    SetChrPos(0xF0, 28470, 15000, 1060, 135)
    SetChrPos(0xF1, 28360, 15000, 2600, 135)
    Jump("loc_39D6")

    label("loc_39A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39D6")
    SetChrPos(0xF1, 28470, 15000, 1060, 135)
    SetChrPos(0xF0, 28360, 15000, 2600, 135)

    label("loc_39D6")

    Jump("loc_3AE0")

    label("loc_39D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A5E")
    SetChrPos(0xF0, 29750, 15000, 960, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A2B")
    SetChrPos(0xEF, 28470, 15000, 1060, 135)
    SetChrPos(0xF1, 28360, 15000, 2600, 135)
    Jump("loc_3A5B")

    label("loc_3A2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A5B")
    SetChrPos(0xF1, 28470, 15000, 1060, 135)
    SetChrPos(0xEF, 28360, 15000, 2600, 135)

    label("loc_3A5B")

    Jump("loc_3AE0")

    label("loc_3A5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AE0")
    SetChrPos(0xF1, 29750, 15000, 960, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AB0")
    SetChrPos(0xEF, 28470, 15000, 1060, 135)
    SetChrPos(0xF0, 28360, 15000, 2600, 135)
    Jump("loc_3AE0")

    label("loc_3AB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AE0")
    SetChrPos(0xF0, 28470, 15000, 1060, 135)
    SetChrPos(0xEF, 28360, 15000, 2600, 135)

    label("loc_3AE0")

    Jump("loc_3BBD")

    label("loc_3AE3")

    SetChrPos(0x109, 30710, 15000, 1530, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B38")
    SetChrPos(0xEF, 29660, 15000, 540, 135)
    SetChrPos(0xF0, 29900, 15000, 3020, 135)
    SetChrPos(0xF1, 28620, 15000, 1700, 135)
    Jump("loc_3BBD")

    label("loc_3B38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B7C")
    SetChrPos(0xF0, 29660, 15000, 540, 135)
    SetChrPos(0xEF, 29900, 15000, 3020, 135)
    SetChrPos(0xF1, 28620, 15000, 1700, 135)
    Jump("loc_3BBD")

    label("loc_3B7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BBD")
    SetChrPos(0xF1, 29660, 15000, 540, 135)
    SetChrPos(0xEF, 29900, 15000, 3020, 135)
    SetChrPos(0xF0, 28620, 15000, 1700, 135)

    label("loc_3BBD")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E67")

    ChrTalk(    #74
        0x10,
        (
            "#792F#5P呼，\x01",
            "以前那一套果然行不通呢。\x02\x03",

            "#794F泰斗的『不动』……\x01",
            "相当了得的功夫啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x108,
        (
            "#573F#6P你也是……\x01",
            "技术比以前更精湛了啊。\x02\x03",

            "#070F完全不是只做协会接待\x01",
            "就能达到的水平啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x10,
        (
            "#792F#5P哪里……\x01",
            "我离极致还差得远。\x02\x03",

            "#791F如果真正的我能够体会到这种不甘心，\x01",
            "一定会再努力锻炼的。\x02\x03",

            "到时候，金。\x01",
            "再做我的对手吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x108,
        (
            "#075F#6P是是。\x02\x03",

            "真是的，\x01",
            "再强下去可怎么办啊……\x02",
        )
    )

    Jump("loc_3E02")

    label("loc_3E02")

    CloseMessageWindow()

    ChrTalk(    #78
        0x10A,
        "#812F#12P一、一点都没错啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x109,
        (
            "#1068F#6P还差得远……\x01",
            "到底要强到什么地步啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F42")

    label("loc_3E67")


    ChrTalk(    #80
        0x10,
        (
            "#792F#5P哎呀哎呀……\x01",
            "我也太疏于锻炼了。\x02\x03",

            "#794F如果是生死相搏的话，\x01",
            "我大概就很会危险了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10A,
        (
            "#819F#12P哎、哎呀～……\x01",
            "你已经很厉害啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x109,
        (
            "#1068F#6P这还叫疏于锻炼……\x01",
            "……真是怪物啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F7C")

    ChrTalk(    #83
        0x101,
        (
            "#1007F#12P真、真是\x01",
            "长见识了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FB8")

    ChrTalk(    #84
        0x106,
        "#551F#12P难、难以置信的女人啊……\x02",
    )

    CloseMessageWindow()

    label("loc_3FB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FF4")

    ChrTalk(    #85
        0x103,
        (
            "#1534F#12P哈哈……\x01",
            "正如我所料呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_402E")

    ChrTalk(    #86
        0x107,
        "#066F#12P厉、厉害，雾香姐姐……\x02",
    )

    CloseMessageWindow()

    label("loc_402E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4071")

    ChrTalk(    #87
        0x10B,
        (
            "#413F#12P呜呜……\x01",
            "那是什么啊，那条龙……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4071")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40B3")

    ChrTalk(    #88
        0x104,
        (
            "#1544F#12P哎呀哎呀……\x01",
            "还好没去搭讪她。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40FF")

    ChrTalk(    #89
        0x10E,
        (
            "#176F#12P没想到竟然能\x01",
            "将斗气操纵得这般自如……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4148")

    label("loc_40FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4148")

    ChrTalk(    #90
        0x10C,
        (
            "#115F#12P没想到竟然能\x01",
            "将斗气操纵得这般自如……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4148")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_417E")

    ChrTalk(    #91
        0x10F,
        "#1806F#12P……太精彩了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_41E7")

    label("loc_417E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41B4")

    ChrTalk(    #92
        0x102,
        "#1514F#12P……太精彩了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_41E7")

    label("loc_41B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41E7")

    ChrTalk(    #93
        0x105,
        "#1382F#12P……太精彩了。\x02",
    )

    CloseMessageWindow()

    label("loc_41E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_422E")

    ChrTalk(    #94
        0x110,
        (
            "#1305F#12P唔……\x01",
            "还是有很多厉害人物的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4264")

    label("loc_422E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4264")

    ChrTalk(    #95
        0x10D,
        "#278F#12P……世界真广阔啊。\x02",
    )

    CloseMessageWindow()

    label("loc_4264")


    ChrTalk(    #96
        0x10,
        (
            "#792F#5P好了……\x01",
            "差不多该分别了吧。\x02\x03",

            "#791F这『第六星层』\x01",
            "到此也算是中间点了。\x02\x03",

            "后面有更加艰难的试炼等着你们，\x01",
            "要做好觉悟哦。\x02\x03",

            "#792F那么……\x01",
            "后会有期吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x138, 0x0, 0x64)

    def lambda_432E():
        OP_6B(3000, 7000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_432E)
    PlayEffect(0x1, 0x1, 0x10, -100, -700, 0, 0, 0, 0, 1900, 1900, 1900, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_23(0x146)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_44(0x10, 0x3)

    def lambda_4389():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4389)
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

    # Function_11_3877 end

    def Function_12_43C3(): pass

    label("Function_12_43C3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_457D")
    SetChrPos(0x109, 30780, 15000, 1680, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4473")
    SetChrPos(0xEF, 30820, 15000, 10, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4440")
    SetChrPos(0xF0, 29340, 15000, -50, 135)
    SetChrPos(0xF1, 29440, 15000, 2090, 135)
    Jump("loc_4470")

    label("loc_4440")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4470")
    SetChrPos(0xF1, 29340, 15000, -50, 135)
    SetChrPos(0xF0, 29440, 15000, 2090, 135)

    label("loc_4470")

    Jump("loc_457A")

    label("loc_4473")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44F8")
    SetChrPos(0xF0, 30820, 15000, 10, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44C5")
    SetChrPos(0xEF, 29340, 15000, -50, 135)
    SetChrPos(0xF1, 29440, 15000, 2090, 135)
    Jump("loc_44F5")

    label("loc_44C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44F5")
    SetChrPos(0xF1, 29340, 15000, -50, 135)
    SetChrPos(0xEF, 29440, 15000, 2090, 135)

    label("loc_44F5")

    Jump("loc_457A")

    label("loc_44F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_457A")
    SetChrPos(0xF1, 30820, 15000, 10, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_454A")
    SetChrPos(0xEF, 29340, 15000, -50, 135)
    SetChrPos(0xF0, 29440, 15000, 2090, 135)
    Jump("loc_457A")

    label("loc_454A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_457A")
    SetChrPos(0xF0, 29340, 15000, -50, 135)
    SetChrPos(0xEF, 29440, 15000, 2090, 135)

    label("loc_457A")

    Jump("loc_4657")

    label("loc_457D")

    SetChrPos(0x109, 30850, 15000, 1020, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45D2")
    SetChrPos(0xEF, 29650, 15000, 270, 135)
    SetChrPos(0xF0, 29890, 15000, 2560, 135)
    SetChrPos(0xF1, 28620, 15000, 1560, 135)
    Jump("loc_4657")

    label("loc_45D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4616")
    SetChrPos(0xF0, 29650, 15000, 270, 135)
    SetChrPos(0xEF, 29890, 15000, 2560, 135)
    SetChrPos(0xF1, 28620, 15000, 1560, 135)
    Jump("loc_4657")

    label("loc_4616")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4657")
    SetChrPos(0xF1, 29650, 15000, 270, 135)
    SetChrPos(0xEF, 29890, 15000, 2560, 135)
    SetChrPos(0xF0, 28620, 15000, 1560, 135)

    label("loc_4657")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_470E")

    ChrTalk(    #97
        0x108,
        (
            "#075F#5P真是的……\x01",
            "还是那样毫不留情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4777")

    label("loc_470E")


    ChrTalk(    #98
        0x10A,
        (
            "#1316F#5P唉，\x01",
            "虽然这是第一次和她交手……\x02\x03",

            "#1314F毫不留情这点\x01",
            "还真是雾香小姐的风格呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4777")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47CC")

    ChrTalk(    #99
        0x101,
        (
            "#1008F#6P啊哈哈……\x01",
            "真看不出来这只是\x01",
            "再现出来的人格啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4906")

    label("loc_47CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4821")

    ChrTalk(    #100
        0x103,
        (
            "#1534F#6P呵呵……　\x01",
            "真看不出来这只是\x01",
            "再现出来的人格啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4906")

    label("loc_4821")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4871")

    ChrTalk(    #101
        0x106,
        (
            "#556F#6P嘿……\x01",
            "真看不出来这只是\x01",
            "再现出来的人格啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4906")

    label("loc_4871")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48C4")

    ChrTalk(    #102
        0x109,
        (
            "#1066F#6P哈哈……\x01",
            "真看不出来这只是\x01",
            "再现出来的人格啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4906")

    label("loc_48C4")


    ChrTalk(    #103
        0x109,
        (
            "#1066F#5P哈哈……\x01",
            "真看不出来这只是\x01",
            "再现出来的人格啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4906")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A72")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4984")

    def lambda_4928():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4928)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4954")

    def lambda_4949():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_4949)
    Jump("loc_4970")

    label("loc_4954")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4970")

    def lambda_4968():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_4968)

    label("loc_4970")

    Sleep(100)
    OP_8C(0xEF, 293, 400)
    Sleep(300)
    Jump("loc_4A6F")

    label("loc_4984")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49F4")

    def lambda_4998():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4998)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49C4")

    def lambda_49B9():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_49B9)
    Jump("loc_49E0")

    label("loc_49C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49E0")

    def lambda_49D8():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_49D8)

    label("loc_49E0")

    Sleep(100)
    OP_8C(0xF0, 293, 400)
    Sleep(300)
    Jump("loc_4A6F")

    label("loc_49F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A6F")

    def lambda_4A08():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4A08)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A34")

    def lambda_4A29():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4A29)
    Jump("loc_4A50")

    label("loc_4A34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A50")

    def lambda_4A48():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_4A48)

    label("loc_4A50")


    def lambda_4A56():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4A56)
    Sleep(100)
    OP_8C(0xF1, 293, 400)
    Sleep(300)

    label("loc_4A6F")

    Jump("loc_4A91")

    label("loc_4A72")


    def lambda_4A78():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4A78)
    Sleep(100)
    OP_8C(0x10A, 0, 400)
    Sleep(300)

    label("loc_4A91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B33")

    ChrTalk(    #104
        0x109,
        (
            "#1075F#6P好了……\x01",
            "现在应该可以前往\x01",
            "下一个领域了。\x02\x03",

            "#1840F不过看来大家也都累坏了，\x01",
            "先回据点休息一下，\x01",
            "再去调查周游道的石碑吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BC4")

    label("loc_4B33")


    ChrTalk(    #105
        0x109,
        (
            "#1075F#5P好了……\x01",
            "现在应该可以前往\x01",
            "下一个领域了。\x02\x03",

            "#1840F不过看来大家也都累坏了，\x01",
            "先回据点休息一下，\x01",
            "再去调查周游道的石碑吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C08")

    ChrTalk(    #106
        0x10F,
        (
            "#1447F#6P赞成……\x01",
            "我的肚子已经饿扁了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EC4")

    label("loc_4C08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C41")

    ChrTalk(    #107
        0x10B,
        (
            "#210F#6P嗯……\x01",
            "真是累坏了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EC4")

    label("loc_4C41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C70")

    ChrTalk(    #108
        0x105,
        "#1160F#6P知道了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EC4")

    label("loc_4C70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CA7")

    ChrTalk(    #109
        0x10E,
        (
            "#170F#6P嗯……\x01",
            "就这样吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EC4")

    label("loc_4CA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CE5")

    ChrTalk(    #110
        0x104,
        (
            "#1540F#6P呼……\x01",
            "这样是比较好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EC4")

    label("loc_4CE5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D13")

    ChrTalk(    #111
        0x10D,
        "#277F#6P知道了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EC4")

    label("loc_4D13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D4A")

    ChrTalk(    #112
        0x10C,
        (
            "#110F#6P嗯……\x01",
            "就这样吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EC4")

    label("loc_4D4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D81")

    ChrTalk(    #113
        0x102,
        "#1500F#6P这样是比较好呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EC4")

    label("loc_4D81")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4DBA")

    ChrTalk(    #114
        0x110,
        (
            "#261F#6P嘻嘻……\x01",
            "玲也赞成。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EC4")

    label("loc_4DBA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4DEA")

    ChrTalk(    #115
        0x107,
        "#560F#6P是、是啊～\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EC4")

    label("loc_4DEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E22")

    ChrTalk(    #116
        0x106,
        "#051F#6P啊啊，就这么办吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EC4")

    label("loc_4E22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E57")

    ChrTalk(    #117
        0x103,
        "#1520F#6P嗯，就这样吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EC4")

    label("loc_4E57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E95")

    ChrTalk(    #118
        0x101,
        (
            "#1025F#6P嗯……\x01",
            "确实有点累了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EC4")

    label("loc_4E95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EC4")

    ChrTalk(    #119
        0x108,
        "#070F#6P是啊，没错。\x02",
    )

    CloseMessageWindow()

    label("loc_4EC4")

    OP_A2(0x2B15)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4ED8")
    OP_A2(0x2641)

    label("loc_4ED8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EE9")
    OP_A2(0x2642)

    label("loc_4EE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EFA")
    OP_A2(0x2643)

    label("loc_4EFA")

    OP_28(0x39, 0x4, 0x4)
    OP_28(0x39, 0x4, 0x8)
    OP_28(0x39, 0x1, 0x1)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_12_43C3 end

    def Function_13_4F12(): pass

    label("Function_13_4F12")

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

    # Function_13_4F12 end

    def Function_14_4FB9(): pass

    label("Function_14_4FB9")

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

    # Function_14_4FB9 end

    def Function_15_5060(): pass

    label("Function_15_5060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5071")
    Call(0, 3)
    Return()

    label("loc_5071")

    OP_DE(0x0, 0x4, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_15_5060 end

    def Function_16_51F7(): pass

    label("Function_16_51F7")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_16_51F7 end

    def Function_17_535B(): pass

    label("Function_17_535B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5384")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_5378():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5378)

    label("loc_5384")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53AD")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_53A1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_53A1)

    label("loc_53AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53D6")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_53CA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_53CA)

    label("loc_53D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53FF")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_53F3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_53F3)

    label("loc_53FF")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_542B")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_542B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5442")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_5442")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5459")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_5459")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5470")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_5470")

    Return()

    # Function_17_535B end

    def Function_18_5471(): pass

    label("Function_18_5471")


    def lambda_5477():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5477)

    def lambda_5489():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5489)

    def lambda_549B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_549B)

    def lambda_54AD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_54AD)
    Sleep(1000)
    Return()

    # Function_18_5471 end

    def Function_19_54BF(): pass

    label("Function_19_54BF")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_19_54BF end

    def Function_20_54C6(): pass

    label("Function_20_54C6")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #120
        "\x07\x05门紧紧地关着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_20_54C6 end

    SaveToFile()

Try(main)
