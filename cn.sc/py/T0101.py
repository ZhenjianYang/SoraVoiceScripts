from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0101   ._SN',
        MapName             = 'rolent',
        Location            = 'T0101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0101_1 ._SN',
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
        '雪拉',                                 # 9
        '提妲',                                 # 10
        '科洛丝',                               # 11
        '奥利维尔',                             # 12
        '阿加特',                               # 13
        '洛连特·市长官邸',                     # 14
        '洛连特飞船坪',                         # 15
        '艾利兹街道方向',                       # 16
        '米尔西街道方向',                       # 17
        '玛鲁加山道方向',                       # 18
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
        'ED6_DT07/CH00020 ._CH',             # 00
        'ED6_DT07/CH00060 ._CH',             # 01
        'ED6_DT07/CH00040 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH00050 ._CH',             # 04
        'ED6_DT06/CH20038 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH00020P._CP',             # 00
        'ED6_DT07/CH00060P._CP',             # 01
        'ED6_DT07/CH00040P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00050P._CP',             # 04
        'ED6_DT06/CH20038P._CP',             # 05
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        X                   = 90860,
        Z                   = 0,
        Y                   = 40240,
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
        X                   = 49150,
        Z                   = 0,
        Y                   = 95090,
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
        X                   = 48960,
        Z                   = 0,
        Y                   = 1120,
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
        X                   = 5400,
        Z                   = 0,
        Y                   = 39830,
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
        X                   = 28060,
        Z                   = 0,
        Y                   = 80870,
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
        X                   = 43240,
        Y                   = -50,
        Z                   = 11610,
        Range               = 54840,
        Unknown_10          = 0x79E,
        Unknown_14          = 0x317E,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )

    DeclEvent(
        X                   = 18140,
        Y                   = -50,
        Z                   = 36360,
        Range               = 19090,
        Unknown_10          = 0x79E,
        Unknown_14          = 0xAF14,
        Unknown_18          = 0x0,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = 25210,
        Y                   = -50,
        Z                   = 70360,
        Range               = 30660,
        Unknown_10          = 0x79E,
        Unknown_14          = 0x11828,
        Unknown_18          = 0x0,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = 52800,
        Y                   = 0,
        Z                   = 18950,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 52800,
        Y                   = 0,
        Z                   = 29050,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = 44700,
        Y                   = 0,
        Z                   = 33020,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 24,
    )

    DeclEvent(
        X                   = 44700,
        Y                   = 0,
        Z                   = 21990,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = 30900,
        Y                   = 0,
        Z                   = 47270,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 26,
    )

    DeclEvent(
        X                   = 34300,
        Y                   = 0,
        Z                   = 52980,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 26,
    )

    DeclEvent(
        X                   = 66000,
        Y                   = 0,
        Z                   = 52470,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 27,
    )

    DeclEvent(
        X                   = 73000,
        Y                   = 0,
        Z                   = 34550,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 28,
    )

    DeclEvent(
        X                   = 54800,
        Y                   = 0,
        Z                   = 49170,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 29,
    )


    DeclActor(
        TriggerX            = 55000,
        TriggerZ            = 0,
        TriggerY            = 45300,
        TriggerRange        = 1700,
        ActorX              = 55000,
        ActorZ              = 2500,
        ActorY              = 45300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 44710,
        TriggerZ            = 0,
        TriggerY            = 70740,
        TriggerRange        = 1500,
        ActorX              = 44710,
        ActorZ              = 1800,
        ActorY              = 70740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 45280,
        TriggerZ            = 0,
        TriggerY            = 71310,
        TriggerRange        = 1500,
        ActorX              = 45280,
        ActorZ              = 1800,
        ActorY              = 71310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 76980,
        TriggerZ            = 0,
        TriggerY            = 19020,
        TriggerRange        = 800,
        ActorX              = 76980,
        ActorZ              = 0,
        ActorY              = 19020,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_42A",          # 00, 0
        "Function_1_47D",          # 01, 1
        "Function_2_4C9",          # 02, 2
        "Function_3_5B2",          # 03, 3
        "Function_4_AEC",          # 04, 4
        "Function_5_B1C",          # 05, 5
        "Function_6_B4C",          # 06, 6
        "Function_7_B7C",          # 07, 7
        "Function_8_BD1",          # 08, 8
        "Function_9_D9C",          # 09, 9
        "Function_10_F6D",         # 0A, 10
        "Function_11_113A",        # 0B, 11
        "Function_12_198B",        # 0C, 12
        "Function_13_19BB",        # 0D, 13
        "Function_14_19EB",        # 0E, 14
        "Function_15_1A1B",        # 0F, 15
        "Function_16_1A44",        # 10, 16
        "Function_17_1A99",        # 11, 17
        "Function_18_1B35",        # 12, 18
        "Function_19_1B87",        # 13, 19
        "Function_20_1C8B",        # 14, 20
        "Function_21_1CD4",        # 15, 21
        "Function_22_1D17",        # 16, 22
        "Function_23_1D1B",        # 17, 23
        "Function_24_1D1F",        # 18, 24
        "Function_25_1D23",        # 19, 25
        "Function_26_1D27",        # 1A, 26
        "Function_27_1D2B",        # 1B, 27
        "Function_28_1D2F",        # 1C, 28
        "Function_29_1D33",        # 1D, 29
    )


    def Function_0_42A(): pass

    label("Function_0_42A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_444")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 2)
    Jump("loc_47C")

    label("loc_444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_455")
    OP_A3(0x10F1)
    Event(0, 3)
    Jump("loc_47C")

    label("loc_455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_466")
    OP_A3(0x10F2)
    Event(0, 11)
    Jump("loc_47C")

    label("loc_466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_47C")
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(1, 2)
    Jump("loc_47C")

    label("loc_47C")

    Return()

    # Function_0_42A end

    def Function_1_47D(): pass

    label("Function_1_47D")

    OP_B1("T0100_n")
    OP_16(0x2, 0xFA0, 0xFFFEC780, 0xFFFEA840, 0x230001)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B9")
    SetMapFlags(0x10)
    OP_11(0x4B, 0x4B, 0x96, 0x0, 0xEA60, 0x0)

    label("loc_4B9")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_4C5"),
        (SWITCH_DEFAULT, "loc_4C8"),
    )


    label("loc_4C5")

    Jump("loc_4C8")

    label("loc_4C8")

    Return()

    # Function_1_47D end

    def Function_2_4C9(): pass

    label("Function_2_4C9")

    EventBegin(0x0)
    OP_11(0x4B, 0x4B, 0x96, 0x0, 0x15F90, 0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(50400, 0, 23350, 0)
    OP_67(0, 7720, -10000, 0)
    OP_6B(5070, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)

    def lambda_532():
        OP_6D(63060, 0, 57110, 9500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_532)

    def lambda_54A():
        OP_6C(38000, 9500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_54A)

    def lambda_55A():
        OP_67(0, 5420, -10000, 9500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_55A)
    FadeToBright(1000, 0)
    Sleep(8500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x0, 0x1)
    OP_44(0x0, 0x2)
    OP_44(0x0, 0x3)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0211   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_2_4C9 end

    def Function_3_5B2(): pass

    label("Function_3_5B2")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D2")
    Call(0, 17)
    FadeToBright(0, 0)
    Call(0, 18)

    label("loc_5D2")

    SetChrPos(0x101, 73060, 500, 32259, 0)
    SetChrPos(0x103, 73060, 500, 31260, 0)
    SetChrPos(0xF8, 73060, 500, 30260, 0)
    SetChrPos(0xF9, 73060, 500, 29260, 0)
    OP_6D(73090, 0, 34420, 0)
    OP_67(0, 8780, -10000, 0)
    OP_6B(2810, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0xE, 0)
    OP_70(0xE, 0x3B)
    OP_73(0xE)
    Sleep(200)
    OP_43(0x101, 0x1, 0x0, 0x4)
    OP_43(0x103, 0x1, 0x0, 0x5)
    OP_43(0xF8, 0x1, 0x0, 0x6)
    OP_43(0xF9, 0x1, 0x0, 0x7)

    def lambda_695():
        OP_6D(73020, 0, 37990, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_695)
    Sleep(2000)
    WaitChrThread(0xF9, 0x1)
    Sleep(200)

    ChrTalk(    #0
        0x101,
        (
            "#1010F#6P我说，各位……\x02\x03",

            "#1002F我觉得……\x01",
            "这会不会是『结社』干的好事？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_731")

    ChrTalk(    #1
        0x108,
        (
            "#074F啊啊……\x01",
            "很有可能。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B5")

    label("loc_731")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75E")

    ChrTalk(    #2
        0x104,
        (
            "#032F嗯……\x01",
            "很有可能。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B5")

    label("loc_75E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78B")

    ChrTalk(    #3
        0x106,
        (
            "#057F嗯……\x01",
            "很有可能。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B5")

    label("loc_78B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B5")

    ChrTalk(    #4
        0x105,
        (
            "#043F嗯……\x01",
            "很有可能。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_828")

    ChrTalk(    #5
        0x107,
        (
            "#561F连教区长都查不出原由，\x01",
            "原因不明的昏睡状态……\x02\x03",

            "#062F可以称为是\x01",
            "『不可能的现象』了吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_980")

    label("loc_828")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89D")

    ChrTalk(    #6
        0x105,
        (
            "#047F连教会都查不出原由，\x01",
            "原因不明的昏睡状态……\x02\x03",

            "#042F可能可以称为是\x01",
            "『不可能的现象』了吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_980")

    label("loc_89D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_910")

    ChrTalk(    #7
        0x106,
        (
            "#053F连教会的人都查不出原由，\x01",
            "原因不明的昏睡状态……\x02\x03",

            "#057F可以称为是\x01",
            "『不可能的现象』了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_980")

    label("loc_910")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_980")

    ChrTalk(    #8
        0x104,
        (
            "#035F连教会的人都查不出原由，\x01",
            "原因不明的昏睡状态……\x02\x03",

            "#032F可以称为是\x01",
            "『不可能的现象』了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_980")


    ChrTalk(    #9
        0x101,
        (
            "#1007F#6P果然是这样啊……\x02\x03",

            "#1002F那么，莫非\x01",
            "也有『暗示』吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x103,
        (
            "#026F#5P嗯……\x01",
            "有必要确认一下。\x02\x03",

            "#022F昏睡的人的名单\x01",
            "都记在笔记上了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#1004F#6P啊，等一等……\x02",
    )

    CloseMessageWindow()
    OP_AD(0x240116, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    OP_56(0x2)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #12
        0x103,
        (
            "#022F以那四个人身边的人为中心\x01",
            "走访一下整个城镇。\x02\x03",

            "转一圈后再返回协会\x01",
            "向爱娜报告就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#1002F#6P嗯……！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1812)
    OP_28(0x90, 0x4, 0x2)
    OP_28(0x90, 0x4, 0x8)
    OP_28(0x90, 0x1, 0x1)
    OP_28(0x90, 0x1, 0x2)
    OP_28(0x90, 0x1, 0x8)
    OP_28(0x90, 0x1, 0x20)
    OP_28(0x90, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_3_5B2 end

    def Function_4_AEC(): pass

    label("Function_4_AEC")

    OP_90(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
    OP_8E(0xFE, 0x11CE2, 0x0, 0x9934, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_4_AEC end

    def Function_5_B1C(): pass

    label("Function_5_B1C")

    OP_90(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
    OP_8E(0xFE, 0x12110, 0x0, 0x951A, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_5_B1C end

    def Function_6_B4C(): pass

    label("Function_6_B4C")

    OP_90(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
    OP_8E(0xFE, 0x118BE, 0x0, 0x94CA, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_6_B4C end

    def Function_7_B7C(): pass

    label("Function_7_B7C")

    OP_90(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(200)
    OP_6F(0xE, 59)
    OP_70(0xE, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xE)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0x11DFA, 0x0, 0x90BA, 0x7D0, 0x0)
    Return()

    # Function_7_B7C end

    def Function_8_BD1(): pass

    label("Function_8_BD1")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D04")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C1D")

    ChrTalk(    #14
        0x108,
        "#070F好，差不多该回协会了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C8C")

    label("loc_C1D")


    ChrTalk(    #15
        0x108,
        (
            "#070F呼，浓雾弥漫的夜路……\x02\x03",

            "对修行正合适，\x01",
            "不过现在时机\x01",
            "并不对。\x02\x03",

            "该问的都已经问过了，\x01",
            "我们回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_C8C")

    Jump("loc_D01")

    label("loc_C8F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA5")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_CAC")

    label("loc_CA5")

    TurnDirection(0x103, 0x0, 400)

    label("loc_CAC")


    ChrTalk(    #16
        0x103,
        (
            "#020F在雾这么浓的深夜\x01",
            "出去太危险了。\x02\x03",

            "该问的都已经问过了，\x01",
            "差不多该回协会了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D01")

    Jump("loc_D80")

    label("loc_D04")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3B")

    ChrTalk(    #17
        0x108,
        (
            "#070F夜已经深了，\x01",
            "赶快完成走访吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D80")

    label("loc_D3B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D51")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_D58")

    label("loc_D51")

    TurnDirection(0x103, 0x0, 400)

    label("loc_D58")


    ChrTalk(    #18
        0x103,
        (
            "#020F夜已经深了，尽快\x01",
            "完成走访吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D80")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_8_BD1 end

    def Function_9_D9C(): pass

    label("Function_9_D9C")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ECF")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DE8")

    ChrTalk(    #19
        0x108,
        "#070F好，差不多该回协会了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E57")

    label("loc_DE8")


    ChrTalk(    #20
        0x108,
        (
            "#070F呼，浓雾弥漫的夜路……\x02\x03",

            "对修行正合适，\x01",
            "不过现在时机\x01",
            "并不对。\x02\x03",

            "该问的都已经问过了，\x01",
            "我们回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_E57")

    Jump("loc_ECC")

    label("loc_E5A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E70")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_E77")

    label("loc_E70")

    TurnDirection(0x103, 0x0, 400)

    label("loc_E77")


    ChrTalk(    #21
        0x103,
        (
            "#020F在雾这么浓的深夜\x01",
            "出去太危险了。\x02\x03",

            "该问的都已经问过了，\x01",
            "差不多该回协会了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ECC")

    Jump("loc_F51")

    label("loc_ECF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F0C")

    ChrTalk(    #22
        0x108,
        (
            "#070F夜已经深了，\x01",
            "得赶快把事情做完才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F51")

    label("loc_F0C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F22")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_F29")

    label("loc_F22")

    TurnDirection(0x103, 0x0, 400)

    label("loc_F29")


    ChrTalk(    #23
        0x103,
        (
            "#020F夜已经深了，尽快\x01",
            "完成走访吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F51")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_9_D9C end

    def Function_10_F6D(): pass

    label("Function_10_F6D")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_109C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1027")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FB9")

    ChrTalk(    #24
        0x108,
        "#070F好，差不多该回协会了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1024")

    label("loc_FB9")


    ChrTalk(    #25
        0x108,
        (
            "#070F呼，浓雾弥漫的夜路……\x02\x03",

            "对修行正合适，\x01",
            "不过现在时机\x01",
            "并不对。\x02\x03",

            "该问的都问过了，\x01",
            "我们回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1024")

    Jump("loc_1099")

    label("loc_1027")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_103D")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_1044")

    label("loc_103D")

    TurnDirection(0x103, 0x0, 400)

    label("loc_1044")


    ChrTalk(    #26
        0x103,
        (
            "#020F在雾这么浓的深夜\x01",
            "出去太危险了。\x02\x03",

            "该问的都已经问过了，\x01",
            "差不多该回协会了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1099")

    Jump("loc_111E")

    label("loc_109C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D9")

    ChrTalk(    #27
        0x108,
        (
            "#070F夜已经深了，\x01",
            "得赶快把事情做完才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_111E")

    label("loc_10D9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10EF")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_10F6")

    label("loc_10EF")

    TurnDirection(0x103, 0x0, 400)

    label("loc_10F6")


    ChrTalk(    #28
        0x103,
        (
            "#020F夜已经深了，尽快\x01",
            "完成走访吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_111E")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_10_F6D end

    def Function_11_113A(): pass

    label("Function_11_113A")

    EventBegin(0x0)
    OP_6D(52910, 250, 28860, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 55680, 250, 28860, 270)
    SetChrPos(0x8, 56680, 250, 28860, 270)
    SetChrPos(0x9, 57680, 250, 28860, 270)
    SetChrPos(0xA, 58680, 250, 28860, 270)
    SetChrPos(0xB, 60680, 250, 28860, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0xA, 0)
    OP_70(0xA, 0x3B)
    OP_73(0xA)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0xC)
    OP_43(0x8, 0x1, 0x0, 0xD)
    OP_43(0x9, 0x1, 0x0, 0xE)
    OP_43(0xA, 0x1, 0x0, 0xF)
    OP_43(0xB, 0x1, 0x0, 0x10)
    Sleep(2000)

    def lambda_1230():
        OP_6D(50370, 0, 29350, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1230)

    def lambda_1248():
        OP_67(0, 8830, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1248)

    def lambda_1260():
        OP_6C(32000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1260)

    def lambda_1270():
        OP_6E(272, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1270)
    WaitChrThread(0xB, 0x1)
    Sleep(500)

    ChrTalk(    #29
        0xB,
        (
            "#030F呼，已经这么晚了，\x01",
            "还是快点回去休息的好。\x02\x03",

            "#031F那么，艾丝蒂尔，\x01",
            "能不能带我去拜访你家？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12EC():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_12EC)
    Sleep(50)

    def lambda_12FF():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_12FF)
    Sleep(50)
    TurnDirection(0xA, 0xB, 400)

    ChrTalk(    #30
        0x101,
        (
            "#1019F#6P等等……\x01",
            "你为什么要来？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xB,
        (
            "#031F哈哈哈。\x01",
            "不用这么警惕。\x02\x03",

            "我奥利维尔，\x01",
            "就算在后宫环境中\x01",
            "也能保持绅士风度。\x02\x03",

            "#037F呼呵呵……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        "#065F啊、啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "#045F#6P奥利维尔先生……\x01",
            "你的眼睛已经把你出卖了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1007F#6P真是的，该不该\x01",
            "直接用草席把你包着吊在外面呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0xA, 0)
    OP_70(0xA, 0x3B)
    OP_73(0xA)
    Sleep(200)
    SetChrPos(0xC, 55680, 250, 28860, 270)
    ClearChrFlags(0xC, 0x80)

    def lambda_145A():
        OP_8E(0xC, 0xCEAE, 0xFA, 0x70BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_145A)
    Sleep(500)

    def lambda_147A():
        OP_6D(51570, 0, 29500, 1500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_147A)
    WaitChrThread(0x106, 0x1)
    WaitChrThread(0x106, 0x0)

    ChrTalk(    #35
        0xC,
        (
            "#555F你这个没出息的演奏家，\x01",
            "在这里干吗呢。\x02\x03",

            "赶快决定巡逻的\x01",
            "队伍吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 400)

    ChrTalk(    #36
        0xB,
        (
            "#033F#6P咦……\x02\x03",

            "#031F……哈哈哈。\x01",
            "阿加特兄你真坏，\x02\x03",

            "巡逻不是说好由\x01",
            "你和金先生来嘛？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xC,
        (
            "#050F没这回事。\x02\x03",

            "我只记得是说\x01",
            "由我们这些男的负责巡逻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        "#033F#6P啊……\x02",
    )

    CloseMessageWindow()
    OP_8E(0xC, 0xCC4C, 0x82, 0x70BC, 0x7D0, 0x0)

    ChrTalk(    #39
        0xC,
        "#054F好了，赶紧来。\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    ChrTalk(    #40
        0xB,
        (
            "#036F#6P阿、阿加特兄。\x01",
            "能不能稍微等等？\x02\x03",

            "这样的后宫环境\x01",
            "可是很难得的啊。\x02\x03",

            "我会代替你一起享受的，\x01",
            "求你放过我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xC,
        "#053F少废话，赶紧开工。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x20)
    OP_8C(0xB, 270, 800)

    def lambda_1672():
        OP_90(0xFE, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1672)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 5)
    SetChrSubChip(0xB, 7)
    OP_63(0xB)

    def lambda_169F():
        OP_91(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_169F)
    WaitChrThread(0xB, 0x1)
    OP_6F(0xA, 59)
    OP_70(0xA, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xA)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    def lambda_1739():
        OP_6D(50370, 0, 29350, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1739)
    Sleep(1000)

    ChrTalk(    #42
        0x101,
        (
            "#1007F#6P嗯，对付奥利维尔\x01",
            "那样是最好的……\x02\x03",

            "#1019F不过真是个不知道啥叫紧张的家伙。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17AE():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_17AE)
    Sleep(50)

    def lambda_17C1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_17C1)
    Sleep(50)

    def lambda_17D4():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_17D4)
    WaitChrThread(0xA, 0x1)
    Sleep(400)

    ChrTalk(    #43
        0xA,
        (
            "#045F#2P呵呵，我到现在都不知道\x01",
            "他到底是说笑的还是认真的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1015F#6P我看１００％是认真的……\x02\x03",

            "#1006F总之他肯定是个\x01",
            "会教坏提妲的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        (
            "#067F#4P姐、姐姐这么说的话\x01",
            "奥利维尔先生就太可怜了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        "#524F#5P呵呵……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #47
        0x101,
        "#1015F#6P雪拉姐？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#027F#5P嗯，没什么。\x02\x03",

            "不过奥利维尔他说的也对，\x01",
            "今夜就早点休息吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1006F#6P嗯，是啊。\x02\x03",

            "提妲，科洛丝。\x01",
            "我来给你们带路。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_113A end

    def Function_12_198B(): pass

    label("Function_12_198B")

    OP_90(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
    OP_90(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_12_198B end

    def Function_13_19BB(): pass

    label("Function_13_19BB")

    OP_90(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
    OP_90(0xFE, 0xFFFFFC18, 0x0, 0x3E8, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_13_19BB end

    def Function_14_19EB(): pass

    label("Function_14_19EB")

    OP_90(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
    OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_14_19EB end

    def Function_15_1A1B(): pass

    label("Function_15_1A1B")

    OP_90(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
    OP_90(0xFE, 0xFFFFF768, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_15_1A1B end

    def Function_16_1A44(): pass

    label("Function_16_1A44")

    OP_8E(0xFE, 0xCEAE, 0xFA, 0x70BC, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(200)
    OP_6F(0xA, 59)
    OP_70(0xA, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xA)
    OP_8C(0xFE, 270, 400)
    OP_90(0xFE, 0xFFFFFB32, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_16_1A44 end

    def Function_17_1A99(): pass

    label("Function_17_1A99")

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
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B16"),
        (1, "loc_1B1C"),
        (SWITCH_DEFAULT, "loc_1B22"),
    )


    label("loc_1B16")

    OP_A2(0x1200)
    Jump("loc_1B22")

    label("loc_1B1C")

    OP_A2(0x1201)
    Jump("loc_1B22")

    label("loc_1B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1B30")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_1B34")

    label("loc_1B30")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_1B34")

    Return()

    # Function_17_1A99 end

    def Function_18_1B35(): pass

    label("Function_18_1B35")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_18_1B35 end

    def Function_19_1B87(): pass

    label("Function_19_1B87")

    SetMapFlags(0x80)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #50
        (
            "\x07\x05『七耀历１０７５年』\x01",
            "　由利贝尔王室、七耀教会\x01",
            "　以及洛连特市共同建造。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #51
        (
            "\x07\x05『七耀历１１９２年』\x01",
            "　百日战役中，被围攻洛连特的\x01",
            "　埃雷波尼亚帝国军队炮击而倒塌。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #52
        (
            "\x07\x05『七耀历１１９７年』\x01",
            "　在市民的协力下得以重建。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    ClearMapFlags(0x80)
    Return()

    # Function_19_1B87 end

    def Function_20_1C8B(): pass

    label("Function_20_1C8B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #53
        "\x07\x05西　玛鲁加山道一侧出口\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_20_1C8B end

    def Function_21_1CD4(): pass

    label("Function_21_1CD4")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #54
        "\x07\x05北　洛连特飞船坪\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_21_1CD4 end

    def Function_22_1D17(): pass

    label("Function_22_1D17")

    SetPlaceName(0x4)
    Return()

    # Function_22_1D17 end

    def Function_23_1D1B(): pass

    label("Function_23_1D1B")

    SetPlaceName(0x2)
    Return()

    # Function_23_1D1B end

    def Function_24_1D1F(): pass

    label("Function_24_1D1F")

    SetPlaceName(0x6)
    Return()

    # Function_24_1D1F end

    def Function_25_1D23(): pass

    label("Function_25_1D23")

    SetPlaceName(0x5)
    Return()

    # Function_25_1D23 end

    def Function_26_1D27(): pass

    label("Function_26_1D27")

    SetPlaceName(0x7)
    Return()

    # Function_26_1D27 end

    def Function_27_1D2B(): pass

    label("Function_27_1D2B")

    SetPlaceName(0x8)
    Return()

    # Function_27_1D2B end

    def Function_28_1D2F(): pass

    label("Function_28_1D2F")

    SetPlaceName(0x3)
    Return()

    # Function_28_1D2F end

    def Function_29_1D33(): pass

    label("Function_29_1D33")

    SetPlaceName(0xA)
    Return()

    # Function_29_1D33 end

    SaveToFile()

Try(main)
