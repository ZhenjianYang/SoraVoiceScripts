from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4281   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4281.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60035",
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
        'ED6_DT07/CH00050 ._CH',             # 05
        'ED6_DT07/CH00060 ._CH',             # 06
        'ED6_DT07/CH02020 ._CH',             # 07
        'ED6_DT07/CH01320 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH02010P._CP',             # 00
        'ED6_DT07/CH02090P._CP',             # 01
        'ED6_DT07/CH00010P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00070P._CP',             # 04
        'ED6_DT07/CH00050P._CP',             # 05
        'ED6_DT07/CH00060P._CP',             # 06
        'ED6_DT07/CH02020P._CP',             # 07
        'ED6_DT07/CH01320P._CP',             # 08
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
        "Function_0_232",          # 00, 0
        "Function_1_241",          # 01, 1
        "Function_2_276",          # 02, 2
    )


    def Function_0_232(): pass

    label("Function_0_232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_240")
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_240")

    Return()

    # Function_0_232 end

    def Function_1_241(): pass

    label("Function_1_241")

    OP_A1(0x11, 0x2)
    SetChrPos(0x11, 0, 0, 0, 0)
    SetChrFlags(0x11, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_26C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26C")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_241 end

    def Function_2_276(): pass

    label("Function_2_276")

    EventBegin(0x0)
    OP_6D(-40, 100, -60120, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
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
    SetChrPos(0xB, 640, 0, -72930, 0)
    SetChrPos(0xC, 2070, 0, -73010, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)

    def lambda_384():
        OP_8E(0xFE, 0xFFFFFA24, 0x0, 0xFFFEF502, 0x44C, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_384)

    def lambda_39F():
        OP_8E(0xFE, 0xFFFFFBD2, 0x0, 0xFFFEEF94, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_39F)

    def lambda_3BA():
        OP_8E(0xFE, 0x1A4, 0x0, 0xFFFEF390, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3BA)

    def lambda_3D5():
        OP_8E(0xFE, 0x50, 0x0, 0xFFFEF8CC, 0x578, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3D5)

    def lambda_3F0():
        OP_8E(0xFE, 0x488, 0x0, 0xFFFEF7A0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3F0)

    def lambda_40B():
        OP_8E(0xFE, 0xFFFFF74A, 0x0, 0xFFFEF7FA, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_40B)

    def lambda_426():
        OP_8E(0xFE, 0x280, 0x0, 0xFFFEEEFE, 0x44C, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_426)

    def lambda_441():
        OP_8E(0xFE, 0x816, 0x0, 0xFFFEF1D8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_441)

    def lambda_45C():
        OP_6D(-80, 0, -64650, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_45C)
    FadeToBright(1000, 0)
    WaitChrThread(0x0, 0x2)

    ChrTalk(    #0
        0x9,
        (
            "#170FThis elevator wasn't here before...\x02\x03",

            "Where'd it come from?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xC,
        (
            "#070FPerhaps it's a piece of Colonel\x01",
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
            "#090FYes...\x02\x03",

            "And that may have been the true\x01",
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
        "#000FThat's crazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xB,
        (
            "#030FHm... It's definitely a possibility.\x02\x03",

            "To violate a royal sanctuary\x01",
            "would certainly require an...\x01",
            "aggressive plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xA,
        (
            "#010FRegardless, we'll probably need\x01",
            "to use this to get underground.\x02\x03",

            "Let's test it to see if it works.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xA, 0xFFFFFC68, 0x0, 0xFFFEFCAA, 0xBB8, 0x0)
    OP_8E(0xA, 0xFFFFFDDA, 0x3C, 0xFFFEFE4E, 0xBB8, 0x0)
    OP_8E(0xA, 0xA, 0x64, 0xFFFF10B4, 0xBB8, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #6
        "\x07\x05Joshua began to inspect the elevator's control panel.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #7
        "\x07\x05Impatience quickly began to color his face.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)

    ChrTalk(    #8
        0x101,
        "#000FWhat is it?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #9
        0xA,
        (
            "#010FIt's locked with some type\x01",
            "of orbal energy.\x02\x03",

            "It looks like it won't work\x01",
            "unless we can find some special\x01",
            "type of quartz to put in it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_895():
        OP_8E(0xFE, 0xFFFFFF60, 0x0, 0xFFFF01E6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_895)

    ChrTalk(    #10
        0x101,
        "#000FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x105,
        (
            "#040FNo...\x01",
            "We've come so far...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #12
        0x9,
        (
            "#170FI'm going to go put the screws to\x01",
            "one of those Special Ops soldiers.\x02\x03",

            "One of them might have the key!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        "Yes, that sounds wisest.\x02",
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

    def lambda_9ED():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_9ED)

    ChrTalk(    #14
        0xF,
        "No, that won't be necessary.\x02",
    )

    CloseMessageWindow()

    def lambda_A21():
        OP_6D(-550, 0, -69950, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_A21)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_A67():

        label("loc_A67")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_A67")

    QueueWorkItem2(0x101, 1, lambda_A67)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_AAB():

        label("loc_AAB")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_AAB")

    QueueWorkItem2(0x105, 1, lambda_AAB)

    def lambda_ABC():

        label("loc_ABC")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_ABC")

    QueueWorkItem2(0x103, 1, lambda_ABC)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_B00():

        label("loc_B00")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_B00")

    QueueWorkItem2(0x8, 1, lambda_B00)

    def lambda_B11():

        label("loc_B11")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_B11")

    QueueWorkItem2(0x9, 1, lambda_B11)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_B55():

        label("loc_B55")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_B55")

    QueueWorkItem2(0xB, 1, lambda_B55)

    def lambda_B66():

        label("loc_B66")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_B66")

    QueueWorkItem2(0xC, 1, lambda_B66)
    WaitChrThread(0x0, 0x2)

    ChrTalk(    #15
        0x101,
        "#000FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xA,
        "#010FIt can't be...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        "#090FOh... Professor Russell?\x02",
    )

    CloseMessageWindow()

    def lambda_BC8():
        OP_6D(-400, 0, -68560, 2500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_BC8)

    def lambda_BE0():
        OP_8E(0xFE, 0xFFFFFD4E, 0x0, 0xFFFEE9EA, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_BE0)
    Sleep(200)
    SetChrFlags(0xA, 0x4)

    def lambda_C05():
        OP_8E(0xFE, 0xFFFFF484, 0x0, 0xFFFEF502, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_C05)

    def lambda_C20():

        label("loc_C20")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_C20")

    QueueWorkItem2(0xA, 1, lambda_C20)
    WaitChrThread(0x0, 0x2)

    ChrTalk(    #18
        0xF,
        (
            "#100FQueen Alicia, it has been quite\x01",
            "some time.\x02\x03",

            "#100FI'm glad to see Estelle and\x01",
            "Joshua are doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#000FH-Hold up... Professor, what\x01",
            "are you doing here?\x02\x03",

            "I thought the Intelligence Division\x01",
            "was after you in Zeiss...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D1E():

        label("loc_D1E")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_D1E")

    QueueWorkItem2(0xA, 1, lambda_D1E)

    ChrTalk(    #20
        0xA,
        (
            "#010FAnd on top of that, HOW did\x01",
            "you get here...?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D66():
        OP_6D(-20, 0, -71810, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_D66)
    Sleep(100)

    def lambda_D83():

        label("loc_D83")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_D83")

    QueueWorkItem2(0x101, 1, lambda_D83)
    Sleep(50)

    def lambda_D99():

        label("loc_D99")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_D99")

    QueueWorkItem2(0x105, 1, lambda_D99)

    def lambda_DAA():

        label("loc_DAA")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_DAA")

    QueueWorkItem2(0x103, 1, lambda_DAA)
    Sleep(50)

    def lambda_DC0():

        label("loc_DC0")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_DC0")

    QueueWorkItem2(0x8, 1, lambda_DC0)

    def lambda_DD1():

        label("loc_DD1")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_DD1")

    QueueWorkItem2(0x9, 1, lambda_DD1)
    Sleep(50)

    def lambda_DE7():

        label("loc_DE7")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_DE7")

    QueueWorkItem2(0xB, 1, lambda_DE7)

    def lambda_DF8():

        label("loc_DF8")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_DF8")

    QueueWorkItem2(0xC, 1, lambda_DF8)

    def lambda_E09():

        label("loc_E09")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_E09")

    QueueWorkItem2(0xF, 1, lambda_E09)

    ChrTalk(    #21
        0xE,
        (
            "Grandpaaaaa!\x01",
            "Where'd you go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xD,
        (
            "Hey! Enough with running all\x01",
            "over the place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xD,
        (
            "Is everyone in your family as\x01",
            "big a pain in the ass as you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xE,
        "B-But, Agate...\x02",
    )

    CloseMessageWindow()

    def lambda_EC4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_EC4)

    def lambda_ED6():
        OP_8E(0xFE, 0xFFFFFBA0, 0x0, 0xFFFEDB30, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_ED6)
    Sleep(600)

    def lambda_EF6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_EF6)

    def lambda_F08():
        OP_8E(0xFE, 0xE6, 0x0, 0xFFFEDC16, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_F08)

    ChrTalk(    #25
        0xE,
        "#060FOh...!\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)

    ChrTalk(    #26
        0x101,
        "#000FTita?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xA,
        "#010FI knew it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xE,
        "#060FEstelle! Joshua!\x02",
    )

    CloseMessageWindow()

    def lambda_F7B():
        OP_8E(0xFE, 0xFFFFF696, 0x0, 0xFFFEEF9E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_F7B)

    def lambda_F96():

        label("loc_F96")

        OP_8C(0xFE, 0, 0)
        OP_48()
        Jump("loc_F96")

    QueueWorkItem2(0xE, 1, lambda_F96)

    def lambda_FA7():
        OP_8E(0xFE, 0xFFFFF880, 0x0, 0xFFFEE922, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_FA7)

    def lambda_FC2():

        label("loc_FC2")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_FC2")

    QueueWorkItem2(0xD, 1, lambda_FC2)
    OP_6D(-460, 0, -68660, 2000)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)

    ChrTalk(    #29
        0x101,
        "#000FAwww, Tita...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xE,
        (
            "#060FThank goodness... I was hoping\x01",
            "I'd get to see you again...\x02\x03",

            "We heard at the guild that you\x01",
            "two were fighting at the castle.\x02\x03",

            "I'm so glad you're all right!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#000FTita...\x02",
    )

    CloseMessageWindow()

    def lambda_10CF():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_10CF)

    ChrTalk(    #32
        0xA,
        (
            "#010FThank you for being so concerned.\x02\x03",

            "It's good to see you well, Agate.\x02\x03",

            "But...what are you doing in\x01",
            "the royal city?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1159():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1159)

    def lambda_1167():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1167)

    def lambda_1175():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1175)

    def lambda_1183():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1183)

    def lambda_1191():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1191)

    def lambda_119F():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_119F)

    def lambda_11AD():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_11AD)

    def lambda_11BB():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_11BB)

    ChrTalk(    #33
        0xD,
        (
            "#050FWell, we hid out for a bit, but then\x01",
            "we happened upon a cargo freighter\x01",
            "bound for Grancel...\x02\x03",

            "And I figured, 'What the hell?'\x01",
            "The best place to hide is in plain\x01",
            "sight, after all.\x02\x03",

            "We used it to get here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#000FOh, okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xD,
        (
            "#050FSo, what brings your amateur\x01",
            "asses here?\x02\x03",

            "Me, I figured we could at least beat\x01",
            "up the remaining Special Ops guys...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xD, 0xFF)
    TurnDirection(0xD, 0x105, 400)

    ChrTalk(    #36
        0xD,
        "#050FHm? Wait, I know you...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xD, 400)

    def lambda_1367():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1367)

    def lambda_1375():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1375)

    def lambda_1383():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1383)

    def lambda_1391():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1391)

    ChrTalk(    #37
        0x105,
        (
            "#040FIt's been a while, Agate.\x02\x03",

            "Thank you for your efforts\x01",
            "at the lighthouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xD,
        (
            "#050FKloe, right?\x02\x03",

            "What's a student doing in a\x01",
            "place like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "#090FIt seems my granddaughter\x01",
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
            "#050FDon't worry about it.\x01",
            "S'all part of the job.\x02\x03",

            "So, what's up, granny? You work in\x01",
            "the castle? Did these numbskulls\x01",
            "rope you into helping them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "#170FY-You barbarian! Do you realize\x01",
            "to whom you're speaking!?\x02\x03",

            "You stand in the presence of\x01",
            "Queen Alicia of Liberl!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15B1():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_15B1)

    ChrTalk(    #42
        0xD,
        (
            "#050FHuh...?\x02\x03",

            "Y-You know, she does look\x01",
            "sorta familiar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xF,
        (
            "#100F*sigh* You really should loosen that\x01",
            "bandanna of yours, boy. It's obviously\x01",
            "squeezing your brain too tight.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xF, 400)

    ChrTalk(    #44
        0xD,
        "#050FSay that again, old man!\x02",
    )

    CloseMessageWindow()

    def lambda_169E():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_169E)
    TurnDirection(0xE, 0x105, 400)

    ChrTalk(    #45
        0xE,
        (
            "#060FQu-Queen?!\x02\x03",

            "S-So that means...this lady\x01",
            "would have to be...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xE, 400)

    ChrTalk(    #46
        0xA,
        (
            "#010FHer Majesty's granddaughter,\x01",
            "Princess Klaudia.\x02\x03",

            "We call her Kloe, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#000FKloe, meet the professor's\x01",
            "granddaughter, Tita.\x02\x03",

            "She's like our little sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x105,
        (
            "#040FI see... It's a pleasure to\x01",
            "meet you, Tita.\x02\x03",

            "I'd be happy if you'd also\x01",
            "call me Kloe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xE,
        (
            "#060FY-Yes, ma'am...\x02\x03",

            "I, I, I mean Kloe.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x103, 0xFFFFFE48, 0x0, 0xFFFEF494, 0x7D0, 0x0)
    TurnDirection(0x103, 0xE, 400)

    ChrTalk(    #50
        0x103,
        (
            "#020FAwwww...\x01",
            "What a little cutie pie.\x02\x03",

            "My name's Scherazard. I'm\x01",
            "Joshua and Estelle's mentor.\x02\x03",

            "You can just call me Schera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xE,
        "#060FO-Okay, Schera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xB,
        "#030FAnd you can call me Uncle Olivier...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#000FYou shaddup.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xA, 400)

    ChrTalk(    #54
        0xF,
        (
            "#100FAnyway, this elevator seems to\x01",
            "be giving you some trouble.\x02\x03",

            "What seems to be the problem,\x01",
            "and what in Aidios' name is\x01",
            "going on here?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_19D0():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_19D0)

    def lambda_19DE():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_19DE)

    ChrTalk(    #55
        0xA,
        "#010FWell...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #56
        (
            "\x07\x05Joshua briefly relayed the gist of Colonel\x01",
            "Richard's plan and told the professor about\x01",
            "the 'Shining Ring,' a.k.a. the Aureole.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #57
        0xD,
        (
            "#050FOh, come on... This is some kinda\x01",
            "joke, right? You're not serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xE,
        (
            "#060FI can't believe such a thing\x01",
            "would be buried here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xF,
        (
            "#100FHrm... So it's happened,\x01",
            "just as I was afraid of.\x02\x03",

            "So if we use this elevator, we\x01",
            "can get where we need to go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xA,
        (
            "#010FYes...but it has a special lock.\x02\x03",

            "Made of quartz, apparently...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 0, 400)

    ChrTalk(    #61
        0xF,
        (
            "#100FAhh, that.\x02\x03",

            "Let me have a look at it.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-470, 100, -63150, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(32000, 0)
    OP_6E(262, 0)
    SetChrPos(0xF, -230, 100, -61280, 0)
    SetChrPos(0xE, 630, 100, -61490, 327)
    SetChrPos(0x101, -20, 100, -62860, 0)
    SetChrPos(0xA, -1040, 100, -62820, 33)
    SetChrPos(0x8, -80, 0, -65250, 9)
    SetChrPos(0x9, 760, 0, -66280, 346)
    SetChrPos(0xD, 1100, 100, -63990, 334)
    SetChrPos(0x105, -840, 0, -67210, 339)
    SetChrPos(0xC, -2050, 0, -66600, 39)
    SetChrPos(0x103, -3290, 0, -67250, 44)
    SetChrPos(0xB, -1860, 0, -67840, 10)
    OP_0D()

    ChrTalk(    #62
        0xF,
        (
            "#100FThis is my own design.\x01",
            "It uses a card key.\x02\x03",

            "You can't undo the lock unless you\x01",
            "insert the card that's embedded with\x01",
            "the identical quartz.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #63
        (
            "\x07\x05The professor produced a small cable\x01",
            "and slid it into the card slot.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #64
        0xF,
        (
            "#100FHowever, this is an early model,\x01",
            "without any type of failsafe.\x02\x03",

            "So, if you feed it just the right\x01",
            "amount of orbal energy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        "#000FWoohoo! Nice going, Prof!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        "#010FI'm impressed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "#090FHa ha...\x01",
            "Why am I not surprised?\x02\x03",

            "Now, shall we descend?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 20, 0, -77690, 315)

    ChrTalk(    #68
        0x10,
        "W-We've got trouble!\x02",
    )

    CloseMessageWindow()

    def lambda_1F5E():

        label("loc_1F5E")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1F5E")

    QueueWorkItem2(0x101, 1, lambda_1F5E)

    def lambda_1F6F():

        label("loc_1F6F")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1F6F")

    QueueWorkItem2(0x105, 1, lambda_1F6F)

    def lambda_1F80():

        label("loc_1F80")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1F80")

    QueueWorkItem2(0x103, 1, lambda_1F80)

    def lambda_1F91():

        label("loc_1F91")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1F91")

    QueueWorkItem2(0x8, 1, lambda_1F91)

    def lambda_1FA2():

        label("loc_1FA2")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1FA2")

    QueueWorkItem2(0x9, 1, lambda_1FA2)

    def lambda_1FB3():

        label("loc_1FB3")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1FB3")

    QueueWorkItem2(0xB, 1, lambda_1FB3)

    def lambda_1FC4():

        label("loc_1FC4")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1FC4")

    QueueWorkItem2(0xC, 1, lambda_1FC4)

    def lambda_1FD5():

        label("loc_1FD5")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1FD5")

    QueueWorkItem2(0xF, 1, lambda_1FD5)

    def lambda_1FE6():

        label("loc_1FE6")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1FE6")

    QueueWorkItem2(0xE, 1, lambda_1FE6)

    def lambda_1FF7():

        label("loc_1FF7")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1FF7")

    QueueWorkItem2(0xD, 1, lambda_1FF7)

    def lambda_2008():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2008)

    def lambda_201A():
        OP_8E(0xFE, 0x1D6, 0x0, 0xFFFEF688, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_201A)
    OP_6D(-170, 0, -65530, 3000)

    ChrTalk(    #69
        0x9,
        "#170FWhat is it? Report!\x02",
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
        "#170FWhat?!\x02",
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
        "#170FOf all the damned times...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "#090FPerhaps I should make an appearance,\x01",
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

    def lambda_2208():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2208)

    def lambda_2216():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2216)

    def lambda_2224():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2224)

    def lambda_2232():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2232)

    def lambda_2240():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2240)

    def lambda_224E():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_224E)

    def lambda_225C():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_225C)

    ChrTalk(    #77
        0x105,
        "#040FGr-Grandmother...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        (
            "#090FI will go to the terrace on the roof\x01",
            "and address the arriving forces.\x02\x03",

            "Lieutenant Schwarz, make\x01",
            "your preparations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        "#170FB-But...what if you are attacked?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x8,
        (
            "#090FI believe in them.\x02\x03",

            "Misguided though they are, they\x01",
            "are still citizens of Liberl...\x02\x03",

            "If they see me, and hear my voice, I do\x01",
            "not believe that they will attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x9,
        "#170FYour Majesty...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #82
        0x8,
        (
            "#090FAll of you...\x02\x03",

            "It is with boundless regret that I\x01",
            "ask you to shoulder this burden...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#000FPlease, Your Majesty... You don't\x01",
            "need to say anything else.\x02\x03",

            "We'll do whatever it takes\x01",
            "to stop the colonel!\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x11, 0x2)
    SetChrPos(0x11, 0, 170000, 0, 0)
    SetChrFlags(0x11, 0x4)

    ChrTalk(    #84
        0xA,
        "#010FPlease, leave this to us.\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_11(0x0, 0x0, 0x0, 0x7530, 0x9C40, 0x0)
    SetMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x11, 0x0)
    OP_6A(0x11)
    OP_67(0, 4000, -10000, 0)
    OP_6B(2070, 0)
    OP_6C(65000, 0)
    OP_6E(554, 0)

    def lambda_2571():
        OP_67(0, 15000, -10000, 20000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2571)

    def lambda_2589():
        OP_6B(1280, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2589)

    def lambda_2599():
        OP_6C(600000, 20000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2599)

    def lambda_25A9():
        OP_6E(900, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_25A9)
    SetChrPos(0x101, 0, 0, 0, 0)
    ClearChrFlags(0xA, 0x4)
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0xA, 0x20)
    SetChrBattleFlags(0x105, 0x20)
    SetChrBattleFlags(0x103, 0x20)
    SetChrBattleFlags(0xB, 0x20)
    SetChrBattleFlags(0xE, 0x20)
    SetChrBattleFlags(0xD, 0x20)
    SetChrBattleFlags(0xC, 0x20)
    SetChrBattleFlags(0xF, 0x20)
    OP_89(0x101, -1370, 190100, 270, 258)
    OP_89(0xA, -1470, 190100, 1080, 286)
    OP_89(0x105, -390, 190100, -450, 9)
    OP_89(0x103, -1660, 190100, -1180, 246)
    OP_89(0xB, -850, 190100, -2020, 246)
    OP_89(0xE, 950, 190100, 440, 319)
    OP_89(0xD, 1300, 190100, -1220, 265)
    OP_89(0xC, 420, 190100, -2009, 155)
    OP_89(0xF, -70, 190100, 750, 9)
    FadeToBright(2000, 0)
    OP_8F(0x11, 0x0, 0x9C40, 0x0, 0x2710, 0x0)
    FadeToDark(2000, 0, -1)
    OP_8F(0x11, 0x0, 0x0, 0x0, 0x2710, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x3FB)
    NewScene("ED6_DT01/C4300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_276 end

    SaveToFile()

Try(main)
