from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3605_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3605.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/C3605_1 ._SN',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_B5",           # 03, 3
        "Function_4_FF2",          # 04, 4
        "Function_5_102C",         # 05, 5
        "Function_6_1066",         # 06, 6
        "Function_7_10C4",         # 07, 7
        "Function_8_43F7",         # 08, 8
        "Function_9_4401",         # 09, 9
        "Function_10_444E",        # 0A, 10
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    Call(1, 3)
    Call(1, 7)
    Return()

    # Function_2_AC end

    def Function_3_B5(): pass

    label("Function_3_B5")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC")
    Call(0, 5)
    Call(0, 6)

    label("loc_CC")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_E9"),
        (5, "loc_100"),
        (4, "loc_117"),
        (6, "loc_12E"),
        (8, "loc_145"),
        (SWITCH_DEFAULT, "loc_15C"),
    )


    label("loc_E9")

    OP_D2(0x701D0, 0x701DC, 0x12)
    OP_D2(0x701D1, 0x701DD, 0x13)
    Jump("loc_15C")

    label("loc_100")

    OP_D2(0x70218, 0x70224, 0x12)
    OP_D2(0x70219, 0x70225, 0x13)
    Jump("loc_15C")

    label("loc_117")

    OP_D2(0x70200, 0x7020C, 0x12)
    OP_D2(0x70201, 0x7020D, 0x13)
    Jump("loc_15C")

    label("loc_12E")

    OP_D2(0x70230, 0x7023C, 0x12)
    OP_D2(0x70231, 0x7023D, 0x13)
    Jump("loc_15C")

    label("loc_145")

    OP_D2(0x270176, 0x270183, 0x12)
    OP_D2(0x270177, 0x270184, 0x13)
    Jump("loc_15C")

    label("loc_15C")

    OP_D2(0x26019C, 0x2601A1, 0x14)
    OP_D2(0x2600A0, 0x2600A5, 0x15)
    OP_D2(0x260052, 0x260057, 0x16)
    OP_D2(0x29014C, 0x290150, 0x17)
    OP_D2(0x29014D, 0x290151, 0x18)
    OP_6D(-3550, 13000, -1710, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(307000, 0)
    OP_6E(282, 0)
    SetChrPos(0x8, -1150, 950, 12410, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 20)
    OP_71(0x5, 0x4)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_70(0x0, 0x8)
    OP_70(0x1, 0x8)
    OP_70(0x2, 0x8)
    OP_70(0x3, 0x8)
    OP_70(0x4, 0x8)
    LoadEffect(0x0, "map\\\\mp061_00.eff")
    LoadEffect(0x1, "Scraft\\\\sc005_03.eff")
    LoadEffect(0x2, "scraft\\\\sc000_11.eff")
    LoadEffect(0x3, "battle\\\\btbomb00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x101, 740, -1750, -7480, 0)
    SetChrPos(0x102, -650, -1750, -7480, 0)
    SetChrPos(0xF9, 820, -1750, -7480, 0)
    SetChrPos(0x108, -750, -1750, -7480, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x108, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_71(0xC, 0x4)
    FadeToBright(2000, 0)

    def lambda_335():
        OP_6D(-550, 0, -1710, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_335)

    def lambda_34D():
        OP_67(0, 8480, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_34D)

    def lambda_365():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_365)

    def lambda_375():
        OP_6C(320000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_375)

    def lambda_385():
        OP_6E(282, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_385)
    Sleep(4000)
    ClearChrFlags(0x101, 0x80)

    def lambda_39F():
        OP_8E(0xFE, 0x2E4, 0x0, 0xFFFFF808, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39F)
    Sleep(100)
    ClearChrFlags(0x102, 0x80)

    def lambda_3C4():
        OP_8E(0xFE, 0xFFFFFD76, 0x0, 0xFFFFF827, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C4)
    Sleep(800)
    ClearChrFlags(0xF9, 0x80)

    def lambda_3E9():
        OP_8E(0xFE, 0x334, 0x0, 0xFFFFF240, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3E9)
    Sleep(100)
    ClearChrFlags(0x108, 0x80)

    def lambda_40E():
        OP_8E(0xFE, 0xFFFFFD12, 0x0, 0xFFFFF1FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_40E)
    WaitChrThread(0x108, 0x1)
    Sleep(500)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #0
        0x101,
        "#1007F#6PFINALLY here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        "#1043F#6PThat was definitely a climb.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #2
        0x8,
        "Man's Voice",
        "#3PHeh. Figured you'd be dropping in.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52D")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_56B")

    label("loc_52D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_554")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_56B")

    label("loc_554")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_56B")

    Sleep(1000)
    OP_1D(0x6F)
    Sleep(500)

    def lambda_57D():
        OP_6D(-1310, 950, 13270, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57D)

    def lambda_595():
        OP_67(0, 6500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_595)

    def lambda_5AD():
        OP_6E(307, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5AD)
    WaitChrThread(0x101, 0x3)
    SetChrPos(0x108, 740, -1750, -7480, 0)
    SetChrPos(0x102, -650, -1750, -7480, 0)
    SetChrPos(0x101, 820, -1750, -7480, 0)
    SetChrPos(0xF9, -750, -1750, -7480, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 12)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 18)

    def lambda_62E():
        OP_8F(0xFE, 0xFFFFFE3E, 0x0, 0x1388, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_62E)
    Sleep(300)

    def lambda_64E():
        OP_8F(0xFE, 0x29E, 0x0, 0xED8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_64E)
    Sleep(200)

    def lambda_66E():
        OP_8F(0xFE, 0xFFFFFB5A, 0x0, 0xF3C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_66E)
    Sleep(300)

    def lambda_68E():
        OP_8F(0xFE, 0x64, 0x0, 0x834, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_68E)
    Fade(500)
    OP_6D(-1490, 1000, 9000, 0)
    OP_67(0, 3640, -10000, 0)
    OP_6B(3640, 0)
    OP_6C(333000, 0)
    OP_6E(293, 0)
    OP_0D()
    WaitChrThread(0xF9, 0x1)
    Sleep(500)

    ChrTalk(    #3
        0x108,
        "#072F#5PWalter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#250F#4PZin. Knew you'd come.\x02\x03",

            "And hey, it's Fangboy.\x01",
            "Been a while, kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#1035F#5PIt has.\x02\x03",

            "#1042FI'm surprised, though, Walter.\x01",
            "You never mentioned being part\x01",
            "of the school Zin trained at.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#252F#4PHeh, yeah, well, I've pulled in a lot of\x01",
            "styles aside from just the Taito school.\x02\x03",

            "Gotta diversify if you want to beat people\x01",
            "to death with their own arms, you know?\x02\x03",

            "No big surprise you never noticed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x108,
        "#572F#5PWalter, you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#250F#4PSo how about you, Zin?\x02\x03",

            "Still clingin' to that dusty old\x01",
            "Living Fist?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x108,
        (
            "#074F#5PYeah, well. You know. I'm a clumsy guy.\x02\x03",

            "#070FAfraid I could never hope to be half\x01",
            "as good as our master was in Taito\x01",
            "if I tried branching into other styles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#254F#4PTch. Dull as ever.\x02\x03",

            "#252FAh, whatever. I was gettin' bored\x01",
            "just sittin' up here.\x02\x03",

            "Time for a good, old-fashioned\x01",
            "deathmatch.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x8, 0x0, 0x2, 0x5DC)
    Sleep(1000)
    OP_99(0x8, 0x3, 0x9, 0x5DC)
    Sleep(200)
    ClearChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 2)
    Sleep(200)
    OP_99(0x8, 0x1, 0x2, 0x3E8)
    OP_22(0xBC, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_A99():
        OP_6D(-930, 1000, 5500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A99)

    def lambda_AB1():
        OP_67(0, 4160, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AB1)

    def lambda_AC9():
        OP_6B(3690, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AC9)

    def lambda_AD9():
        OP_6E(293, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_AD9)
    SetChrPos(0xA, 12740, 250, 9670, 270)
    SetChrPos(0xB, -13570, 250, 6260, 90)
    SetChrPos(0xC, 9220, 250, -3940, 270)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x800)
    OP_43(0xA, 0x3, 0x0, 0x2)
    OP_43(0xB, 0x3, 0x0, 0x2)
    OP_43(0xC, 0x3, 0x0, 0x2)
    OP_43(0xA, 0x2, 0x1, 0x4)
    Sleep(100)
    OP_43(0xB, 0x2, 0x1, 0x5)
    Sleep(100)
    OP_43(0xC, 0x2, 0x1, 0x6)
    Sleep(500)
    SetChrSubChip(0x8, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD9")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C17")

    label("loc_BD9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C00")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C17")

    label("loc_C00")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_C17")

    Sleep(1000)

    def lambda_C22():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C22)
    Sleep(50)

    def lambda_C35():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C35)
    Sleep(50)
    OP_8C(0xF9, 180, 400)
    WaitChrThread(0xA, 0x2)
    WaitChrThread(0xB, 0x2)
    WaitChrThread(0xC, 0x2)

    ChrTalk(    #11
        0x101,
        "#1020F#5PWaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        "#1042F#5PSteel Cougars!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC6")

    ChrTalk(    #13
        0x106,
        "#054F#2PMore society armored freaks?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_DB6")

    label("loc_CC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D06")

    ChrTalk(    #14
        0x103,
        "#024F#2PThe society's weaponized animals!\x02",
    )

    CloseMessageWindow()
    Jump("loc_DB6")

    label("loc_D06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D2F")

    ChrTalk(    #15
        0x107,
        "#065F#2PWaaaaaaah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_DB6")

    label("loc_D2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D6B")

    ChrTalk(    #16
        0x105,
        "#042F#2PArmored animals... How cruel.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DB6")

    label("loc_D6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DB6")

    ChrTalk(    #17
        0x109,
        (
            "#1069F#5PArmored beasts...\x01",
            "More of the society's tools!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB6")


    ChrTalk(    #18
        0x8,
        (
            "#250FYou have fun playin' with those,\x01",
            "kids.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-1040, 1200, 9600, 0)
    OP_67(0, 3100, -10000, 0)
    OP_6B(4200, 0)
    OP_6C(356000, 0)
    OP_6E(240, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #19
        0x8,
        (
            "#252FSo, c'mon, Zin. Show me.\x02\x03",

            "I wanna see those moves you've\x01",
            "been working on for six years!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x108,
        "#072F#5PI'll be more than glad to!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 22)
    SetChrSubChip(0x8, 1)
    OP_0D()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_EE7():
        OP_6D(-800, 950, 6000, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_EE7)

    def lambda_EFF():
        OP_67(0, 3960, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EFF)

    def lambda_F17():
        OP_6B(3300, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F17)
    SetChrSubChip(0x8, 2)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_F39():
        OP_96(0xFE, 0xFFFFFE20, 0x0, 0x1694, 0x7D0, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_F39)
    Sleep(100)
    SetChrChipByIndex(0xA, 24)

    def lambda_F61():
        OP_8E(0xFE, 0x2F8, 0x0, 0xEA6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_F61)
    SetChrChipByIndex(0xB, 24)

    def lambda_F81():
        OP_8E(0xFE, 0xFFFFFAC4, 0x0, 0xFBE, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_F81)
    SetChrChipByIndex(0xC, 24)

    def lambda_FA1():
        OP_8E(0xFE, 0xFFFFFF10, 0x0, 0x9A6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_FA1)
    WaitChrThread(0x101, 0x0)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_44(0x8, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    Battle(0x455, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_FEC"),
        (SWITCH_DEFAULT, "loc_FF1"),
    )


    label("loc_FEC")

    OP_B4(0x0)
    Jump("loc_FF1")

    label("loc_FF1")

    Return()

    # Function_3_B5 end

    def Function_4_FF2(): pass

    label("Function_4_FF2")

    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0x2968, 0xFA, 0x1360, 0x1770, 0x0)
    OP_8E(0xFE, 0x17B6, 0xFA, 0x114E, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 23)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_4_FF2 end

    def Function_5_102C(): pass

    label("Function_5_102C")

    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0xFFFFD972, 0xFA, 0xC80, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFE7BE, 0xFA, 0x13CE, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 23)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_5_102C end

    def Function_6_1066(): pass

    label("Function_6_1066")

    SetChrChipByIndex(0xFE, 24)
    SetChrFlags(0xFE, 0x4)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xFE, 0x13E2, 0x1360, 0xFFFFE610, 0x1388, 0x1770)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xFE, 0xFFFFFF92, 0x0, 0xFFFFF330, 0x7D0, 0x1770)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 23)
    ClearChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_6_1066 end

    def Function_7_10C4(): pass

    label("Function_7_10C4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x8, 0x0)
    OP_44(0xB, 0x0)
    OP_44(0xC, 0x0)
    OP_44(0xC, 0x0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_1114"),
        (5, "loc_112B"),
        (4, "loc_1142"),
        (6, "loc_1159"),
        (8, "loc_1170"),
        (SWITCH_DEFAULT, "loc_1187"),
    )


    label("loc_1114")

    OP_D2(0x701D0, 0x701DC, 0x12)
    OP_D2(0x701D1, 0x701DD, 0x13)
    Jump("loc_1187")

    label("loc_112B")

    OP_D2(0x70218, 0x70224, 0x12)
    OP_D2(0x70219, 0x70225, 0x13)
    Jump("loc_1187")

    label("loc_1142")

    OP_D2(0x70200, 0x7020C, 0x12)
    OP_D2(0x70201, 0x7020D, 0x13)
    Jump("loc_1187")

    label("loc_1159")

    OP_D2(0x70230, 0x7023C, 0x12)
    OP_D2(0x70231, 0x7023D, 0x13)
    Jump("loc_1187")

    label("loc_1170")

    OP_D2(0x270176, 0x270183, 0x12)
    OP_D2(0x270177, 0x270184, 0x13)
    Jump("loc_1187")

    label("loc_1187")

    OP_D2(0x26019C, 0x2601A1, 0x14)
    OP_D2(0x2600A0, 0x2600A5, 0x15)
    OP_D2(0x260052, 0x260057, 0x16)
    OP_D2(0x70251, 0x7025D, 0x17)
    OP_D2(0x7024D, 0x70259, 0x18)
    OP_D2(0x2601A7, 0x2601AC, 0x19)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 12)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 65535)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 18)
    SetChrPos(0x108, 40, 0, 5100, 0)
    SetChrPos(0x101, 210, 0, 3200, 0)
    SetChrPos(0x102, 1130, 0, 2410, 0)
    SetChrPos(0xF9, -530, 0, 1460, 0)
    SetChrPos(0x8, 50, 0, 10340, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 2)
    SetChrSubChip(0x8, 0)
    OP_71(0x5, 0x4)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_70(0x0, 0x8)
    OP_70(0x1, 0x8)
    OP_70(0x2, 0x8)
    OP_70(0x3, 0x8)
    OP_70(0x4, 0x8)
    LoadEffect(0x0, "map\\\\mp061_00.eff")
    LoadEffect(0x1, "scraft\\sc007_10.eff")
    LoadEffect(0x2, "scraft\\\\sc000_11.eff")
    LoadEffect(0x3, "battle\\\\btbomb00.eff")
    LoadEffect(0x4, "scraft\\\\sc000_10.eff")
    PlayEffect(0x0, 0x0, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_6D(1110, 0, 8260, 0)
    OP_67(0, 6210, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(344, 0)
    OP_71(0xC, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #21
        0x101,
        "#1002F#2PGrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        "#1043F#2PThat was about what I expected.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(0, 0, 8800, 0)
    OP_67(0, 4720, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(0, 0)
    OP_6E(287, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #23
        0x8,
        (
            "#250FNot bad. Your forms are all pretty\x01",
            "refined.\x02\x03",

            "#252FBut you ain't lyin' about being clumsy!\x01",
            "Your movements are so obvious.\x02\x03",

            "And it's because you're so stuck on\x01",
            "sticking to just that ragged old Taito\x01",
            "style.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x108,
        "#070F#5PHaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        "#254FAnd what's so damned funny?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x108,
        (
            "#074F#5PYou really are a genius, but you lack\x01",
            "understanding of a core principle.\x02\x03",

            "Master must be ashamed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "#254FOh?\x02\x03",

            "You lecturin' me in place\x01",
            "of the old man, now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x108,
        (
            "#070F#5PI wouldn't presume to do\x01",
            "anything so great as that.\x02\x03",

            "#074FHowever, after matching fists with\x01",
            "you, I understood.\x02\x03",

            "As I am now, it would be very\x01",
            "difficult for me to win.\x02\x03",

            "#072FBut conversely, I wouldn't lose,\x01",
            "either.\x02\x03",

            "Your bloody fists cannot defeat me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#254F...\x02\x03",

            "#251FInteresting.\x02\x03",

            "Never thought I'd hear something\x01",
            "that gutsy come outta your mouth.\x02\x03",

            "I thought I'd just have a taste to kill\x01",
            "some time, but we're past that now.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    Fade(500)
    SetChrSubChip(0x8, 0)
    OP_0D()
    SetChrChipByIndex(0x8, 25)
    OP_99(0x8, 0x0, 0x2, 0x3E8)
    Sleep(500)

    def lambda_17C6():
        OP_6B(3400, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17C6)
    PlayEffect(0x1, 0x1, 0x8, -100, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    ChrTalk(    #30
        0x8,
        (
            "#254FAssume your stance, Zin.\x02\x03",

            "It's about time I taught you just\x01",
            "what the hell 'difference in ability'\x01",
            "really means.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x108,
        "#072F#5P...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)
    OP_0D()
    Sleep(500)
    PlayEffect(0x1, 0x2, 0x108, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    ChrTalk(    #32
        0x101,
        (
            "#1020F(What should we do?\x01",
            "Should we help?!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        "#1042F#2P(I... I think this has to be Zin's fight.)\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x2)
    Sleep(500)
    OP_1D(0x2C)
    Sleep(500)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x108, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x108, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x108, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_19A9():
        OP_6B(2500, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19A9)

    def lambda_19B9():
        OP_6C(12000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19B9)

    def lambda_19C9():
        OP_6D(0, 500, 9500, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_19C9)

    def lambda_19E1():

        label("loc_19E1")

        TurnDirection(0xFE, 0x108, 400)
        OP_48()
        Jump("loc_19E1")

    QueueWorkItem2(0x101, 3, lambda_19E1)

    def lambda_19F2():

        label("loc_19F2")

        TurnDirection(0xFE, 0x108, 400)
        OP_48()
        Jump("loc_19F2")

    QueueWorkItem2(0x102, 3, lambda_19F2)

    def lambda_1A03():

        label("loc_1A03")

        TurnDirection(0xFE, 0x108, 400)
        OP_48()
        Jump("loc_1A03")

    QueueWorkItem2(0xF9, 3, lambda_1A03)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x108, 0x40)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x108, 0x1000)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 7)

    def lambda_1A46():
        OP_99(0xFE, 0x0, 0x1, 0x640)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1A46)

    def lambda_1A56():
        OP_8F(0xFE, 0x28, 0x0, 0x2706, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A56)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_1A7B():
        OP_99(0xFE, 0x0, 0x4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_1A7B)
    OP_8F(0x108, 0x28, 0x0, 0x23BE, 0x2EE0, 0x0)

    def lambda_1A9F():

        label("loc_1A9F")

        OP_9E(0xFE, 0x14, 0x0, 0x1388, 0x9C4)
        OP_48()
        Jump("loc_1A9F")

    QueueWorkItem2(0x8, 3, lambda_1A9F)

    def lambda_1ABC():

        label("loc_1ABC")

        OP_9E(0xFE, 0x14, 0x0, 0x1388, 0x9C4)
        OP_48()
        Jump("loc_1ABC")

    QueueWorkItem2(0x108, 3, lambda_1ABC)
    PlayEffect(0x4, 0xFF, 0x8, 0, 700, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0x190, 0xBB8, 0x12C)
    Sleep(500)
    OP_44(0x8, 0x3)
    OP_44(0x108, 0x3)

    def lambda_1B2C():
        OP_6C(24000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B2C)

    def lambda_1B3C():
        OP_96(0xFE, 0x910, 0xFA, 0x286E, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B3C)

    def lambda_1B5A():
        OP_96(0xFE, 0xFFFFF6F0, 0xFA, 0x286E, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1B5A)
    WaitChrThread(0x108, 0x1)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x108, 14)
    SetChrSubChip(0x108, 0)
    OP_8C(0x8, 270, 0)
    OP_8C(0x108, 90, 0)

    def lambda_1B9F():
        OP_6D(-8380, 250, 9110, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B9F)

    def lambda_1BB7():
        OP_6B(2820, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1BB7)
    SetChrPos(0x101, 300, 0, 2110, 0)
    SetChrPos(0x102, 930, 0, 1470, 0)
    SetChrPos(0xF9, -810, 0, 1110, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0xF9, 0)
    OP_96(0x108, 0xFFFFDB02, 0xFA, 0x2378, 0x1F4, 0x1F40)
    OP_96(0x8, 0xFFFFDEEA, 0xFA, 0x2364, 0x1F4, 0x1F40)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 7)

    def lambda_1C50():
        OP_99(0xFE, 0x0, 0xD, 0x640)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1C50)
    SetChrChipByIndex(0x108, 14)
    SetChrSubChip(0x108, 0)
    Sleep(200)
    OP_22(0x1FB, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x8, 0, 800, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1CA9():

        label("loc_1CA9")

        OP_9E(0xFE, 0x1E, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_1CA9")

    QueueWorkItem2(0x108, 1, lambda_1CA9)
    OP_7C(0x64, 0xC8, 0xBB8, 0x64)
    Sleep(300)
    OP_22(0x1FB, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x8, 0, 800, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0xC8, 0xBB8, 0x64)

    def lambda_1D27():
        OP_96(0xFE, 0xFFFFDDA0, 0xFA, 0x2364, 0x12C, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1D27)
    Sleep(400)
    OP_22(0x1FB, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x8, 0, 1058642330, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0xC8, 0xBB8, 0x64)
    OP_44(0x108, 0x1)
    SetChrChipByIndex(0x108, 24)
    SetChrSubChip(0x108, 1)
    Sleep(200)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)

    def lambda_1DB2():
        OP_91(0xFE, 0xFFFFFCE0, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_1DB2)
    WaitChrThread(0x8, 0x1)
    OP_96(0x108, 0xFFFFDEEA, 0xFA, 0x1F90, 0x1F4, 0x1F40)
    TurnDirection(0x108, 0x8, 0)
    TurnDirection(0x8, 0x108, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_1E0B():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1E0B)
    SetChrSubChip(0x8, 2)
    SetChrChipByIndex(0x8, 25)
    OP_22(0x1FB, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x8, 0, 700, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0xC8, 0xBB8, 0x64)
    Sleep(100)
    OP_91(0x8, 0x0, 0x0, 0x320, 0x2710, 0x0)
    WaitChrThread(0x108, 0x1)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)
    SetChrSubChip(0x8, 3)
    Sleep(300)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)

    def lambda_1EAC():
        OP_96(0xFE, 0xFFFFDB02, 0xFA, 0x209E, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1EAC)
    Sleep(100)

    def lambda_1ECF():
        OP_96(0xFE, 0xFFFFEAA2, 0xFA, 0x209E, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1ECF)
    WaitChrThread(0x8, 0x1)

    def lambda_1EF2():
        OP_6D(-6390, 250, 2530, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1EF2)

    def lambda_1F0A():
        OP_6C(48000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F0A)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x108, 0x1000)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 6)

    def lambda_1F2E():
        OP_8E(0xFE, 0xFFFFEAA2, 0xFA, 0x1194, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1F2E)

    def lambda_1F49():
        OP_8E(0xFE, 0xFFFFDB02, 0xFA, 0x11A8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1F49)
    WaitChrThread(0x108, 0x1)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    TurnDirection(0x108, 0x8, 0)
    TurnDirection(0x8, 0x108, 0)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x108, 0x1000)

    def lambda_1F8B():
        OP_96(0xFE, 0xFFFFEAA2, 0xFA, 0x11A8, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1F8B)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_1FB3():
        OP_99(0xFE, 0x0, 0x4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_1FB3)
    Sleep(100)
    OP_22(0x208, 0x0, 0x64)

    def lambda_1FCD():
        OP_96(0xFE, 0xFFFFEAA2, 0xFA, 0x1784, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1FCD)
    WaitChrThread(0x108, 0x1)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)
    WaitChrThread(0x108, 0x2)
    TurnDirection(0x108, 0x8, 0)
    TurnDirection(0x8, 0x108, 0)

    def lambda_200D():
        OP_6D(-2380, 250, -860, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_200D)
    SetChrFlags(0x108, 0x1000)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 9)

    def lambda_2034():
        OP_99(0xFE, 0x0, 0xD, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2034)
    Sleep(500)
    PlayEffect(0x4, 0xFF, 0x108, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x3DCCCCCD, 0xFA0, 0xBB8, 0x64)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 17)

    def lambda_2099():
        OP_96(0xFE, 0xFFFFEAA2, 0xFA, 0xFFFFF560, 0x64, 0x3A98)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2099)
    WaitChrThread(0x108, 0x1)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)

    def lambda_20D0():
        OP_6C(80000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20D0)

    def lambda_20E0():
        OP_96(0x8, 0xFFFFEAA2, 0xFA, 0xFFFFF948, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_20E0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 7)

    def lambda_2108():
        OP_99(0xFE, 0x0, 0x2, 0x9C4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2108)
    OP_22(0x208, 0x0, 0x64)
    OP_96(0x108, 0xFFFFF088, 0xFA, 0xFFFFF948, 0x1F4, 0x1F40)
    TurnDirection(0x108, 0x8, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    TurnDirection(0x8, 0x108, 0)
    OP_8F(0x8, 0xFFFFECA0, 0xFA, 0xFFFFF948, 0x2710, 0x0)
    OP_96(0x108, 0xFFFFFC40, 0xFA, 0xFFFFFD30, 0x1F4, 0x1F40)
    OP_96(0x108, 0x7A8, 0xFA, 0xFFFFF560, 0x1F4, 0x1F40)
    OP_96(0x108, 0xB90, 0xFA, 0xFFFFF948, 0x1F4, 0x1F40)

    def lambda_21A5():
        OP_6D(10500, 250, -1530, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_21A5)
    OP_96(0x8, 0x7A8, 0xFA, 0xFFFFF948, 0x1F4, 0x1B58)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 9)

    def lambda_21DE():
        OP_99(0xFE, 0x0, 0xD, 0xDAC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_21DE)
    OP_22(0x208, 0x0, 0x64)
    OP_96(0x108, 0xFFFFF088, 0xFA, 0xFFFFF948, 0x7D0, 0x1F40)
    TurnDirection(0x108, 0x8, 0)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_221B():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_221B)

    def lambda_2229():
        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_2229)
    OP_8F(0x108, 0x3C0, 0xFA, 0xFFFFF948, 0x4E20, 0x0)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 15)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 8)
    PlayEffect(0x4, 0xFF, 0x8, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0x190, 0xBB8, 0x64)
    OP_8F(0x8, 0x2300, 0xFA, 0xFFFFF948, 0x55F0, 0x0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_22CF():
        OP_99(0xFE, 0x0, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_22CF)

    def lambda_22DF():
        OP_8F(0xFE, 0x2AD0, 0xFA, 0xFFFFF948, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_22DF)
    Sleep(200)
    OP_22(0x208, 0x0, 0x64)

    def lambda_2304():
        OP_96(0xFE, 0x2300, 0xFA, 0xFFFFF178, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2304)

    def lambda_2322():

        label("loc_2322")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_2322")

    QueueWorkItem2(0x8, 2, lambda_2322)
    WaitChrThread(0x108, 0x1)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)
    WaitChrThread(0x8, 0x1)

    def lambda_2347():
        OP_6C(128000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2347)

    def lambda_2357():
        OP_6D(10500, 250, -530, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2357)
    OP_96(0x8, 0x1F18, 0xFA, 0xFFFFF948, 0x1F4, 0x1F40)
    OP_96(0x8, 0x267A, 0xFA, 0xFFFFF948, 0x1F4, 0x1F40)
    TurnDirection(0x108, 0x8, 0)
    OP_44(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 7)

    def lambda_23B2():
        OP_99(0xFE, 0x0, 0xD, 0x640)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_23B2)
    OP_22(0x1FB, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x108, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0xC8, 0xBB8, 0x64)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_2417():

        label("loc_2417")

        OP_9E(0xFE, 0x1E, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_2417")

    QueueWorkItem2(0x108, 1, lambda_2417)
    Sleep(300)

    def lambda_2439():
        OP_99(0xFE, 0x0, 0x2, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_2439)
    OP_22(0x1FB, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x108, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0xC8, 0xBB8, 0x64)
    Sleep(500)
    SetChrChipByIndex(0x108, 16)
    SetChrSubChip(0x108, 0)
    OP_22(0x1FB, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x108, 0, 700, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0xC8, 0xBB8, 0x64)
    OP_44(0x108, 0x1)

    def lambda_24F2():
        OP_91(0xFE, 0x320, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_24F2)
    WaitChrThread(0x8, 0x1)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    WaitChrThread(0x108, 0x1)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)

    def lambda_252B():
        OP_91(0xFE, 0xFFFFFCE0, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_252B)
    Sleep(100)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_2555():
        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_2555)
    Sleep(100)
    OP_22(0x1FB, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x8, 0, 700, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0xC8, 0xBB8, 0x64)
    Sleep(100)

    def lambda_25BA():
        OP_91(0xFE, 0xFFFFFCE0, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_25BA)
    WaitChrThread(0x108, 0x2)

    def lambda_25DA():
        OP_91(0xFE, 0x320, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_25DA)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 9)

    def lambda_25FF():
        OP_99(0xFE, 0x0, 0xD, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_25FF)
    Sleep(400)
    OP_22(0x208, 0x0, 0x64)

    def lambda_2619():
        OP_96(0xFE, 0x267A, 0xFA, 0xFFFFED90, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2619)
    WaitChrThread(0x108, 0x1)
    TurnDirection(0x108, 0x8, 0)
    WaitChrThread(0x8, 0x2)
    TurnDirection(0x8, 0x108, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)

    def lambda_2659():
        OP_96(0xFE, 0x267A, 0xFA, 0xFFFFF63C, 0x12C, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2659)
    Sleep(100)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_2686():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_2686)
    Sleep(50)
    OP_22(0x208, 0x0, 0x64)
    Sleep(100)
    OP_96(0x8, 0x267A, 0xFA, 0xFFFFFCC2, 0x1F4, 0x1F40)
    WaitChrThread(0x108, 0x2)

    def lambda_26C1():
        OP_96(0xFE, 0x267A, 0xFA, 0xFFFFFA06, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_26C1)
    Sleep(100)

    def lambda_26E4():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_26E4)
    Sleep(50)
    OP_22(0x208, 0x0, 0x64)
    Sleep(100)
    OP_96(0x8, 0x290E, 0xFA, 0x384, 0x1F4, 0x1F40)

    def lambda_271A():
        OP_6D(8500, 250, 6500, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_271A)
    OP_96(0x8, 0x2832, 0xFA, 0x12D4, 0x1F4, 0x1F40)
    OP_96(0x8, 0x1EDC, 0xFA, 0x22B0, 0x1F4, 0x1F40)
    OP_96(0x108, 0x1E1E, 0xFA, 0x1310, 0x1F4, 0x1F40)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)

    def lambda_2781():
        OP_96(0xFE, 0x1EDC, 0xFA, 0x1CD4, 0x1F4, 0x2328)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2781)

    def lambda_279F():
        OP_96(0xFE, 0x1E1E, 0xFA, 0x18EC, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_279F)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_27C7():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_27C7)
    Sleep(100)
    WaitChrThread(0x8, 0x1)
    OP_22(0x1FB, 0x0, 0x64)
    SetChrChipByIndex(0x8, 25)
    SetChrSubChip(0x8, 2)
    PlayEffect(0x2, 0xFF, 0x8, 0, 700, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0xC8, 0xBB8, 0x64)

    def lambda_2836():
        OP_91(0xFE, 0x0, 0x0, 0x320, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2836)
    SetChrSubChip(0x8, 3)
    WaitChrThread(0x108, 0x2)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)

    def lambda_286F():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFCE0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_286F)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 9)

    def lambda_2894():
        OP_99(0xFE, 0x0, 0xD, 0x640)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2894)
    Sleep(500)
    SetChrChipByIndex(0x108, 24)
    SetChrSubChip(0x108, 0)
    OP_22(0x1FB, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x108, 0, 1300, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0xC8, 0xBB8, 0x64)

    def lambda_28FE():

        label("loc_28FE")

        OP_9E(0xFE, 0x14, 0x0, 0x1388, 0x9C4)
        OP_48()
        Jump("loc_28FE")

    QueueWorkItem2(0x108, 3, lambda_28FE)

    def lambda_291B():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFCE0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_291B)
    WaitChrThread(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    OP_44(0x108, 0x3)
    WaitChrThread(0x108, 0x1)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)

    def lambda_2958():
        OP_96(0xFE, 0x1EDC, 0xFA, 0x22B0, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2958)

    def lambda_2976():
        OP_96(0xFE, 0x1E1E, 0xFA, 0x1310, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2976)
    WaitChrThread(0x108, 0x1)

    def lambda_2999():
        OP_6D(630, 0, 6360, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2999)

    def lambda_29B1():
        OP_6C(153000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_29B1)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x108, 0x4)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x108, 0x1000)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)

    def lambda_29E9():
        OP_8E(0xFE, 0x0, 0xFA, 0x22B0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_29E9)

    def lambda_2A04():
        OP_8E(0xFE, 0x0, 0xFA, 0x1310, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2A04)
    WaitChrThread(0x108, 0x1)
    TurnDirection(0x8, 0x108, 0)
    TurnDirection(0x108, 0x8, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x108, 0x1000)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 7)

    def lambda_2A50():
        OP_96(0xFE, 0x0, 0xFA, 0x1504, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2A50)

    def lambda_2A6E():
        OP_99(0xFE, 0x0, 0x1, 0x640)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2A6E)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_2A88():
        OP_96(0xFE, 0x0, 0xFA, 0x24A4, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2A88)

    def lambda_2AA6():
        OP_99(0xFE, 0x0, 0x4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_2AA6)
    PlayEffect(0x4, 0xFF, 0xFF, 0, 1200, 6880, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0x190, 0xBB8, 0x96)
    WaitChrThread(0x108, 0x1)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)

    def lambda_2B15():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2B15)
    TurnDirection(0x108, 0x8, 400)
    Sleep(700)

    def lambda_2B2F():
        OP_96(0xFE, 0xB04, 0xFA, 0x1AE0, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2B2F)

    def lambda_2B4D():
        OP_96(0xFE, 0xFFFFF4CA, 0xFA, 0x1AE0, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2B4D)
    WaitChrThread(0x108, 0x1)
    TurnDirection(0x8, 0x108, 0)
    TurnDirection(0x108, 0x8, 0)
    WaitChrThread(0x108, 0x1)
    Fade(500)
    OP_44(0x101, 0x3)
    OP_44(0x102, 0x3)
    OP_44(0xF9, 0x3)

    def lambda_2B94():
        OP_8C(0xFE, 0, 0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2B94)

    def lambda_2BA2():
        OP_8C(0xFE, 0, 0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2BA2)

    def lambda_2BB0():
        OP_8C(0xFE, 0, 0)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_2BB0)
    OP_6D(1220, 0, 8760, 0)
    OP_67(-500, 5590, -10000, 0)
    OP_6B(1900, 0)
    OP_6C(45000, 0)
    OP_6E(481, 0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 7)

    def lambda_2C0B():
        OP_96(0xFE, 0xFFFFF4FC, 0xFA, 0x1AE0, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2C0B)

    def lambda_2C29():
        OP_99(0xFE, 0x0, 0x1, 0x640)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2C29)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 16)

    def lambda_2C43():
        OP_96(0xFE, 0xB36, 0xFA, 0x1AE0, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2C43)

    def lambda_2C61():
        OP_99(0xFE, 0x0, 0x4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_2C61)
    PlayEffect(0x4, 0xFF, 0xFF, 0, 1500, 6880, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x108, 0x1)
    PlayEffect(0x3, 0x3, 0xFF, -4100, 1000, 7000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0xFF, 4100, 1000, 7000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0x1F4, 0xBB8, 0x12C)
    OP_B0(0x8, 0xF)
    OP_6F(0x8, 0)
    OP_70(0x8, 0x1E)
    OP_B0(0x9, 0xF)
    OP_6F(0x9, 0)
    OP_70(0x9, 0x1E)
    OP_73(0x8)
    OP_73(0x9)
    OP_83(0x4, 0x2)
    Sleep(1000)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)

    def lambda_2D6C():
        OP_6D(1210, 0, 10570, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D6C)
    OP_22(0x23B, 0x0, 0x64)
    SetChrFlags(0x8, 0x1000)

    def lambda_2D8E():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2D8E)

    def lambda_2D9C():
        OP_96(0xFE, 0xFFFFF182, 0xFA, 0x218E, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2D9C)
    Sleep(100)
    OP_22(0x23B, 0x0, 0x64)
    SetChrFlags(0x108, 0x1000)

    def lambda_2DC9():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_2DC9)

    def lambda_2DD7():
        OP_96(0xFE, 0xFDB, 0xFA, 0x2378, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2DD7)
    WaitChrThread(0x108, 0x1)
    WaitChrThread(0x8, 0x1)
    ClearChrFlags(0x108, 0x1000)
    ClearChrFlags(0x8, 0x1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x108, 0x1)
    WaitChrThread(0x101, 0x0)
    Sleep(300)

    ChrTalk(    #34
        0x8,
        (
            "#253F#5PHeheh. Daaaamn.\x02\x03",

            "You're stickin' with it pretty well,\x01",
            "but after all that preachin' you did,\x01",
            "I was hoping you would.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x108,
        (
            "#077F#4PYou're doing well, too...\x02\x03",

            "#076FDAMN it, Walter! How could you allow\x01",
            "yourself to be dragged down into the\x01",
            "darkness with abilities like yours?!\x02\x03",

            "If you'd walked the path Master\x01",
            "showed us, you would have reached\x01",
            "the pinnacle of righteousness!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "#257F#5PYou really gonna stand there\x01",
            "and say that?\x02\x03",

            "#255FYou never actually figured out\x01",
            "why the old man died, did you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x108, 0xFFFFFF38, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #37
        0x108,
        "#073F#4PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "#253F#5PHeh heh.\x01",
            "That one got your attention.\x02\x03",

            "Tell you what. If by some damn\x01",
            "miracle you win, I'll fill you in on it.\x02\x03",

            "Your side of the bet is your life.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x8, 0)
    OP_0D()
    SetChrChipByIndex(0x8, 25)
    OP_99(0x8, 0x0, 0x2, 0x5DC)
    Sleep(500)
    PlayEffect(0x1, 0x1, 0x8, 100, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    ChrTalk(    #39
        0x108,
        (
            "#074F...\x02\x03",

            "#072FVery well. This life is worth\x01",
            "wagering for that.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 23)
    OP_0D()
    OP_99(0x108, 0x0, 0xF, 0x7D0)
    PlayEffect(0x1, 0x2, 0x108, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    Fade(500)
    OP_6D(0, 0, 7000, 0)
    OP_67(0, 4580, -10000, 0)
    OP_6B(4080, 0)
    OP_6C(33000, 0)
    OP_6E(243, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #40
        0x101,
        "#1020F#5P(ZIN!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        "#1043F#2P(No, Estelle. We can't stop this.)\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_6D(1000, 0, 10500, 0)
    OP_67(0, 6490, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(45000, 0)
    OP_6E(481, 0)
    ClearMapFlags(0x10)
    OP_0D()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_32C5():
        OP_6B(1650, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_32C5)
    OP_7C(0x0, 0x64, 0xBB8, 0x1388)

    ChrTalk(    #42 op#A op#5
        0x8,
        "#258F#30AKuuuuuuuuh!\x05\x02",
    )


    ChrTalk(    #43 op#A op#5
        0x108,
        "#077F#30AHaaaaaaaaa!\x05\x02",
    )

    Sleep(5000)
    OP_56(0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    SetChrPos(0xE, 40, 2000, 2090, 270)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 4)
    SetChrSubChip(0xE, 16)
    SetChrFlags(0xE, 0x2)
    OP_22(0x38E, 0x0, 0x64)
    OP_7D(0x0, 0xE, 0x32, 0x1F4)

    def lambda_335D():

        label("loc_335D")

        OP_99(0xFE, 0x10, 0x17, 0x1F40)
        OP_48()
        Jump("loc_335D")

    QueueWorkItem2(0xE, 1, lambda_335D)

    def lambda_3370():
        OP_8F(0xFE, 0x0, 0x4B0, 0x2580, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3370)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 14)

    def lambda_339F():
        OP_90(0xFE, 0xA8C, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_339F)

    def lambda_33BA():
        OP_90(0xFE, 0xFFFFF574, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_33BA)
    WaitChrThread(0x8, 0x1)
    OP_20(0x0)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_33E4():
        OP_96(0xFE, 0xFFFFF614, 0xFA, 0x2350, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_33E4)
    Sleep(100)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_340C():
        OP_96(0xFE, 0xAAA, 0xFA, 0x2224, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_340C)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    Sleep(1000)
    Sleep(1000)

    ChrTalk(    #44
        0x8,
        "#259F#1PThe hell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x108,
        "#073F#4PA Chakram? Impossible!\x02",
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, 40, 0, -3240, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 2)
    SetChrChipByIndex(0x9, 4)

    def lambda_34D6():
        OP_8F(0xFE, 0x1F4, 0x1F4, 0xFFFFF358, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_34D6)

    def lambda_34F1():
        OP_6D(310, 300, -800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_34F1)

    def lambda_3509():
        OP_67(0, 7680, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3509)

    def lambda_3521():
        OP_6B(1450, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3521)

    def lambda_3531():
        OP_6E(533, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_3531)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 2)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 65535)

    def lambda_3573():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3573)
    Sleep(50)

    def lambda_3586():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3586)
    Sleep(50)

    def lambda_3599():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3599)
    Sleep(50)

    def lambda_35AC():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_35AC)
    Sleep(50)

    def lambda_35BF():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_35BF)
    Sleep(600)
    OP_22(0xD8, 0x0, 0x64)
    WaitChrThread(0xE, 0x2)
    SetChrFlags(0xE, 0x80)
    WaitChrThread(0x101, 0x2)
    OP_99(0x9, 0x2, 0x8, 0x5DC)
    Sleep(1000)

    ChrTalk(    #46
        0x101,
        "#1004F#6PKilika?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x102,
        "#1044F#6PWhat in the world are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "#792F#2PThe battle to defend Zeiss has ended.\x02\x03",

            "#791FI left the receptionist's desk to Wong\x01",
            "and came to see how you were getting on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#1016F#6PSee how we were...uh...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3734")

    ChrTalk(    #50
        0x106,
        (
            "#055F#6PSo you got through the shadow\x01",
            "tower...by yourself. Whoa...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3822")

    label("loc_3734")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3790")

    ChrTalk(    #51
        0x103,
        (
            "#023F#6PWait. Kilika, you...got through the\x01",
            "shadow tower by yourself?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3822")

    label("loc_3790")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37E7")

    ChrTalk(    #52
        0x109,
        (
            "#1064F#6PHang on. You got through the\x01",
            "shadow tower by yourself?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3822")

    label("loc_37E7")


    ChrTalk(    #53
        0x102,
        (
            "#1044F#6PSo you climbed the shadow\x01",
            "tower by yourself?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3822")

    Fade(250)
    SetMapFlags(0x10)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 1)
    OP_0D()
    OP_1D(0x50)
    Sleep(1000)

    def lambda_384E():
        OP_6D(210, 0, 8800, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_384E)

    def lambda_3866():
        OP_67(0, 4650, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3866)

    def lambda_387E():
        OP_6B(2880, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_387E)

    def lambda_388E():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_388E)

    def lambda_389E():
        OP_6E(315, 4000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_389E)

    def lambda_38AE():
        OP_8E(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_38AE)

    def lambda_38C9():

        label("loc_38C9")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_38C9")

    QueueWorkItem2(0x108, 3, lambda_38C9)
    Sleep(500)

    def lambda_38DF():
        OP_8E(0xFE, 0x5DC, 0x0, 0x5BE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_38DF)
    Sleep(200)

    def lambda_38FF():
        OP_8E(0xFE, 0xFFFFFC18, 0x0, 0x456, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_38FF)
    Sleep(300)

    def lambda_391F():
        OP_8E(0xFE, 0x3E8, 0x0, 0x83E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_391F)
    WaitChrThread(0x102, 0x3)

    def lambda_393F():

        label("loc_393F")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_393F")

    QueueWorkItem2(0x102, 3, lambda_393F)
    WaitChrThread(0xF9, 0x3)

    def lambda_3955():

        label("loc_3955")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3955")

    QueueWorkItem2(0xF9, 3, lambda_3955)
    WaitChrThread(0x101, 0x3)

    def lambda_396B():

        label("loc_396B")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_396B")

    QueueWorkItem2(0x101, 3, lambda_396B)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0x8, 400)
    WaitChrThread(0x102, 0x0)
    OP_44(0x108, 0x1)
    OP_44(0x108, 0x3)
    OP_44(0x8, 0x1)
    OP_44(0x101, 0x3)
    OP_44(0x102, 0x3)
    OP_44(0xF9, 0x3)

    def lambda_39A5():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_39A5)
    WaitChrThread(0x8, 0x3)
    Sleep(500)

    ChrTalk(    #54
        0x108,
        "#072FKilika, really...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "#257FHeheh... Now THIS is like old times.\x02\x03",

            "#253FSo what is it, then? See how things\x01",
            "are going, maybe get some sweet,\x01",
            "sweet revenge for the old man?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "#791F#2PNot at all. The match was fairly\x01",
            "done, after all.\x02\x03",

            "Why do you believe I would tread\x01",
            "on Father's will?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        "#255F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x108,
        "#572FKilika...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x9,
        (
            "#792F#2PI am simply here because I wished\x01",
            "to say something to someone who\x01",
            "disappeared six years ago.\x02\x03",

            "#790FNothing more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        (
            "#251FSomething to say, huh?\x01",
            "All right, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x9,
        (
            "#793F#2PSo.\x02\x03",

            "#792FWalter.\x02\x03",

            "Why did you never see\x01",
            "me for who I am?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        "#255F#3SGh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x9,
        (
            "#793F#2PI don't know the details of what\x01",
            "Father told you.\x02\x03",

            "I cannot imagine it had anything to\x01",
            "do with...what we had, however.\x02\x03",

            "#790FEven more so with Zin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x108,
        "#073F?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        "#254F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x9,
        (
            "#792F#2PSo it really didn't. I thought so.\x02\x03",

            "#794FWalter, you are a fool.\x02\x03",

            "Did you really think Father was\x01",
            "the kind of man to hold such a\x01",
            "thing against you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "#254FIt... It had nothin' to do with the old\x01",
            "man. It was my problem to resolve.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x8, 400)
    Sleep(500)

    ChrTalk(    #68
        0x108,
        (
            "#072FNow, now wait a moment.\x02\x03",

            "#076FWalter! What did Master say to you?!\x02\x03",

            "What would it have to do with me?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#254FAh, shaddup. I got no obligation to\x01",
            "tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        (
            "#792F#2PYes, it has nothing to do with Zin.\x02\x03",

            "#790FBut it had everything to do with me.\x02\x03",

            "You disappearing without telling\x01",
            "me was negligent. At best.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x9, 400)

    ChrTalk(    #71
        0x8,
        "#254F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x9,
        (
            "#792F#2PI have no lingering attachment to\x01",
            "someone who could not see me as\x01",
            "myself.\x02\x03",

            "You are welcome to begone to\x01",
            "wherever you wish, or to slink back\x01",
            "to the nest of Ouroboros.\x02\x03",

            "#790FHowever you choose, I will deal with\x01",
            "you as a member of the Bracer Guild.\x01",
            "Nothing more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        "#250FHa...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #74
        0x8,
        "#252F#4SAAHHH-HAHAHA!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)
    OP_22(0x99, 0x0, 0x64)
    OP_23(0xEB)
    OP_1F(0x5A, 0x7D0)
    Fade(500)
    OP_6B(2700, 0)
    OP_82(0x0, 0x2)
    OP_82(0x81, 0x2)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x83, 0x2)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()
    Sleep(1000)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41C5")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4203")

    label("loc_41C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41EC")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4203")

    label("loc_41EC")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4203")

    Sleep(1000)

    def lambda_420E():
        OP_6D(-250, 200, 17430, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_420E)

    def lambda_4226():
        OP_67(0, 3660, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4226)

    def lambda_423E():
        OP_6B(3460, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_423E)

    def lambda_424E():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_424E)
    Sleep(50)

    def lambda_4261():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_4261)
    Sleep(50)
    OP_8C(0x9, 0, 400)
    WaitChrThread(0x101, 0x0)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3C)
    Sleep(500)
    OP_72(0x1, 0x20)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3C)
    Sleep(100)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x3C)
    Sleep(100)
    OP_72(0x3, 0x20)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3C)
    Sleep(100)
    OP_72(0x4, 0x20)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x3C)

    ChrTalk(    #75
        0x101,
        "#1004F#5PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x102,
        "#1042F#5PIt's reverting!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_1F(0x64, 0x7D0)
    Fade(1000)
    OP_6D(5030, 3860, 11650, 0)
    OP_67(0, 1590, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(45000, 0)
    OP_6E(363, 0)
    OP_0D()

    def lambda_4371():
        OP_6B(5500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4371)
    Sleep(500)
    OP_22(0x139, 0x0, 0x64)
    LoadEffect(0x2, "map\\mp049_02.eff")
    PlayEffect(0x2, 0x2, 0xFF, 0, 0, 6720, 0, 0, 0, 550, 550, 550, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    OP_82(0x80, 0x0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C3607   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_10C4 end

    def Function_8_43F7(): pass

    label("Function_8_43F7")

    OP_6C(760000, 6000)
    Return()

    # Function_8_43F7 end

    def Function_9_4401(): pass

    label("Function_9_4401")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_444D")
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x108, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x108, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x108, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_9_4401")

    label("loc_444D")

    Return()

    # Function_9_4401 end

    def Function_10_444E(): pass

    label("Function_10_444E")

    OP_98(0x0, 0xE)
    OP_98(0x1, 0x28, 0x7D0, 0x334A)
    OP_98(0x1, 0x28, 0xBB8, 0x3B1A)
    OP_98(0x1, 0x28, 0x1770, 0x4E20)
    OP_98(0x2, 0xFE, 0x4E20, 0x2)
    Return()

    # Function_10_444E end

    SaveToFile()

Try(main)
