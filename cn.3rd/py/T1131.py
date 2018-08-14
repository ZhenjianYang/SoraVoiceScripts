from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1131   ._SN',
        MapName             = 'Bose',
        Location            = 'T1131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T1131   ._SN',
            '',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '维尔纳',                               # 9
        '普拉达',                               # 10
        '索斯摩夫',                             # 11
        '料理',                                 # 12
        '汤勺',                                 # 13
        '亚妮拉丝',                             # 14
        '目标用照相机',                         # 15
        '',                                     # 16
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
        'ED6_DT07/CH01560 ._CH',             # 00
        'ED6_DT07/CH01280 ._CH',             # 01
        'ED6_DT07/CH02480 ._CH',             # 02
        'ED6_DT07/CH01570 ._CH',             # 03
        'ED6_DT07/CH02540 ._CH',             # 04
        'ED6_DT07/CH01003 ._CH',             # 05
        'ED6_DT07/CH01183 ._CH',             # 06
        'ED6_DT07/CH01023 ._CH',             # 07
        'ED6_DT07/CH01123 ._CH',             # 08
        'ED6_DT07/CH01120 ._CH',             # 09
        'ED6_DT07/CH01370 ._CH',             # 0A
        'ED6_DT07/CH01220 ._CH',             # 0B
        'ED6_DT07/CH01223 ._CH',             # 0C
        'ED6_DT07/CH01570 ._CH',             # 0D
        'ED6_DT07/CH01093 ._CH',             # 0E
        'ED6_DT07/CH01140 ._CH',             # 0F
        'ED6_DT07/CH01150 ._CH',             # 10
        'ED6_DT07/CH01043 ._CH',             # 11
        'ED6_DT07/CH01053 ._CH',             # 12
        'ED6_DT07/CH01000 ._CH',             # 13
        'ED6_DT07/CH01180 ._CH',             # 14
        'ED6_DT07/CH01153 ._CH',             # 15
        'ED6_DT07/CH01143 ._CH',             # 16
        'ED6_DT07/CH01020 ._CH',             # 17
        'ED6_DT06/CH20021 ._CH',             # 18
        'ED6_DT06/CH20020 ._CH',             # 19
        'ED6_DT07/CH01270 ._CH',             # 1A
        'ED6_DT07/CH01050 ._CH',             # 1B
        'ED6_DT07/CH01660 ._CH',             # 1C
        'ED6_DT07/CH02490 ._CH',             # 1D
        'ED6_DT07/CH01040 ._CH',             # 1E
        'ED6_DT07/CH02360 ._CH',             # 1F
        'ED6_DT07/CH02370 ._CH',             # 20
        'ED6_DT07/CH01090 ._CH',             # 21
        'ED6_DT07/CH01453 ._CH',             # 22
        'ED6_DT27/CH03090 ._CH',             # 23
    )

    AddCharChipPat(
        'ED6_DT07/CH01560P._CP',             # 00
        'ED6_DT07/CH01280P._CP',             # 01
        'ED6_DT07/CH02480P._CP',             # 02
        'ED6_DT07/CH01570P._CP',             # 03
        'ED6_DT07/CH02540P._CP',             # 04
        'ED6_DT07/CH01003P._CP',             # 05
        'ED6_DT07/CH01183P._CP',             # 06
        'ED6_DT07/CH01023P._CP',             # 07
        'ED6_DT07/CH01123P._CP',             # 08
        'ED6_DT07/CH01120P._CP',             # 09
        'ED6_DT07/CH01370P._CP',             # 0A
        'ED6_DT07/CH01220P._CP',             # 0B
        'ED6_DT07/CH01223P._CP',             # 0C
        'ED6_DT07/CH01570P._CP',             # 0D
        'ED6_DT07/CH01093P._CP',             # 0E
        'ED6_DT07/CH01140P._CP',             # 0F
        'ED6_DT07/CH01150P._CP',             # 10
        'ED6_DT07/CH01043P._CP',             # 11
        'ED6_DT07/CH01053P._CP',             # 12
        'ED6_DT07/CH01000P._CP',             # 13
        'ED6_DT07/CH01180P._CP',             # 14
        'ED6_DT07/CH01153P._CP',             # 15
        'ED6_DT07/CH01143P._CP',             # 16
        'ED6_DT07/CH01020P._CP',             # 17
        'ED6_DT06/CH20021P._CP',             # 18
        'ED6_DT06/CH20020P._CP',             # 19
        'ED6_DT07/CH01270P._CP',             # 1A
        'ED6_DT07/CH01050P._CP',             # 1B
        'ED6_DT07/CH01660P._CP',             # 1C
        'ED6_DT07/CH02490P._CP',             # 1D
        'ED6_DT07/CH01040P._CP',             # 1E
        'ED6_DT07/CH02360P._CP',             # 1F
        'ED6_DT07/CH02370P._CP',             # 20
        'ED6_DT07/CH01090P._CP',             # 21
        'ED6_DT07/CH01453P._CP',             # 22
        'ED6_DT27/CH03090P._CP',             # 23
    )

    DeclNpc(
        X                   = 2970,
        Z                   = 0,
        Y                   = 3650,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1400,
        Z                   = 0,
        Y                   = 1500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -7160,
        Z                   = 1580,
        Y                   = -4250,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -6140,
        Z                   = 2250,
        Y                   = -4000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 262169,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -6480,
        Z                   = 2250,
        Y                   = -4300,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1114137,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
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
        Unknown3            = 35,
        ChipIndex           = 0x23,
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


    ScpFunction(
        "Function_0_2AA",          # 00, 0
        "Function_1_2D3",          # 01, 1
        "Function_2_2D4",          # 02, 2
        "Function_3_2F8",          # 03, 3
        "Function_4_591",          # 04, 4
        "Function_5_6C3",          # 05, 5
        "Function_6_6E7",          # 06, 6
    )


    def Function_0_2AA(): pass

    label("Function_0_2AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_2D2")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 6)

    label("loc_2D2")

    Return()

    # Function_0_2AA end

    def Function_1_2D3(): pass

    label("Function_1_2D3")

    Return()

    # Function_1_2D3 end

    def Function_2_2D4(): pass

    label("Function_2_2D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F7")
    OP_8D(0xFE, -48200, 42570, -46450, 46500, 1000)
    Jump("Function_2_2D4")

    label("loc_2F7")

    Return()

    # Function_2_2D4 end

    def Function_3_2F8(): pass

    label("Function_3_2F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_590")
    OP_8E(0xFE, 0xFFFF2CFC, 0x5DC, 0xBB8, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF3350, 0x5DC, 0xCE4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0xFA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0x21FC, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF5358, 0x5DC, 0x2580, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF5358, 0x5DC, 0x2EE0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4D18, 0x5DC, 0x2EE0, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF4D7C, 0x5DC, 0x319C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF5FD8, 0x5DC, 0x319C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF77AC, 0x5DC, 0x30D4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF77AC, 0x5DC, 0x2E7C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF77AC, 0x5DC, 0x30D4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF80A8, 0x5DC, 0x30D4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF80A8, 0x5DC, 0x1F40, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF6EB0, 0x5DC, 0xFA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF6DE8, 0x5DC, 0xFFFFFB50, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7040, 0x5DC, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF72FC, 0x5DC, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF748C, 0x5DC, 0xFFFFF7CC, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF7428, 0x5DC, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF81D5, 0x5DC, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF81D5, 0x5DC, 0x190, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7748, 0x5DC, 0x190, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7040, 0x5DC, 0x960, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7040, 0x5DC, 0x2198, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF3990, 0x5DC, 0x2198, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0x1CE8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0x9C4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF2FCC, 0x5DC, 0xC8, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    Jump("Function_3_2F8")

    label("loc_590")

    Return()

    # Function_3_2F8 end

    def Function_4_591(): pass

    label("Function_4_591")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C2")
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF7CC, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFEFFC, 0x5DC, 0xFFFFFBB4, 0x3E8, 0x0)
    OP_8E(0xFE, 0xFFFFE890, 0x5DC, 0xFFFFF574, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFE37C, 0x5DC, 0xFFFFFF9C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE37C, 0xCB2, 0x834, 0x3E8, 0x0)
    OP_8E(0xFE, 0xFFFFEC78, 0xCB2, 0x1004, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFE638, 0xCB2, 0x898, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE638, 0x5DC, 0x0, 0x3E8, 0x0)
    OP_8E(0xFE, 0xFFFFE890, 0x5DC, 0xFFFFF574, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFEFFC, 0x5DC, 0xFFFFFBB4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF7CC, 0x0, 0xFFFFFB50, 0x3E8, 0x0)
    OP_8E(0xFE, 0x578, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    Jump("Function_4_591")

    label("loc_6C2")

    Return()

    # Function_4_591 end

    def Function_5_6C3(): pass

    label("Function_5_6C3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E6")
    OP_8D(0xFE, -47100, -2490, -44490, -1060, 2000)
    Jump("Function_5_6C3")

    label("loc_6E6")

    Return()

    # Function_5_6C3 end

    def Function_6_6E7(): pass

    label("Function_6_6E7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(370, 0, 2000, 0)
    OP_67(0, 6220, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x11, 1400, 0, 1500, 180)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 1400, 0, 300, 0)
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0 op#A
        "\x07\x00#15A#4S证言①\x18\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_1D(0xBF)
    FadeToBright(1500, 0)
    OP_6B(2700, 1500)
    OP_0D()
    Sleep(500)

    ChrTalk(    #1
        0x11,
        (
            "#11P嗯嗯，\x01",
            "那两个人确实到店里来过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x11,
        (
            "#11P好像在餐桌席\x01",
            "亲密地谈论着什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x11,
        (
            "#11P对话的内容\x01",
            "我可就不知道了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x11,
        (
            "#11P不过那位莉拉小姐很少见地面带笑容，\x01",
            "所以我印象很深刻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x15,
        (
            "#819F#6P哦、哦～，带着笑容啊……\x02\x03",

            "#816F还有，普拉达。\x01",
            "对方那个男性\x01",
            "是怎样的人你还记得吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x11,
        (
            "#11P嗯～\x01",
            "感觉是个既潇洒又温柔的人吧？\x02",
        )
    )

    Jump("loc_949")

    label("loc_949")

    CloseMessageWindow()

    ChrTalk(    #7
        0x11,
        (
            "#11P具体是什么身份\x01",
            "我就不知道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x15,
        "#817F#6P唔唔，原来如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x11,
        (
            "#11P……我说，亚妮拉丝。\x01",
            "你为什么要打听这种事啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x15,
        "#819F#6P嗯～这个是因为……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x11,
        (
            "#11P不用说了，我明白。\x01",
            "这是恋爱，是恋爱对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        (
            "#11P回想起来，\x01",
            "那时候莉拉小姐的表情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x11,
        (
            "#11P那毫无疑问\x01",
            "是恋爱中的少女的表情啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #14
        0x11,
        (
            "#11P嗯～\x01",
            "莉拉小姐的春天终于也到来了吗～\x02",
        )
    )

    Jump("loc_AF3")

    label("loc_AF3")

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #15
        0x15,
        (
            "#1316F#6P我、我说，\x01",
            "这个还不确定啦。\x02\x03",

            "#1314F普拉达……\x01",
            "拜托你可千万\x01",
            "别告诉其他客人哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x11,
        "#11P好～知道啦☆\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T1101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_6E7 end

    SaveToFile()

Try(main)
