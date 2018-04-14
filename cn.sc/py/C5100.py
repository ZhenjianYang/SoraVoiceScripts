from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5100   ._SN',
        MapName             = 'Other',
        Location            = 'C5100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60062",
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
        '暴动钢臂（黑）',                       # 9
        '地震控制用假人',                       # 10
        '中枢塔入口',                           # 11
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
        'ED6_DT29/CH12520 ._CH',             # 00
        'ED6_DT29/CH12521 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT29/CH12520P._CP',             # 00
        'ED6_DT29/CH12521P._CP',             # 01
    )

    DeclNpc(
        X                   = -30,
        Z                   = 4000,
        Y                   = 47660,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 310,
        Z                   = 4000,
        Y                   = 82310,
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
        X                   = 0,
        Y                   = 6000,
        Z                   = -135000,
        Range               = 2000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = -7000,
        Y                   = 4000,
        Z                   = -59610,
        Range               = 7130,
        Unknown_10          = 0x1388,
        Unknown_14          = 0xFFFF0C54,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )


    DeclActor(
        TriggerX            = -27960,
        TriggerZ            = 4000,
        TriggerY            = -101880,
        TriggerRange        = 800,
        ActorX              = -27560,
        ActorZ              = 5000,
        ActorY              = -101880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -26160,
        TriggerZ            = 4000,
        TriggerY            = -102500,
        TriggerRange        = 800,
        ActorX              = -26140,
        ActorZ              = 6000,
        ActorY              = -102180,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1A2",          # 00, 0
        "Function_1_1E2",          # 01, 1
        "Function_2_263",          # 02, 2
        "Function_3_279",          # 03, 3
        "Function_4_2A2",          # 04, 4
        "Function_5_5B2",          # 05, 5
        "Function_6_5DD",          # 06, 6
        "Function_7_623",          # 07, 7
        "Function_8_669",          # 08, 8
        "Function_9_694",          # 09, 9
        "Function_10_E91",         # 0A, 10
        "Function_11_EBE",         # 0B, 11
        "Function_12_F89",         # 0C, 12
        "Function_13_1094",        # 0D, 13
        "Function_14_120E",        # 0E, 14
        "Function_15_1295",        # 0F, 15
        "Function_16_1328",        # 10, 16
    )


    def Function_0_1A2(): pass

    label("Function_0_1A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1B3")
    OP_A3(0x10F0)
    Event(0, 13)
    Jump("loc_1E1")

    label("loc_1B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_1C4")
    OP_A3(0x10F1)
    Event(0, 9)
    Jump("loc_1E1")

    label("loc_1C4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E1")
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_1E1")

    Return()

    # Function_0_1A2 end

    def Function_1_1E2(): pass

    label("Function_1_1E2")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFD92E8, 0x230071)
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 0)
    OP_71(0x3, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 6)), scpexpr(EXPR_END)), "loc_255")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x42), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0x2, 0x1)
    OP_64(0x0, 0x1)
    OP_71(0x4, 0x4)
    OP_72(0x1, 0x10)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 30)
    OP_43(0x9, 0x3, 0x0, 0x3)
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    OP_22(0x85, 0x1, 0x46)
    Jump("loc_262")

    label("loc_255")

    OP_10(0x2, 0x0)
    OP_71(0x1, 0x4)
    OP_22(0x1C7, 0x0, 0x64)

    label("loc_262")

    Return()

    # Function_1_1E2 end

    def Function_2_263(): pass

    label("Function_2_263")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_278")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_263")

    label("loc_278")

    Return()

    # Function_2_263 end

    def Function_3_279(): pass

    label("Function_3_279")

    OP_C4(0x0, 0x20)

    label("loc_27F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A1")
    OP_7C(0x3C, 0x3C, 0x3E8, 0x384)
    Sleep(1000)
    Jump("loc_27F")

    label("loc_2A1")

    Return()

    # Function_3_279 end

    def Function_4_2A2(): pass

    label("Function_4_2A2")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B9")
    Call(0, 14)
    Call(0, 15)

    label("loc_2B9")

    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x8, 0x80)
    OP_6D(26370, 4000, -100180, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x1E)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x2)
    OP_43(0x101, 0x1, 0x0, 0x5)
    Sleep(800)
    LoadEffect(0x0, "map\\mp096_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 25500, 9000, -106000, -20, 0, 25, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_43(0x102, 0x1, 0x0, 0x6)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x7)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x8)

    def lambda_3AC():
        OP_6D(26630, 4000, -104390, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3AC)

    def lambda_3C4():
        OP_67(0, 5830, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3C4)

    def lambda_3DC():
        OP_6B(3650, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3DC)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_6F(0x2, 30)
    OP_70(0x2, 0x0)

    ChrTalk(    #0
        0x101,
        (
            "#1007F#5P好、好刺眼……\x02\x03",

            "#1004F咦，这里是……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x102, 315, 400)

    ChrTalk(    #1
        0x102,
        "#1042F#6P艾丝蒂尔……那个！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(13060, 4000, -109970, 0)
    OP_67(0, 6220, -10000, 0)
    OP_6B(8560, 0)
    OP_6C(348000, 0)
    OP_6E(262, 0)
    OP_6D(11490, 4000, -99590, 0)
    OP_67(0, 6540, -10000, 0)
    OP_6B(7760, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)

    def lambda_4FF():
        OP_6D(50, 4000, 33050, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4FF)

    def lambda_517():
        OP_67(0, 3780, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_517)

    def lambda_52F():
        OP_6B(4190, 10000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_52F)

    def lambda_53F():
        OP_6C(0, 10000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_53F)

    def lambda_54F():
        OP_6E(412, 10000)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_54F)

    def lambda_55F():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55F)
    Sleep(50)

    def lambda_572():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_572)
    Sleep(50)

    def lambda_585():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_585)
    Sleep(9000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0x2)
    OP_44(0x101, 0x3)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C5101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_2A2 end

    def Function_5_5B2(): pass

    label("Function_5_5B2")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 27960, 4000, -98520, 180)
    OP_8E(0xFE, 0x6D38, 0xFA0, 0xFFFE5F84, 0x7D0, 0x0)
    Return()

    # Function_5_5B2 end

    def Function_6_5DD(): pass

    label("Function_6_5DD")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 27960, 4000, -98520, 180)
    OP_8E(0xFE, 0x6D38, 0xFA0, 0xFFFE6F10, 0x7D0, 0x0)
    OP_8E(0xFE, 0x6766, 0xFA0, 0xFFFE64D4, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_6_5DD end

    def Function_7_623(): pass

    label("Function_7_623")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 27960, 4000, -98520, 180)
    OP_8E(0xFE, 0x6D38, 0xFA0, 0xFFFE6F10, 0x7D0, 0x0)
    OP_8E(0xFE, 0x724C, 0xFA0, 0xFFFE6268, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_7_623 end

    def Function_8_669(): pass

    label("Function_8_669")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 27960, 4000, -98520, 180)
    OP_8E(0xFE, 0x6BC6, 0xFA0, 0xFFFE686C, 0x7D0, 0x0)
    Return()

    # Function_8_669 end

    def Function_9_694(): pass

    label("Function_9_694")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6AB")
    Call(0, 14)
    Call(0, 15)

    label("loc_6AB")

    OP_6D(18100, 4000, -99210, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3820, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 17390, 4000, -98710, 0)
    SetChrPos(0x102, 18670, 4000, -98620, 0)
    SetChrPos(0xF8, 18060, 4000, -100190, 0)
    SetChrPos(0xF9, 19290, 4000, -100050, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_770")

    ChrTalk(    #2
        0x108,
        "#072F#6P那就是『中枢塔』吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8AE")

    label("loc_770")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A5")

    ChrTalk(    #3
        0x106,
        "#057F#6P那就是『中枢塔』吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8AE")

    label("loc_7A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7DB")

    ChrTalk(    #4
        0x109,
        "#1063F#6P那就是『中枢塔』吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8AE")

    label("loc_7DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_815")

    ChrTalk(    #5
        0x104,
        (
            "#030F#6P嗯……\x01",
            "那就是『中枢塔』吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AE")

    label("loc_815")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_84A")

    ChrTalk(    #6
        0x103,
        "#022F#6P那就是『中枢塔』吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8AE")

    label("loc_84A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_87E")

    ChrTalk(    #7
        0x105,
        "#1162F#6P那就是『中枢塔』……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8AE")

    label("loc_87E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8AE")

    ChrTalk(    #8
        0x107,
        "#065F#6P那就是『中枢塔』……\x02",
    )

    CloseMessageWindow()

    label("loc_8AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_908")

    ChrTalk(    #9
        0x10B,
        (
            "#212F#6P……坠落以来，\x01",
            "一直看着那个塔……\x02\x03",

            "没想到是这么高大的塔……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B51")

    label("loc_908")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_960")

    ChrTalk(    #10
        0x107,
        (
            "#065F#6P远、远看虽然\x01",
            "也觉得很高大……\x02\x03",

            "但没想到是如此巨大的塔……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B51")

    label("loc_960")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B3")

    ChrTalk(    #11
        0x105,
        (
            "#1162F#6P远看也觉得\x01",
            "相当的大……\x02\x03",

            "没想到竟是这么大的塔啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B51")

    label("loc_9B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A1D")

    ChrTalk(    #12
        0x103,
        (
            "#025F#6P……远看也觉得\x01",
            "相当的大……\x02\x03",

            "#022F但这样近距离仰望之下\x01",
            "还真是超乎想象啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B51")

    label("loc_A1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A85")

    ChrTalk(    #13
        0x104,
        (
            "#035F#6P呀呀，远看\x01",
            "也觉得是很大的建筑物……\x02\x03",

            "#030F却没想到是这么\x01",
            "高层的建筑物啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B51")

    label("loc_A85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AFD")

    ChrTalk(    #14
        0x109,
        (
            "#1065F#6P即使在远处看也觉得\x01",
            "是座非常高的塔……\x02\x03",

            "#1063F但这样近距离仰望之下\x01",
            "还真是超乎预想的大啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B51")

    label("loc_AFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B51")

    ChrTalk(    #15
        0x106,
        (
            "#052F#6P远眺之下\x01",
            "觉得是座很大的塔……\x02\x03",

            "#057F但没想到竟然这么大。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B51")

    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    Sleep(500)
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    ChrTalk(    #16
        0x101,
        (
            "#1025F#5P……对了，约修亚。\x02\x03",

            "莱维和教授\x01",
            "他们在那里吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #17
        0x102,
        (
            "#1043F#4P……我认为可能性很高。\x02\x03",

            "#1042F看起来像是掌控\x01",
            "都市中枢的地方。\x02\x03",

            "说不定也会有\x01",
            "『辉之环』的线索。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1010F#5P是吗……\x02\x03",

            "#1002F……怎么办？\x01",
            "就这样冲进去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#1035F#4P……如果莱维他们在，\x01",
            "我想可能会遭遇到\x01",
            "前所未有的严酷战斗。\x02\x03",

            "#1040F先回『埃尔赛尤』\x01",
            "做好万全的准备才是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1006F#5P嗯……是啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D36")

    ChrTalk(    #21
        0x108,
        (
            "#070F#6P好，那么\x01",
            "赶快寻找站点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E75")

    label("loc_D36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D6E")

    ChrTalk(    #22
        0x106,
        (
            "#051F#6P好，那么\x01",
            "赶快寻找站点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E75")

    label("loc_D6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DA3")

    ChrTalk(    #23
        0x109,
        (
            "#1060F#6P那就赶快\x01",
            "寻找站点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E75")

    label("loc_DA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DDB")

    ChrTalk(    #24
        0x104,
        (
            "#035F#6P呼，那就赶快\x01",
            "寻找站点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E75")

    label("loc_DDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E0F")

    ChrTalk(    #25
        0x103,
        (
            "#027F#6P那就赶快\x01",
            "寻找站点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E75")

    label("loc_E0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E44")

    ChrTalk(    #26
        0x105,
        (
            "#1160F#6P那就赶快\x01",
            "寻找站点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E75")

    label("loc_E44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E75")

    ChrTalk(    #27
        0x107,
        (
            "#061F#6P那就赶快\x01",
            "寻找站点吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E75")

    OP_A2(0x2230)
    OP_28(0x9E, 0x1, 0x800)
    OP_28(0x9E, 0x1, 0x1000)
    OP_28(0x9F, 0x4, 0x2)
    OP_28(0x9F, 0x4, 0x8)
    EventEnd(0x0)
    Return()

    # Function_9_694 end

    def Function_10_E91(): pass

    label("Function_10_E91")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #28
        "\x07\x05门牢牢地锁着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_10_E91 end

    def Function_11_EBE(): pass

    label("Function_11_EBE")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #29
        (
            "\x07\x05【紧急避难通道】\x01",
            "中枢塔≌ 卡尔玛丽\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #30
        (
            "\x07\x05只有在来自『中枢塔』的\x01",
            "导力供给产生异常的情况下\x01",
            "才会自动解除锁定。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #31
        (
            "\x07\x05此外，门边\x01",
            "禁止放置会\x01",
            "妨碍避难的物体。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_EBE end

    def Function_12_F89(): pass

    label("Function_12_F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 6)), scpexpr(EXPR_END)), "loc_F91")
    Return()

    label("loc_F91")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-290, 6000, -134740, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x101, 0, 6000, -134000, 0)
    OP_89(0x102, -1000, 6000, -135000, 0)
    OP_89(0xF8, 1000, 6000, -135000, 0)
    OP_89(0xF9, 0, 6000, -136000, 0)
    OP_0D()
    Sleep(100)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x258)

    def lambda_103D():
        OP_6D(-290, 55000, -134740, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_103D)

    def lambda_1055():
        OP_67(0, 10570, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1055)

    def lambda_106D():
        OP_6C(320000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_106D)
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C6003   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_F89 end

    def Function_13_1094(): pass

    label("Function_13_1094")

    EventBegin(0x0)
    OP_6D(-290, 45000, -134740, 0)
    OP_67(0, 10570, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(320000, 0)
    OP_6E(262, 0)
    OP_6F(0x0, 500)
    OP_48()
    OP_89(0x101, 0, 70000, -134000, 0)
    OP_89(0x102, -1000, 70000, -135000, 0)
    OP_89(0xF8, 1000, 70000, -135000, 0)
    OP_89(0xF9, 0, 70000, -136000, 0)
    OP_22(0xEB, 0x0, 0x64)
    FadeToBright(1000, 0)

    def lambda_1133():
        OP_6D(-290, 6000, -134740, 9000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1133)

    def lambda_114B():
        OP_67(0, 6500, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_114B)

    def lambda_1163():
        OP_6C(315000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1163)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_23(0xEB)
    WaitChrThread(0x101, 0x1)
    Sleep(200)
    Fade(500)
    OP_6D(240, 6010, -133220, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 240, 6010, -133220, 0)
    SetChrPos(0x1, 240, 6010, -133220, 0)
    SetChrPos(0x2, 240, 6010, -133220, 0)
    SetChrPos(0x3, 240, 6010, -133220, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_13_1094 end

    def Function_14_120E(): pass

    label("Function_14_120E")

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
        (0, "loc_1288"),
        (1, "loc_128E"),
        (SWITCH_DEFAULT, "loc_1294"),
    )


    label("loc_1288")

    OP_A2(0x1200)
    Jump("loc_1294")

    label("loc_128E")

    OP_A2(0x1201)
    Jump("loc_1294")

    label("loc_1294")

    Return()

    # Function_14_120E end

    def Function_15_1295(): pass

    label("Function_15_1295")

    FadeToDark(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_15_1295 end

    def Function_16_1328(): pass

    label("Function_16_1328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1331")
    Return()

    label("loc_1331")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_13B9")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_134A"),
        (1, "loc_1380"),
        (SWITCH_DEFAULT, "loc_13B6"),
    )


    label("loc_134A")


    ChrTalk(    #32
        0x101,
        (
            "#1002F这里是『中枢塔』吧。\x01",
            "……必须回去才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B6")

    label("loc_1380")


    ChrTalk(    #33
        0x102,
        (
            "#1042F这里是『中枢塔』了。\x01",
            "……必须回去才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B6")

    label("loc_13B6")

    Jump("loc_1476")

    label("loc_13B9")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_13C9"),
        (1, "loc_13FE"),
        (SWITCH_DEFAULT, "loc_1427"),
    )


    label("loc_13C9")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #34
        0x102,
        (
            "#1042F艾丝蒂尔！\x01",
            "那边是『中枢塔』哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1427")

    label("loc_13FE")


    ChrTalk(    #35
        0x102,
        "#1042F不是！　这边是『中枢塔』。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1427")

    label("loc_1427")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #36
        0x101,
        "#1002F……避难通道在前面啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #37
        0x102,
        "#1042F啊啊……赶快吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1476")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    Return()

    # Function_16_1328 end

    SaveToFile()

Try(main)
