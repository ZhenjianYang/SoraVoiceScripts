from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4241   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4241.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        'Queen Alicia',                         # 9
        '1st Lieutenant Schwarz',               # 10
        'Joshua',                               # 11
        'Olivier',                              # 12
        'Zin',                                  # 13
        'Agate',                                # 14
        'Tita',                                 # 15
        'Professor Russell',                    # 16
        'Royal Guardsman',                      # 17
        'Elevator',                             # 18
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
        'ED6_DT07/CH02010 ._CH',             # 00
        'ED6_DT07/CH02090 ._CH',             # 01
        'ED6_DT07/CH00010 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH00070 ._CH',             # 04
        'ED6_DT06/CH20053 ._CH',             # 05
        'ED6_DT07/CH00060 ._CH',             # 06
        'ED6_DT07/CH02020 ._CH',             # 07
        'ED6_DT07/CH01320 ._CH',             # 08
        'ED6_DT06/CH20141 ._CH',             # 09
        'ED6_DT07/CH00061 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH02010P._CP',             # 00
        'ED6_DT07/CH02090P._CP',             # 01
        'ED6_DT07/CH00010P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00070P._CP',             # 04
        'ED6_DT06/CH20053P._CP',             # 05
        'ED6_DT07/CH00060P._CP',             # 06
        'ED6_DT07/CH02020P._CP',             # 07
        'ED6_DT07/CH01320P._CP',             # 08
        'ED6_DT06/CH20141P._CP',             # 09
        'ED6_DT07/CH00061P._CP',             # 0A
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_242",          # 00, 0
        "Function_1_253",          # 01, 1
        "Function_2_278",          # 02, 2
    )


    def Function_0_242(): pass

    label("Function_0_242")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 2)
    Return()

    # Function_0_242 end

    def Function_1_253(): pass

    label("Function_1_253")

    OP_A1(0x11, 0x2)
    SetChrPos(0x11, 0, 0, 0, 0)
    SetChrFlags(0x11, 0x4)
    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_253 end

    def Function_2_278(): pass

    label("Function_2_278")

    EventBegin(0x0)
    OP_6D(-10, 0, -72410, 0)
    OP_67(0, 7490, -10000, 0)
    OP_6B(1830, 0)
    OP_6C(45000, 0)
    OP_6E(536, 0)
    SetChrPos(0x101, -1190, 0, -72040, 0)
    SetChrPos(0x105, -1330, 0, -73970, 0)
    SetChrPos(0x103, -30, 0, -72830, 0)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x105, 0x40)
    SetChrFlags(0x103, 0x40)
    SetChrPos(0x8, 80, 0, -70380, 0)
    SetChrPos(0x9, 890, 0, -71230, 0)
    SetChrPos(0xA, -2230, 0, -70590, 0)
    SetChrPos(0xB, 640, 0, -73900, 0)
    SetChrPos(0xC, 2070, 0, -73010, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)

    def lambda_386():
        OP_8E(0xFE, 0xFFFFFA24, 0x0, 0xFFFEF502, 0x44C, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_386)

    def lambda_3A1():
        OP_8E(0xFE, 0xFFFFFBD2, 0x0, 0xFFFEEF94, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3A1)

    def lambda_3BC():
        OP_8E(0xFE, 0x1A4, 0x0, 0xFFFEF390, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3BC)

    def lambda_3D7():
        OP_8E(0xFE, 0x50, 0x0, 0xFFFEF8CC, 0x578, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3D7)

    def lambda_3F2():
        OP_8E(0xFE, 0x488, 0x0, 0xFFFEF7A0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3F2)

    def lambda_40D():
        OP_8E(0xFE, 0xFFFFF74A, 0x0, 0xFFFEF7FA, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_40D)

    def lambda_428():
        OP_8E(0xFE, 0x280, 0x0, 0xFFFEEEFE, 0x44C, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_428)

    def lambda_443():
        OP_8E(0xFE, 0x816, 0x0, 0xFFFEF1D8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_443)

    def lambda_45E():
        OP_6D(110, 0, -66230, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_45E)
    FadeToBright(1000, 0)
    WaitChrThread(0x0, 0x2)
    Fade(500)
    OP_6D(110, 0, -66230, 0)
    OP_67(0, 7490, -10000, 0)
    OP_6B(1470, 0)
    OP_6C(45000, 0)
    OP_6E(536, 0)
    OP_0D()

    ChrTalk(    #0
        0x9,
        (
            "#173F#4PThis elevator wasn't here before...\x02\x03",

            "#177FWhere'd it come from?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xC,
        (
            "#072FPerhaps it's a piece of Colonel\x01",
            "Richard's new construction...\x02\x03",

            "In which case, it probably goes\x01",
            "down to where this 'Shining Ring'\x01",
            "is sealed away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "#093FYes...\x02\x03",

            "#094FAnd that may have been the true\x01",
            "goal behind the coup, from the\x01",
            "very beginning.\x02\x03",

            "They could never have built\x01",
            "such a thing without occupying\x01",
            "the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#580FThat's crazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xB,
        (
            "#035FHm... It's definitely a possibility.\x02\x03",

            "#030FIn any given country, a royal\x01",
            "sanctuary is generally regarded\x01",
            "as inviolate.\x02\x03",

            "To break that trust would require\x01",
            "quite an...aggressive plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xA,
        (
            "#012FRegardless, we'll probably need\x01",
            "to use this to get underground.\x02\x03",

            "Let's test it to see if it works.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7A5():
        OP_6D(-40, 0, -62650, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_7A5)
    OP_8E(0xA, 0xFFFFFC68, 0x0, 0xFFFEFCAA, 0xBB8, 0x0)
    OP_8E(0xA, 0xFFFFFDDA, 0x3C, 0xFFFEFE4E, 0xBB8, 0x0)
    OP_8E(0xA, 0xA, 0x64, 0xFFFF10B4, 0xBB8, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Joshua began to inspect the elevator's control panel.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_62(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0xA)

    ChrTalk(    #7
        0xA,
        "#014F#6P#4S!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#2P#004FWhat is it?\x02",
    )

    CloseMessageWindow()

    def lambda_8C2():
        OP_6D(110, 0, -66230, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8C2)
    TurnDirection(0xA, 0x101, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #9
        0xA,
        (
            "#012FIt's locked with some type\x01",
            "of orbal energy.\x02\x03",

            "It looks like it won't work\x01",
            "unless we can find some special\x01",
            "type of quartz to put in it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_976():
        OP_8E(0xFE, 0xFFFFFF60, 0x0, 0xFFFF01E6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_976)

    ChrTalk(    #10
        0x101,
        "#2P#005FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x105,
        (
            "#043FNo...\x01",
            "We've come so far...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #12
        0x9,
        (
            "#177F#4PI'm going to go put the screws to\x01",
            "one of those Special Ops soldiers.\x02\x03",

            "One of them might have the key!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        "#093FYes, that sounds wisest.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xF, 0x40)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    OP_9F(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xD, 20, 0, -77690, 0)
    SetChrPos(0xE, 20, 0, -77690, 0)
    SetChrPos(0xF, -1020, 0, -74230, 0)

    def lambda_AD9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_AD9)

    NpcTalk(    #14
        0xF,
        "Old Man's Voice",
        "#1PNo, that won't be necessary.\x02",
    )

    CloseMessageWindow()

    def lambda_B20():
        OP_6D(-550, 0, -69950, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_B20)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_B66():

        label("loc_B66")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_B66")

    QueueWorkItem2(0x101, 1, lambda_B66)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_BAA():

        label("loc_BAA")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_BAA")

    QueueWorkItem2(0x105, 1, lambda_BAA)

    def lambda_BBB():

        label("loc_BBB")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_BBB")

    QueueWorkItem2(0x103, 1, lambda_BBB)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_BFF():

        label("loc_BFF")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_BFF")

    QueueWorkItem2(0x8, 1, lambda_BFF)

    def lambda_C10():

        label("loc_C10")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_C10")

    QueueWorkItem2(0x9, 1, lambda_C10)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_C54():

        label("loc_C54")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_C54")

    QueueWorkItem2(0xB, 1, lambda_C54)

    def lambda_C65():

        label("loc_C65")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_C65")

    QueueWorkItem2(0xC, 1, lambda_C65)
    WaitChrThread(0x0, 0x2)

    ChrTalk(    #15
        0x101,
        "#004FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xA,
        "#014FIt can't be...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        "#097FOh... Professor Russell?\x02",
    )

    CloseMessageWindow()

    def lambda_CC7():
        OP_6D(-400, 0, -68560, 2500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_CC7)

    def lambda_CDF():
        OP_8E(0xFE, 0xFFFFFD4E, 0x0, 0xFFFEE9EA, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_CDF)
    Sleep(200)
    SetChrFlags(0xA, 0x4)

    def lambda_D04():
        OP_8E(0xFE, 0xFFFFF484, 0x0, 0xFFFEF502, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D04)

    def lambda_D1F():

        label("loc_D1F")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_D1F")

    QueueWorkItem2(0xA, 1, lambda_D1F)
    WaitChrThread(0x0, 0x2)

    ChrTalk(    #18
        0xF,
        (
            "#101FQueen Alicia, it has been quite\x01",
            "some time.\x02\x03",

            "I'm glad to see Estelle and\x01",
            "Joshua are doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#004F#6PH-Hold up... Professor, what\x01",
            "are you doing here?\x02\x03",

            "I thought the Intelligence Division\x01",
            "was after you in Zeiss...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E1B():

        label("loc_E1B")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_E1B")

    QueueWorkItem2(0xA, 1, lambda_E1B)

    ChrTalk(    #20
        0xA,
        (
            "#014F#5PAnd on top of that, HOW did\x01",
            "you get here...?\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xE, -900, 0, -77820, 0)

    NpcTalk(    #21
        0xE,
        "Girl's Voice",
        (
            "#1PGrandpaaaaa!\x01",
            "Where'd you go?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EA9():
        OP_6D(-20, 0, -71810, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EA9)
    OP_44(0xA, 0xFF)
    OP_8C(0xA, 180, 400)
    Sleep(100)

    def lambda_ED1():

        label("loc_ED1")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_ED1")

    QueueWorkItem2(0x101, 1, lambda_ED1)
    Sleep(50)

    def lambda_EE7():

        label("loc_EE7")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_EE7")

    QueueWorkItem2(0x105, 1, lambda_EE7)

    def lambda_EF8():

        label("loc_EF8")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_EF8")

    QueueWorkItem2(0x103, 1, lambda_EF8)
    Sleep(50)

    def lambda_F0E():

        label("loc_F0E")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_F0E")

    QueueWorkItem2(0x8, 1, lambda_F0E)

    def lambda_F1F():

        label("loc_F1F")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_F1F")

    QueueWorkItem2(0x9, 1, lambda_F1F)
    Sleep(50)

    def lambda_F35():

        label("loc_F35")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_F35")

    QueueWorkItem2(0xB, 1, lambda_F35)

    def lambda_F46():

        label("loc_F46")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_F46")

    QueueWorkItem2(0xC, 1, lambda_F46)

    def lambda_F57():

        label("loc_F57")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_F57")

    QueueWorkItem2(0xF, 1, lambda_F57)
    WaitChrThread(0x101, 0x2)
    SetChrPos(0xD, 360, 0, -77890, 0)

    NpcTalk(    #22
        0xD,
        "Young Man's Voice",
        (
            "#1PHey! Enough with running all\x01",
            "over the place!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #23
        0xD,
        "Young Man's Voice",
        (
            "#1PIs everyone in your family as\x01",
            "big a pain in the ass as you?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #24
        0xE,
        "Girl's Voice",
        "#1PB-But, Agate...\x02",
    )

    CloseMessageWindow()

    def lambda_1040():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1040)

    def lambda_1052():
        OP_8E(0xFE, 0xFFFFFBA0, 0x0, 0xFFFEDC16, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1052)
    Sleep(600)

    def lambda_1072():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1072)

    def lambda_1084():
        OP_8E(0xFE, 0xE6, 0x0, 0xFFFEDB30, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1084)
    OP_31(0x5, 0x0, 0x22)
    OP_B5(0x5, 0x0)
    OP_B5(0x5, 0x1)
    OP_B5(0x5, 0x2)
    OP_B5(0x5, 0x3)
    OP_B5(0x5, 0x5)
    OP_B5(0x5, 0x4)
    OP_41(0x5, 0x9A)
    OP_41(0x5, 0xF6)
    OP_41(0x5, 0x114)
    OP_41(0x5, 0x260, 0x0)
    OP_41(0x5, 0x259, 0x1)
    OP_41(0x5, 0x262, 0x2)
    OP_41(0x5, 0x26E, 0x3)
    OP_41(0x5, 0x283, 0x5)
    OP_35(0x5, 0xC8)
    OP_35(0x5, 0xC9)
    OP_35(0x5, 0xCA)
    OP_35(0x5, 0xCB)
    OP_36(0x5, 0xFF)
    OP_36(0x5, 0x100)
    OP_31(0x6, 0x0, 0x20)
    OP_B5(0x6, 0x0)
    OP_B5(0x6, 0x1)
    OP_B5(0x6, 0x5)
    OP_B5(0x6, 0x4)
    OP_B5(0x6, 0x3)
    OP_B5(0x6, 0x2)
    OP_41(0x6, 0xB8)
    OP_41(0x6, 0xF6)
    OP_41(0x6, 0x114)
    OP_41(0x6, 0x2C9, 0x0)
    OP_41(0x6, 0x281, 0x1)
    OP_41(0x6, 0x25F, 0x5)
    OP_41(0x6, 0x26C, 0x4)
    OP_41(0x6, 0x271, 0x3)
    OP_41(0x6, 0x259, 0x2)
    OP_35(0x6, 0xD2)
    OP_35(0x6, 0xD3)
    OP_36(0x6, 0x104)
    WaitChrThread(0xE, 0x2)

    ChrTalk(    #25
        0xE,
        "#064FOh...!\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)

    ChrTalk(    #26
        0x101,
        "#004FTita?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xA,
        "#010FI knew it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xE,
        "#067FEstelle! Joshua!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xE, 10)

    def lambda_11AE():
        OP_8E(0xFE, 0xFFFFF79A, 0x0, 0xFFFEED32, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_11AE)

    def lambda_11C9():

        label("loc_11C9")

        OP_8C(0xFE, 0, 0)
        OP_48()
        Jump("loc_11C9")

    QueueWorkItem2(0xE, 1, lambda_11C9)

    def lambda_11DA():
        OP_8E(0xFE, 0xFFFFF880, 0x0, 0xFFFEE9AE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_11DA)

    def lambda_11F5():

        label("loc_11F5")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_11F5")

    QueueWorkItem2(0xD, 1, lambda_11F5)

    def lambda_1206():
        OP_6D(-460, 0, -68660, 2000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1206)

    def lambda_121E():
        OP_8E(0xFE, 0xFFFFF6FA, 0x0, 0xFFFEEEF4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_121E)

    def lambda_1239():

        label("loc_1239")

        OP_8C(0xFE, 180, 0)
        OP_48()
        Jump("loc_1239")

    QueueWorkItem2(0x101, 1, lambda_1239)
    WaitChrThread(0xE, 0x2)
    SetChrChipByIndex(0xE, 9)
    SetChrSubChip(0xE, 0)
    SetChrFlags(0xE, 0x20)

    def lambda_125E():
        OP_94(0x1, 0xFE, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_125E)
    OP_94(0x1, 0x101, 0xB4, 0x1F4, 0x7D0, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)

    ChrTalk(    #29
        0x101,
        "#506F#5PAwww, Tita...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xE,
        (
            "#562F#2PThank goodness... I was hoping\x01",
            "I'd get to see you again...\x02\x03",

            "We heard at the guild that you\x01",
            "two were fighting at the castle.\x02\x03",

            "#069FI'm so glad you're all right!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#008F#5PTita...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xA,
        (
            "#019F#5PThank you for being so concerned.\x02\x03",

            "#010FIt's good to see you well, Agate.\x02\x03",

            "But...what are you doing in\x01",
            "the royal city?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1400():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1400)

    def lambda_140E():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_140E)

    def lambda_141C():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_141C)

    def lambda_142A():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_142A)

    def lambda_1438():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1438)

    def lambda_1446():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1446)

    def lambda_1454():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1454)

    ChrTalk(    #33
        0xD,
        (
            "#051FWell, we hid out for a bit, but then\x01",
            "we happened upon a cargo freighter\x01",
            "bound for Grancel...\x02\x03",

            "And I figured, 'What the hell?'\x01",
            "The best place to hide is in plain\x01",
            "sight, after all.\x02\x03",

            "Once we got the lowdown from Elnan,\x01",
            "we came straight to the castle.\x02\x03",

            "Oh, right... Got something\x01",
            "for you from him.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B8")
    Sleep(100)
    OP_AF(0x63, 0x4B)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_28(0x4C, 0x4, 0x10)
    OP_28(0x4C, 0x4, 0x20)

    label("loc_15B8")

    OP_28(0x4D, 0x4, 0x10)
    OP_28(0x4D, 0x1, 0x100)
    Sleep(100)
    OP_AF(0x63, 0x4D)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_28(0x4E, 0x4, 0x10)
    OP_28(0x4E, 0x4, 0x20)

    ChrTalk(    #34
        0x101,
        (
            "#004F#5PI-Is this okay? I mean, we\x01",
            "haven't reported in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xD,
        (
            "#053FLooks like he got filled in on\x01",
            "the general gist of things from\x01",
            "a Guardsman messenger.\x02\x03",

            "#050FSo, what brings your amateur\x01",
            "asses here?\x02\x03",

            "Me, I figured we could at least beat\x01",
            "up the remaining Special Ops guys...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_44(0xD, 0xFF)
    TurnDirection(0xD, 0x105, 400)

    ChrTalk(    #36
        0xD,
        "#052FHm? Wait, I know you...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xD, 400)

    def lambda_174C():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_174C)

    def lambda_175A():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_175A)

    def lambda_1768():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1768)
    SetChrChipByIndex(0xE, 6)
    SetChrSubChip(0xE, 0)
    ClearChrFlags(0xE, 0x20)
    OP_94(0x1, 0xE, 0xB4, 0xC8, 0x3E8, 0x0)

    def lambda_1794():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1794)

    ChrTalk(    #37
        0x105,
        (
            "#041F#5PIt's been a while, Agate.\x02\x03",

            "Thank you for your efforts\x01",
            "at the lighthouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xD,
        (
            "#052FKloe, right?\x02\x03",

            "What's a student doing in a\x01",
            "place like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "#090F#6PIt seems my granddaughter\x01",
            "is in your debt.\x02\x03",

            "Which means that I also\x01",
            "owe you my thanks.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x8, 400)

    ChrTalk(    #40
        0xD,
        (
            "#051FDon't worry about it.\x01",
            "S'all part of the job.\x02\x03",

            "So, what's up, granny? You work in\x01",
            "the castle? Did these numbskulls\x01",
            "rope you into helping them?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #41
        0x9,
        (
            "#177F#4PY-You barbarian!\x02\x03",

            "#177FDo you realize to whom\x01",
            "you're speaking!?\x02\x03",

            "You stand in the presence of\x01",
            "Queen Alicia of Liberl!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_19F0():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_19F0)

    ChrTalk(    #42
        0xD,
        (
            "#055FHuh...?\x02\x03",

            "Y-You know, she does look\x01",
            "sorta familiar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xF,
        (
            "#104F#2P*sigh* You really should loosen that\x01",
            "bandanna of yours, boy. It's obviously\x01",
            "squeezing your brain too tight.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xF, 400)

    ChrTalk(    #44
        0xD,
        "#054F#1PSay that again, old man!\x02",
    )

    CloseMessageWindow()

    def lambda_1AE3():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1AE3)
    OP_62(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xE, 0x105, 400)

    ChrTalk(    #45
        0xE,
        (
            "#065F#1PQu-Queen?!\x02\x03",

            "S-So that means...this lady\x01",
            "would have to be...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xE, 400)

    ChrTalk(    #46
        0xA,
        (
            "#010F#5PHer Majesty's granddaughter,\x01",
            "Princess Klaudia.\x02\x03",

            "We call her Kloe, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#001F#1PKloe, meet the professor's\x01",
            "granddaughter, Tita.\x02\x03",

            "She's like our little sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x105,
        (
            "#048F#2PI see... It's a pleasure to\x01",
            "meet you, Tita.\x02\x03",

            "#041FI'd be happy if you'd also\x01",
            "call me Kloe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xE,
        (
            "#067F#1PY-Yes, ma'am...\x02\x03",

            "I, I, I mean Kloe.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x103, 0xFFFFFE48, 0x0, 0xFFFEF494, 0x7D0, 0x0)
    TurnDirection(0x103, 0xE, 400)

    ChrTalk(    #50
        0x103,
        (
            "#023FAwwww...\x01",
            "What a little cutie pie.\x02\x03",

            "#021FMy name's Scherazard. I'm\x01",
            "Joshua and Estelle's mentor.\x02\x03",

            "You can just call me Schera.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x103, 400)

    ChrTalk(    #51
        0xE,
        "#066F#1PO-Okay, Schera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xB,
        "#031FAnd you can call me Uncle Olivier...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#509F#1PYou shaddup.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xA, 400)

    ChrTalk(    #54
        0xF,
        (
            "#102FAnyway, this elevator seems to\x01",
            "be giving you some trouble.\x02\x03",

            "What seems to be the problem,\x01",
            "and what in Aidios' name is\x01",
            "going on here?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1E4D():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1E4D)

    def lambda_1E5B():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1E5B)

    def lambda_1E69():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E69)
    OP_8C(0xA, 180, 400)

    ChrTalk(    #55
        0xA,
        "#013F#1PWell...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #56
        (
            "\x07\x05Joshua briefly relayed the gist of Colonel Richard's plan and told the\x01",
            "professor about the 'Shining Ring,' a.k.a. the Aureole.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #57
        0xD,
        (
            "#057FOh, come on... This is some kinda\x01",
            "joke, right? You're not serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xE,
        (
            "#065F#2PI can't believe such a thing\x01",
            "would be buried here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xF,
        (
            "#104FHrm... And now it's happened,\x01",
            "just as I was afraid of.\x02\x03",

            "#102FSo if we use this elevator, we\x01",
            "can get where we need to go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xA,
        (
            "#012F#1PYes...but it has a special lock.\x02\x03",

            "Made of quartz, apparently...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 0, 400)

    ChrTalk(    #61
        0xF,
        (
            "#103FAhh, that.\x02\x03",

            "Let me have a look at it.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-470, 100, -63150, 0)
    OP_67(0, 6860, -10000, 0)
    OP_6B(1470, 0)
    OP_6C(32000, 0)
    OP_6E(536, 0)
    SetChrPos(0xF, -230, 100, -61280, 0)
    SetChrPos(0xE, 630, 100, -61490, 327)
    SetChrPos(0x101, -20, 100, -62860, 0)
    SetChrPos(0xA, -1040, 100, -62820, 33)
    SetChrPos(0x8, -80, 0, -65250, 0)
    SetChrPos(0x9, 760, 0, -66280, 346)
    SetChrPos(0xD, 1100, 100, -63990, 334)
    SetChrPos(0x105, -840, 0, -67210, 339)
    SetChrPos(0xC, -2050, 0, -66600, 39)
    SetChrPos(0x103, -3290, 0, -67250, 44)
    SetChrPos(0xB, -1860, 0, -67840, 10)
    OP_0D()
    Sleep(500)

    ChrTalk(    #62
        0xF,
        (
            "#100F#6PThis is my own design.\x01",
            "It uses a card key.\x02\x03",

            "You can't undo the lock unless you\x01",
            "insert the card that's embedded with\x01",
            "the identical quartz.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #63
        "\x07\x05The professor produced a small cable and slid it into the card slot.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #64
        0xF,
        (
            "#102F#6PHowever, this is an early model,\x01",
            "without any type of failsafe.\x02\x03",

            "So, if you feed it just the right\x01",
            "amount of orbal energy...\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xB7, 0x0, 0x64)
    OP_71(0x1, 0x4)
    Sleep(1500)

    ChrTalk(    #65
        0x101,
        "#001F#6PWoohoo! Nice going, Prof!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        "#010F#6PI'm impressed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "#091FHa ha...\x01",
            "Why am I not surprised?\x02\x03",

            "#090FNow, shall we descend?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 20, 0, -77690, 315)

    NpcTalk(    #68
        0x10,
        "Young Man's Voice",
        "W-We've got trouble!\x02",
    )

    CloseMessageWindow()

    def lambda_2462():

        label("loc_2462")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2462")

    QueueWorkItem2(0xA, 1, lambda_2462)

    def lambda_2473():

        label("loc_2473")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2473")

    QueueWorkItem2(0x101, 1, lambda_2473)

    def lambda_2484():

        label("loc_2484")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2484")

    QueueWorkItem2(0x105, 1, lambda_2484)

    def lambda_2495():

        label("loc_2495")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2495")

    QueueWorkItem2(0x103, 1, lambda_2495)

    def lambda_24A6():

        label("loc_24A6")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_24A6")

    QueueWorkItem2(0x8, 1, lambda_24A6)

    def lambda_24B7():

        label("loc_24B7")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_24B7")

    QueueWorkItem2(0x9, 1, lambda_24B7)

    def lambda_24C8():

        label("loc_24C8")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_24C8")

    QueueWorkItem2(0xB, 1, lambda_24C8)

    def lambda_24D9():

        label("loc_24D9")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_24D9")

    QueueWorkItem2(0xC, 1, lambda_24D9)

    def lambda_24EA():

        label("loc_24EA")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_24EA")

    QueueWorkItem2(0xF, 1, lambda_24EA)

    def lambda_24FB():

        label("loc_24FB")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_24FB")

    QueueWorkItem2(0xE, 1, lambda_24FB)

    def lambda_250C():

        label("loc_250C")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_250C")

    QueueWorkItem2(0xD, 1, lambda_250C)

    def lambda_251D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_251D)

    def lambda_252F():
        OP_8E(0xFE, 0x1D6, 0x0, 0xFFFEF688, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_252F)
    OP_6D(-170, 0, -65530, 1500)

    ChrTalk(    #69
        0x9,
        "#3P#173FWhat is it? Report!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x10,
        (
            "A division of the regular army has\x01",
            "arrived at Grancel's main gate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10,
        (
            "It looks like they're being\x01",
            "led by an officer of the\x01",
            "Intelligence Division!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x9,
        "#3P#178FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10,
        (
            "And three military patrol ships\x01",
            "are approaching from the lake!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10,
        "Y-Your orders, ma'am?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x9,
        "#3P#177FOf all the damned times...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "#3P#094FPerhaps I should make an appearance,\x01",
            "in order to persuade them...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xC, 0xFF)

    def lambda_2729():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2729)

    def lambda_2737():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2737)

    def lambda_2745():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2745)

    def lambda_2753():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2753)

    def lambda_2761():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2761)

    def lambda_276F():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_276F)

    def lambda_277D():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_277D)

    def lambda_278B():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_278B)

    ChrTalk(    #77
        0x105,
        "#043FGr-Grandmother...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        (
            "#3P#092FI will go to the terrace on the roof\x01",
            "and address the arriving forces.\x02\x03",

            "Lieutenant Schwarz, make\x01",
            "your preparations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        "#173FB-But...what if you are attacked?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x8,
        (
            "#3P#094FI believe in them.\x02\x03",

            "Misguided though they are, they\x01",
            "are still citizens of Liberl...\x02\x03",

            "#090FIf they see me, and hear my voice, I do\x01",
            "not believe that they will attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x9,
        "#175FYour Majesty...\x02",
    )

    CloseMessageWindow()

    def lambda_292F():
        OP_6D(-470, 100, -63150, 1200)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_292F)
    TurnDirection(0x8, 0x101, 400)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #82
        0x8,
        (
            "#093FAll of you...\x02\x03",

            "It is with boundless regret that I\x01",
            "ask you to shoulder this burden...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#006F#6PPlease, Your Majesty... You don't\x01",
            "need to say anything else.\x02\x03",

            "We'll do whatever it takes\x01",
            "to stop the colonel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xA,
        "#010F#6PPlease, leave this to us.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(140, 100, -61920, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(45000, 0)
    OP_6E(259, 0)
    OP_A1(0x11, 0x0)
    SetChrPos(0x11, 0, 0, -62000, 0)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x40)
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0xA, 0x20)
    SetChrBattleFlags(0x105, 0x20)
    SetChrBattleFlags(0x103, 0x20)
    SetChrBattleFlags(0xB, 0x20)
    SetChrBattleFlags(0xE, 0x20)
    SetChrBattleFlags(0xD, 0x20)
    SetChrBattleFlags(0xC, 0x20)
    SetChrBattleFlags(0xF, 0x20)
    OP_89(0x101, -1370, 10000, -61730, 180)
    OP_89(0xA, -1470, 10000, -60920, 180)
    OP_89(0x105, -390, 10000, -62450, 180)
    OP_89(0x103, -1660, 10000, -63180, 180)
    OP_89(0xB, -850, 10000, -64019, 180)
    OP_89(0xE, 950, 10000, -61560, 180)
    OP_89(0xC, 1300, 10000, -63220, 180)
    OP_89(0xD, 420, 10000, -64010, 180)
    OP_89(0xF, -70, 10000, -61150, 0)
    OP_0D()
    Sleep(500)
    OP_22(0xF7, 0x0, 0x64)
    OP_22(0x68, 0x1, 0x64)

    def lambda_2B91():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2B91)
    Sleep(300)

    def lambda_2BB1():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2BB1)
    Sleep(500)

    def lambda_2BD1():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2BD1)
    Sleep(800)

    def lambda_2BF1():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2BF1)
    Sleep(1000)

    def lambda_2C11():
        OP_8F(0xFE, 0x0, 0xFFFF63C0, 0xFFFF15A0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2C11)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x11, 0xFF)
    OP_A1(0x11, 0x2)
    SetChrPos(0x11, 0, 170000, 0, 0)
    SetChrFlags(0x11, 0x4)
    OP_11(0x0, 0x0, 0x0, 0x7530, 0x9C40, 0x0)
    SetMapFlags(0x10)
    OP_48()
    OP_69(0x11, 0x0)
    OP_6A(0x11)
    OP_67(0, 4000, -10000, 0)
    OP_6B(2070, 0)
    OP_6C(65000, 0)
    OP_6E(554, 0)
    OP_67(0, 3080, -10000, 0)
    OP_6B(2180, 0)
    OP_6C(35000, 0)
    OP_6E(450, 0)

    def lambda_2CCE():
        OP_67(0, 11400, -10000, 20000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2CCE)

    def lambda_2CE6():
        OP_6B(1310, 20000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CE6)

    def lambda_2CF6():
        OP_6C(55000, 20000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2CF6)

    def lambda_2D06():
        OP_6E(776, 20000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2D06)
    SetChrPos(0x101, 0, 0, 0, 0)
    ClearChrFlags(0xA, 0x4)
    OP_89(0x101, -1370, 190100, 270, 270)
    OP_89(0xA, -1470, 190100, 1080, 270)
    OP_89(0x105, -390, 190100, -450, 270)
    OP_89(0x103, -1660, 190100, -1180, 270)
    OP_89(0xB, -850, 190100, -2020, 270)
    OP_89(0xE, 950, 190100, 440, 270)
    OP_89(0xC, 1300, 190100, -1220, 270)
    OP_89(0xD, 420, 190100, -2009, 270)
    OP_89(0xF, -70, 190100, 750, 270)
    FadeToBright(2000, 0)
    OP_8F(0x11, 0x0, 0xEA60, 0x0, 0x1F40, 0x0)
    FadeToDark(2000, 0, -1)

    def lambda_2DEC():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2DEC)
    OP_24(0x68, 0x5A)
    Sleep(400)
    OP_24(0x68, 0x55)
    Sleep(400)
    OP_24(0x68, 0x50)
    Sleep(400)
    OP_24(0x68, 0x4B)
    Sleep(400)
    OP_24(0x68, 0x46)
    Sleep(400)
    OP_24(0x68, 0x41)
    Sleep(400)
    OP_24(0x68, 0x3C)
    Sleep(400)
    OP_23(0x68)
    OP_0D()
    ClearMapFlags(0x2000000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/C4300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_278 end

    SaveToFile()

Try(main)
