from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1707   ._SN',
        MapName             = 'Bose',
        Location            = 'C1707.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        '歼灭天使玲',                           # 9
        '福音',                                 # 10
        '帕蒂尔·玛蒂尔',                       # 11
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
        'ED6_DT27/CH04510 ._CH',             # 00
        'ED6_DT06/CH20020 ._CH',             # 01
        'ED6_DT27/CH04000 ._CH',             # 02
        'ED6_DT27/CH04010 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT27/CH04510P._CP',             # 00
        'ED6_DT06/CH20020P._CP',             # 01
        'ED6_DT27/CH04000P._CP',             # 02
        'ED6_DT27/CH04010P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 458753,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1E6,
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_12A",          # 00, 0
        "Function_1_142",          # 01, 1
        "Function_2_160",          # 02, 2
        "Function_3_1029",         # 03, 3
        "Function_4_10B0",         # 04, 4
    )


    def Function_0_12A(): pass

    label("Function_0_12A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_141")
    OP_A3(0x10F0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x53), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_141")

    Return()

    # Function_0_12A end

    def Function_1_142(): pass

    label("Function_1_142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_156")
    OP_B1("C1707_y")
    Jump("loc_15F")

    label("loc_156")

    OP_B1("C1707_n")

    label("loc_15F")

    Return()

    # Function_1_142 end

    def Function_2_160(): pass

    label("Function_2_160")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_177")
    Call(0, 3)
    Call(0, 4)

    label("loc_177")

    OP_82(0x80, 0x0)
    OP_82(0x82, 0x0)
    OP_72(0x9, 0x4)
    OP_72(0x8, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    LoadEffect(0x2, "map\\\\mp064_01.eff")
    LoadEffect(0x3, "map\\\\mp065_01.eff")
    LoadEffect(0x4, "map\\\\mp064_00.eff")
    LoadEffect(0x5, "map\\\\mp065_00.eff")
    OP_72(0x0, 0x4)
    OP_A1(0xA, 0x0)
    SetChrPos(0xA, 10580, 500, 9330, 225)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0x14)
    OP_6F(0x0, 381)
    OP_70(0x0, 0x1A4)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x1)
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x40)
    SetChrPos(0x101, 1200, 0, 1200, 45)
    SetChrPos(0x102, 870, 0, 2560, 45)
    SetChrPos(0xF8, -50, 0, 110, 45)
    SetChrPos(0xF9, -450, 0, 1740, 45)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrPos(0x8, 1220, 950, 12420, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    ClearChrFlags(0x8, 0x1)
    OP_CF(0x8, 0x0, "Frame85__ren")
    OP_51(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(34920, 250, 12030, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3960, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x1C3, 0x0, 0x64)

    def lambda_386():
        OP_6D(6260, 250, 8340, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_386)

    def lambda_39E():
        OP_67(0, 5950, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39E)

    def lambda_3B6():
        OP_6B(4940, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3B6)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    WaitChrThread(0x101, 0x0)
    Fade(500)
    OP_71(0x8, 0x4)
    OP_6D(7230, 250, 9770, 0)
    OP_67(0, 3510, -10000, 0)
    OP_6B(5260, 0)
    OP_6C(32000, 0)
    OP_6E(243, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x101,
        "#1026F#5P恢、恢复了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        "#1042F#5P『塔』已经解放了吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "#1302F#6P……真无趣。\x02\x03",

            "时间再多一点的话，\x01",
            "就能把你们全部杀光了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x113, 0x1, 0x46)
    OP_22(0x114, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0xA, 0, -500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    PlayEffect(0x4, 0x1, 0xA, 4950, 2800, 0, 0, 0, 20, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0xA, -4950, 2800, 0, 0, 0, 340, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BB")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5F9")

    label("loc_5BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E2")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5F9")

    label("loc_5E2")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_620")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_65E")

    label("loc_620")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_647")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_65E")

    label("loc_647")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_65E")

    Sleep(1000)

    def lambda_669():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_669)

    def lambda_677():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_677)
    Sleep(100)

    def lambda_68A():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_68A)
    OP_8C(0xF9, 45, 400)

    ChrTalk(    #3
        0x101,
        "#1005F#5P慢、慢着！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#1306F#6P哈哈哈……\x01",
            "玲要回『古罗力亚斯』了。\x02\x03",

            "教授说过，『β』一旦完成\x01",
            "就让玲回去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#1020F#5P教、教授！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        (
            "#1044F#5P『β』已经完成了……\x02\x03",

            "#1046F恢复『塔』的原样\x01",
            "也是计划的一部分吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#263F#6P谁知道？\x01",
            "玲也不怎么清楚。\x02\x03",

            "#1305F不过，听说笼罩这里的结界\x01",
            "是『环』的“手”。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1026F#5P『辉之环』的……手！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#261F#6P嘻嘻……\x01",
            "会是什么意思呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_836():
        OP_6D(11800, 4800, 10810, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_836)

    def lambda_84E():
        OP_67(0, 3560, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_84E)

    def lambda_866():
        OP_6B(3450, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_866)

    def lambda_876():
        OP_6C(41000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_876)

    def lambda_886():
        OP_6E(325, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_886)
    PlayEffect(0x2, 0x1, 0xA, 5000, 2500, 0, 0, 0, 20, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0xA, -4900, 2500, 0, 0, 0, 340, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_900():
        OP_8F(0xFE, 0x2954, 0x9C4, 0x2472, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_900)
    Sleep(300)

    def lambda_920():
        OP_8F(0xFE, 0x2954, 0x9C4, 0x2472, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_920)
    Sleep(300)

    def lambda_940():
        OP_8F(0xFE, 0x2954, 0x9C4, 0x2472, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_940)
    OP_24(0x113, 0x50)
    Sleep(100)
    OP_72(0x0, 0x20)
    OP_D8(0x0, 0x1F4)
    OP_6F(0x0, 241)
    OP_70(0x0, 0x104)
    OP_82(0x0, 0x2)
    Sleep(50)
    PlayEffect(0x2, 0x1, 0xA, 4600, 2600, 0, 0, 0, 18, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0xA, -4600, 2600, 0, 0, 0, 342, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)

    def lambda_9F2():
        OP_8F(0xFE, 0x2954, 0x9C4, 0x2472, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9F2)
    OP_24(0x113, 0x5A)
    Sleep(100)
    OP_24(0x113, 0x64)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0x101, 0x1)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #10
        0x8,
        (
            "#263F#5P哈哈哈，那么再见了。\x02\x03",

            "#1304F下次见面时──\x01",
            "我会把你们全部杀掉。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A80():
        OP_8C(0xFE, 80, 10)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_A80)
    Sleep(200)

    def lambda_A93():
        OP_8C(0xFE, 80, 15)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_A93)
    Sleep(200)

    def lambda_AA6():
        OP_8C(0xFE, 80, 20)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_AA6)
    Sleep(500)

    def lambda_AB9():
        OP_8C(0xFE, 80, 30)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_AB9)
    Sleep(100)

    def lambda_ACC():
        OP_8C(0xFE, 80, 40)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_ACC)
    Sleep(2500)
    Fade(500)
    OP_6D(16090, 5040, 13150, 0)
    OP_67(0, 3440, -10000, 0)
    OP_6B(3690, 0)
    OP_6C(39000, 0)
    OP_6E(325, 0)
    ClearChrFlags(0xA, 0x1)

    def lambda_B26():
        OP_8C(0xFE, 80, 20)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_B26)
    Sleep(500)

    def lambda_B39():
        OP_8C(0xFE, 80, 15)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_B39)
    Sleep(500)

    def lambda_B4C():
        OP_8C(0xFE, 80, 10)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_B4C)
    WaitChrThread(0xA, 0x2)

    def lambda_B5F():
        OP_6B(3900, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B5F)
    OP_72(0x0, 0x20)
    OP_D8(0x0, 0x1F4)
    OP_6F(0x0, 261)
    OP_70(0x0, 0x118)
    OP_22(0x116, 0x0, 0x64)
    OP_73(0x0)
    Sleep(500)
    PlayEffect(0x3, 0x0, 0xA, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0xA, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x4, 0xA, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x5, 0xA, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x6, 0xA, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x7, 0xA, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x114, 0x0, 0x64)
    Sleep(2000)
    PlayEffect(0x2, 0x0, 0xA, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x3, 0xA, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0xA, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x5, 0xA, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x6, 0xA, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x7, 0xA, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 281)
    OP_70(0x0, 0x12C)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    Sleep(500)

    def lambda_E37():
        OP_6D(16040, 8000, 13170, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E37)

    def lambda_E4F():
        OP_67(0, 690, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E4F)

    def lambda_E67():
        OP_6C(75000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E67)

    def lambda_E77():
        OP_6E(548, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E77)

    def lambda_E87():
        OP_8F(0xFE, 0x25968, 0x61A8, 0x5064, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E87)
    Sleep(100)

    def lambda_EA7():
        OP_8F(0xFE, 0x25968, 0x61A8, 0x5064, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_EA7)
    Sleep(100)

    def lambda_EC7():
        OP_8F(0xFE, 0x16F2D8, 0x61A8, 0x5064, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_EC7)
    Sleep(100)

    def lambda_EE7():
        OP_8F(0xFE, 0x25968, 0x61A8, 0x5064, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_EE7)
    Sleep(100)

    def lambda_F07():
        OP_8F(0xFE, 0x25968, 0x61A8, 0x5064, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F07)
    Sleep(100)

    def lambda_F27():
        OP_8F(0xFE, 0x25968, 0x7530, 0x5064, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F27)
    Sleep(100)

    def lambda_F47():
        OP_8F(0xFE, 0x25968, 0x7530, 0x5064, 0x59D8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F47)
    Sleep(100)

    def lambda_F67():
        OP_8F(0xFE, 0x25968, 0x7530, 0x5064, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F67)
    Sleep(100)

    def lambda_F87():
        OP_8F(0xFE, 0x25968, 0x9C40, 0x5064, 0x80E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F87)
    Sleep(100)

    def lambda_FA7():
        OP_8F(0xFE, 0x25968, 0x9C40, 0x5064, 0x9470, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_FA7)
    Sleep(100)

    def lambda_FC7():
        OP_8F(0xFE, 0x25968, 0xC350, 0x5064, 0xA7F8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_FC7)
    Sleep(100)

    def lambda_FE7():
        OP_8F(0xFE, 0x25968, 0xC350, 0x5064, 0xBB80, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_FE7)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0x101, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x1E24)
    SetMapFlags(0x100000)
    OP_A2(0x10FF)
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_160 end

    def Function_3_1029(): pass

    label("Function_3_1029")

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
        (0, "loc_10A3"),
        (1, "loc_10A9"),
        (SWITCH_DEFAULT, "loc_10AF"),
    )


    label("loc_10A3")

    OP_A2(0x1200)
    Jump("loc_10AF")

    label("loc_10A9")

    OP_A2(0x1201)
    Jump("loc_10AF")

    label("loc_10AF")

    Return()

    # Function_3_1029 end

    def Function_4_10B0(): pass

    label("Function_4_10B0")

    FadeToDark(0, 0, -1)
    OP_6D(-66940, 250, 36210, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_4_10B0 end

    SaveToFile()

Try(main)
