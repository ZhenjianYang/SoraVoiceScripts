from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3133   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3133.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        'Tita',                                 # 9
        'Agate',                                # 10
        'Professor Russell',                    # 11
        'Erika',                                # 12
        'Dan',                                  # 13
        'Factory Chief Murdock',                # 14
        'Object',                               # 15
        'Coffee',                               # 16
        'Coffee',                               # 17
        'Coffee',                               # 18
        'Coffee',                               # 19
        'Pot',                                  # 20
        'Orbal Gear',                           # 21
        'Dinner',                               # 22
        'Dinner',                               # 23
        'Dinner',                               # 24
        'Crockery',                             # 25
        'Crockery',                             # 26
        'Crockery',                             # 27
        'Crockery',                             # 28
        'Target Camera',                        # 29
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
        'ED6_DT07/CH00060 ._CH',             # 00
        'ED6_DT07/CH00050 ._CH',             # 01
        'ED6_DT07/CH02020 ._CH',             # 02
        'ED6_DT07/CH00061 ._CH',             # 03
        'ED6_DT07/CH00063 ._CH',             # 04
        'ED6_DT07/CH02023 ._CH',             # 05
        'ED6_DT27/CH03970 ._CH',             # 06
        'ED6_DT27/CH03980 ._CH',             # 07
        'ED6_DT26/CH20696 ._CH',             # 08
        'ED6_DT26/CH20697 ._CH',             # 09
        'ED6_DT06/CH20021 ._CH',             # 0A
        'ED6_DT06/CH20020 ._CH',             # 0B
        'ED6_DT07/CH02620 ._CH',             # 0C
        'ED6_DT27/CH04220 ._CH',             # 0D
        'ED6_DT26/CH20205 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH00060P._CP',             # 00
        'ED6_DT07/CH00050P._CP',             # 01
        'ED6_DT07/CH02020P._CP',             # 02
        'ED6_DT07/CH00061P._CP',             # 03
        'ED6_DT07/CH00063P._CP',             # 04
        'ED6_DT07/CH02023P._CP',             # 05
        'ED6_DT27/CH03970P._CP',             # 06
        'ED6_DT27/CH03980P._CP',             # 07
        'ED6_DT26/CH20696P._CP',             # 08
        'ED6_DT26/CH20697P._CP',             # 09
        'ED6_DT06/CH20021P._CP',             # 0A
        'ED6_DT06/CH20020P._CP',             # 0B
        'ED6_DT07/CH02620P._CP',             # 0C
        'ED6_DT27/CH04220P._CP',             # 0D
        'ED6_DT26/CH20205P._CP',             # 0E
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 1179658,
        ChipIndex           = 0xA,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1572875,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1572875,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1572875,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1572875,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1703947,
        ChipIndex           = 0xB,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 393227,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 131083,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 458763,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 917515,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 917515,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 917515,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 917515,
        ChipIndex           = 0xB,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_3C2",          # 00, 0
        "Function_1_420",          # 01, 1
        "Function_2_421",          # 02, 2
        "Function_3_19F4",         # 03, 3
        "Function_4_1A87",         # 04, 4
        "Function_5_1AFA",         # 05, 5
        "Function_6_1C2A",         # 06, 6
        "Function_7_1CB2",         # 07, 7
        "Function_8_1D8A",         # 08, 8
        "Function_9_211B",         # 09, 9
        "Function_10_2184",        # 0A, 10
        "Function_11_28BD",        # 0B, 11
        "Function_12_296A",        # 0C, 12
        "Function_13_2B69",        # 0D, 13
        "Function_14_2B93",        # 0E, 14
    )


    def Function_0_3C2(): pass

    label("Function_0_3C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_3E4")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 10)
    Jump("loc_3F7")

    label("loc_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_3F7")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_3F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_41F")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 12)

    label("loc_41F")

    Return()

    # Function_0_3C2 end

    def Function_1_420(): pass

    label("Function_1_420")

    Return()

    # Function_1_420 end

    def Function_2_421(): pass

    label("Function_2_421")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-580, 0, 1360, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x107, -2460, -500, -5500, 0)
    SetChrPos(0x12, -2460, -500, -5500, 0)
    SetChrPos(0x13, -1560, -500, -5500, 0)
    SetChrPos(0x14, -1560, -500, -5500, 0)
    OP_9F(0x107, 0xFF, 0xE1, 0xE1, 0x0, 0x0)
    OP_9F(0x12, 0xFF, 0xE1, 0xE1, 0x0, 0x0)
    OP_9F(0x13, 0xFF, 0xE1, 0xE1, 0x0, 0x0)
    OP_9F(0x14, 0xFF, 0xE1, 0xE1, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)

    def lambda_4FE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_4FE)

    def lambda_510():
        OP_8E(0xFE, 0xFFFFF9E8, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_510)
    Sleep(500)

    def lambda_530():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_530)

    def lambda_542():
        OP_8E(0xFE, 0xFFFFF664, 0x0, 0xFFFFF254, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_542)
    WaitChrThread(0x12, 0x1)

    ChrTalk(    #0
        0x13,
        "#1451F#11PAhhh... There's nothing quite like home.\x02",
    )

    CloseMessageWindow()
    OP_43(0x13, 0x3, 0x0, 0x3)
    Sleep(300)
    OP_43(0x12, 0x3, 0x0, 0x4)
    Sleep(100)
    Sleep(500)

    def lambda_5B7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_5B7)

    def lambda_5C9():
        OP_8E(0xFE, 0xFFFFF9E8, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5C9)
    Sleep(500)

    def lambda_5E9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_5E9)

    def lambda_5FB():
        OP_8E(0xFE, 0xFFFFF664, 0x0, 0xFFFFF254, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5FB)
    WaitChrThread(0x107, 0x1)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x13, 0x3)

    ChrTalk(    #1
        0x13,
        "#1450F#5PCan I get some coffee, Dan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x14,
        (
            "#1460F#11POne coffee with plenty of milk and\x01",
            "three sugars coming up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x107,
        "#560F#6POooh! Let me help, too!\x02",
    )

    CloseMessageWindow()

    def lambda_6BE():
        OP_6D(420, 0, 2360, 5500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_6BE)
    OP_43(0x14, 0x3, 0x0, 0x5)
    Sleep(300)
    OP_43(0x107, 0x3, 0x0, 0x6)
    WaitChrThread(0x24, 0x3)
    WaitChrThread(0x107, 0x3)
    Sleep(300)

    ChrTalk(    #4
        0x12,
        (
            "#104F#6PI see you haven't mended your heathen ways.\x02\x03",

            "When are you going to grow up enough to\x01",
            "understand that coffee is best taken black?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x13,
        (
            "#1457F#11PAnd when are you going to understand that there's\x01",
            "nothing worse than an old codger too set in his ways\x01",
            "to appreciate another's tastes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x12,
        (
            "#100F#6PHmph. I'm just telling it like it is.\x02\x03",

            "#100FAdding milk alone completely ruins it, and then\x01",
            "you go and plop three sugars in? You can't even\x01",
            "call that coffee anymore!\x02\x03",

            "#104FOh, poor coffee... What did you ever do to be \x01",
            "blasphemed so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x13,
        "#1459F#11PUgh...\x02",
    )

    CloseMessageWindow()
    OP_22(0x82, 0x0, 0x64)
    Sleep(300)
    OP_82(0x0, 0x0)
    Sleep(500)
    OP_8C(0x14, 225, 400)
    Sleep(100)

    def lambda_947():
        OP_8E(0xFE, 0xFFFFFEE8, 0x0, 0xB0E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_947)
    Sleep(100)
    OP_8C(0x107, 225, 400)
    Sleep(100)

    def lambda_973():
        OP_8E(0xFE, 0xFFFFFB82, 0x0, 0xBD6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_973)
    Sleep(100)
    WaitChrThread(0x14, 0x1)
    OP_8C(0x14, 180, 400)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 180, 400)
    OP_82(0x1, 0x2)

    ChrTalk(    #8
        0x14,
        "#1461F#5PHere's your order, Erika.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x107,
        "#061F#5PDon't let it get cold, now!\x02",
    )

    CloseMessageWindow()
    Fade(350)
    OP_22(0x82, 0x0, 0x64)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -900, 800, 1400, 0)
    Sleep(200)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -1660, 800, 1400, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #10
        0x13,
        (
            "#1832F#11PBah. We'll have to settle this dispute\x01",
            "another time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x12,
        "#101F#6PWell, time to drink up.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)

    ChrTalk(    #12
        0x13,
        "#1457F#2P*sip*\x02",
    )


    ChrTalk(    #13
        0x12,
        "#104F#3P*sip*\x02",
    )

    OP_56(0x1)
    OP_59()
    SetChrFlags(0x107, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x14, 0x4)
    SetChrChipByIndex(0x107, 4)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x12, 5)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x13, 8)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x14, 9)
    SetChrSubChip(0x14, 0)
    SetChrPos(0x107, -2300, 200, 500, 90)
    SetChrPos(0x12, -2300, 200, 1800, 90)
    SetChrPos(0x13, 340, 200, 1610, 270)
    SetChrPos(0x14, 310, 200, 450, 270)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x17, -1700, 800, 150, 0)
    SetChrPos(0x18, -1660, 800, 1400, 0)
    SetChrPos(0x19, -900, 800, 1400, 0)
    SetChrPos(0x1A, -900, 800, 150, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #14
        0x13,
        (
            "#1458F#11PAhhh...\x02\x03",

            "#1450FAnyway...\x02\x03",

            "Where are my souvenirs, Albert?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x12,
        (
            "#103F#6PSouvenirs?\x02\x03",

            "Why would I have any of those for you?\x02\x03",

            "You're the one who's been busy slacking\x01",
            "off abroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x13,
        (
            "#1459F#11PGrrr...\x02\x03",

            "Forget traveling abroad! You were the one who got\x01",
            "to ride on the Arseille with Captain Schwarz!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #17
        0x13,
        (
            "#1830F#2P#3SYou're telling me you had a chance like that and\x01",
            "DIDN'T get me a photograph? Or her handkerchief?\x01",
            "#4SOr even a button off her uniform?!#2S\x02",
        )
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0xC8)
    CloseMessageWindow()

    ChrTalk(    #18
        0x107,
        "#065F#6PWh-Why do you want a button off her uniform?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x14,
        (
            "#1461F#2PYour mother's been a huge fan of her since\x01",
            "the captain's academy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x12,
        (
            "#104F#6PI swear... If you have the time to think about\x01",
            "such worthless nonsense, how about using it\x01",
            "to look over an academic report or two?\x02\x03",

            "It's no wonder all your inventions are half rate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x13,
        (
            "#1457F#11P...Did you just use the words 'useless nonsense'\x01",
            "in reference to Captain Schwarz? Did you DARE\x01",
            "to insult her?\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x13, 0x4)
    SetChrChipByIndex(0x13, 6)
    SetChrSubChip(0x13, 0)

    def lambda_FAF():
        OP_96(0xFE, 0x172, 0x0, 0x9E2, 0xC8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_FAF)
    WaitChrThread(0x13, 0x1)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(300)

    ChrTalk(    #22
        0x12,
        (
            "#101F#6POh, nothing of the sort.\x02\x03",

            "I had plenty of chances to share a few cups of tea\x01",
            "with her on board the Arseille.\x02\x03",

            "#104FShe's a fine woman, if you ask me. She'll go far.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_108E():
        OP_8E(0xFE, 0xFFFFF704, 0x0, 0x9E2, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_108E)
    WaitChrThread(0x13, 0x1)
    SetChrSubChip(0x107, 1)
    OP_8C(0x13, 180, 800)

    def lambda_10BA():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0xBD6, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_10BA)
    SetChrFlags(0x12, 0x20)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)

    def lambda_10E4():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_10E4)

    def lambda_10F2():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0x8FC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_10F2)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    ChrTalk(    #23
        0x13,
        (
            "#1830F#5POh, NOW you've done it!\x02\x03",

            "If you're not going to shut that insolent mouth\x01",
            "of yours, I'm going to do it for you!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x8F, 0x0, 0x64)

    def lambda_119E():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_119E)

    def lambda_11B8():
        OP_95(0xFE, 0x0, 0x12C, 0x0, 0x12C, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_11B8)
    WaitChrThread(0x12, 0x1)
    Sleep(300)
    ClearChrFlags(0x12, 0x20)

    ChrTalk(    #24
        0x12,
        "#101F#12PWhat's that? Is someone jealous?\x02",
    )

    CloseMessageWindow()
    OP_43(0x12, 0x3, 0x0, 0x8)
    Sleep(1000)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)

    def lambda_123C():
        OP_96(0xFE, 0xFFFFF542, 0x0, 0xFFFFFC7C, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_123C)
    WaitChrThread(0x107, 0x1)
    Sleep(300)

    def lambda_1264():
        OP_8E(0xFE, 0xFFFFF2B8, 0x0, 0xFFFFFC7C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1264)
    WaitChrThread(0x107, 0x1)

    def lambda_1284():
        OP_8E(0xFE, 0xFFFFF2B8, 0x0, 0x9C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1284)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 90, 600)
    Sleep(300)

    ChrTalk(    #25
        0x107,
        (
            "#62FWill you two PLEASE stop fighting the second\x01",
            "you start a conversation?!\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_A3(0x1)
    OP_A2(0x0)
    OP_A6(0x1)
    ClearChrFlags(0x14, 0x4)
    SetChrChipByIndex(0x14, 7)
    SetChrSubChip(0x14, 0)
    SetChrPos(0x14, 310, 0, -300, 180)
    OP_22(0x1A, 0x0, 0x64)
    OP_0D()

    def lambda_1347():
        OP_8E(0xFE, 0x136, 0x0, 0xFFFFFC7C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1347)
    WaitChrThread(0x14, 0x1)

    def lambda_1367():
        OP_8E(0xFE, 0xFFFFF344, 0x0, 0xFFFFFC7C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1367)
    WaitChrThread(0x14, 0x1)

    def lambda_1387():
        OP_8E(0xFE, 0xFFFFF344, 0x0, 0x62C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1387)
    WaitChrThread(0x14, 0x1)
    Sleep(300)

    ChrTalk(    #26
        0x14,
        (
            "#1463F#12P...Tita?\x02\x03",

            "What is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #27
        0x107,
        (
            "#066FOh, it's just...\x02\x03",

            "It's just that I finally realized it's kinda nice\x01",
            "to see them fighting like this after all.\x02\x03",

            "#067FMakes it feel like Mom's really home, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14, 90, 300)
    Sleep(300)

    ChrTalk(    #28
        0x14,
        "#1461F#6PYeah. I guess you're right.\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x14)
    Sleep(500)
    TurnDirection(0x14, 0x107, 400)
    Sleep(300)

    ChrTalk(    #29
        0x14,
        (
            "#1460F#12PHey, how would you like to do some shopping?\x02\x03",

            "I'll handle making dinner tonight, so I'll need to\x01",
            "grab a few things.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x14, 400)
    Sleep(300)

    ChrTalk(    #30
        0x107,
        (
            "#064F#5PHuh, really?\x02\x03",

            "#066FThat sounds great. I haven't tasted\x01",
            "your cooking in aaages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x14,
        (
            "#1460F#12PWell, hopefully you'll be able to have it a\x01",
            "lot more from here on.\x02\x03",

            "Neither of us are planning to head out for\x01",
            "work again any time soon, so I'll be taking\x01",
            "over cooking duties for a while.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x107, 90, 400)
    Sleep(800)
    TurnDirection(0x107, 0x14, 400)
    Sleep(300)

    ChrTalk(    #32
        0x107,
        (
            "#560F#5POooh...\x02\x03",

            "#67FI'd love to go shopping with you, then!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x14,
        "#1461F#12PAhaha. Great!\x02",
    )

    CloseMessageWindow()

    def lambda_171A():
        OP_6B(2900, 4000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_171A)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x24, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x12, 0xFF)
    OP_6D(420, 0, 2360, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x107, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x14, 0x4)
    SetChrChipByIndex(0x107, 4)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x12, 5)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x13, 8)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x14, 9)
    SetChrSubChip(0x14, 0)
    SetChrPos(0x107, -2300, 200, 500, 90)
    SetChrPos(0x12, -2300, 200, 1800, 90)
    SetChrPos(0x13, 340, 200, 1610, 270)
    SetChrPos(0x14, 310, 200, 450, 270)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x20, -1700, 800, 150, 0)
    SetChrPos(0x21, -1700, 800, 1400, 0)
    SetChrPos(0x22, -700, 800, 1400, 0)
    SetChrPos(0x23, -700, 800, 150, 0)
    SetChrPos(0x1D, -1100, 800, 850, 0)
    SetChrPos(0x1E, -1070, 800, 1720, 0)
    SetChrPos(0x1F, -1110, 800, 30, 0)
    Sleep(500)

    def lambda_18B6():
        OP_6B(2800, 14000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_18B6)
    FadeToBright(2000, 0)
    OP_0D()
    OP_43(0x107, 0x3, 0x0, 0x9)
    Sleep(2000)
    Sleep(300)
    FadeToDark(300, 0, -106)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #34
        (
            "\x07\x00#40WThat day's dinner was a real feast...\x02\x03",

            "...and for the first time in quite a while, Tita was able\x01",
            "to experience the joy of dining happily with her family.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x00#40WAfter dinner...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    Sleep(1000)
    OP_44(0x107, 0xFF)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3172   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_421 end

    def Function_3_19F4(): pass

    label("Function_3_19F4")


    def lambda_19FA():
        OP_8E(0xFE, 0xFFFFFF4C, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_19FA)
    WaitChrThread(0x13, 0x1)

    def lambda_1A1A():
        OP_8E(0xFE, 0x4F6, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1A1A)
    WaitChrThread(0x13, 0x1)

    def lambda_1A3A():
        OP_8E(0xFE, 0x4F6, 0x0, 0x582, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1A3A)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 270, 400)
    Sleep(300)
    Fade(500)
    SetChrFlags(0x13, 0x4)
    SetChrChipByIndex(0x13, 8)
    SetChrSubChip(0x13, 0)
    SetChrPos(0x13, 340, 200, 1610, 270)
    OP_0D()
    Return()

    # Function_3_19F4 end

    def Function_4_1A87(): pass

    label("Function_4_1A87")


    def lambda_1A8D():
        OP_8E(0xFE, 0xFFFFF2FE, 0x0, 0xFFFFF9D4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1A8D)
    WaitChrThread(0x12, 0x1)

    def lambda_1AAD():
        OP_8E(0xFE, 0xFFFFF2FE, 0x0, 0x582, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1AAD)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 90, 400)
    Sleep(300)
    Fade(500)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 5)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, -2300, 200, 1800, 90)
    OP_0D()
    Return()

    # Function_4_1A87 end

    def Function_5_1AFA(): pass

    label("Function_5_1AFA")


    def lambda_1B00():
        OP_8E(0xFE, 0xFFFFFF4C, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1B00)
    WaitChrThread(0x14, 0x1)

    def lambda_1B20():
        OP_8E(0xFE, 0x4F6, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1B20)
    WaitChrThread(0x14, 0x1)

    def lambda_1B40():
        OP_8E(0xFE, 0x4F6, 0x0, 0x1086, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1B40)
    WaitChrThread(0x14, 0x1)

    def lambda_1B60():
        OP_8E(0xFE, 0x6C2, 0x0, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1B60)
    WaitChrThread(0x14, 0x1)
    OP_8C(0x14, 0, 400)
    Sleep(500)
    OP_22(0x82, 0x0, 0x64)
    Sleep(500)
    LoadEffect(0x0, "map\\mp068_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 1870, 200, 5600, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_22(0x86, 0x0, 0x3C)
    Sleep(2000)
    LoadEffect(0x1, "map\\onsen00.eff")
    PlayEffect(0x1, 0x1, 0xFF, 1320, 1800, 5600, 0, 0, 0, 300, 200, 300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_5_1AFA end

    def Function_6_1C2A(): pass

    label("Function_6_1C2A")


    def lambda_1C30():
        OP_8E(0xFE, 0xFFFFFF4C, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1C30)
    WaitChrThread(0x107, 0x1)

    def lambda_1C50():
        OP_8E(0xFE, 0x4F6, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1C50)
    WaitChrThread(0x107, 0x1)

    def lambda_1C70():
        OP_8E(0xFE, 0x4F6, 0x0, 0x1086, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1C70)
    WaitChrThread(0x107, 0x1)

    def lambda_1C90():
        OP_8E(0xFE, 0x2B2, 0x0, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1C90)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 0, 400)
    Return()

    # Function_6_1C2A end

    def Function_7_1CB2(): pass

    label("Function_7_1CB2")


    ChrTalk(    #36
        0x13,
        (
            "#1451F#2PAhhh... There's nothing quite like home.\x02\x03",

            "#1450FCan I get some coffee, Dan?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #37
        0x14,
        (
            "#1460F#4POne coffee with plenty of milk and\x01",
            "three sugars coming up.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #38
        0x107,
        "#560F#4POooh! Let me help, too!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Return()

    # Function_7_1CB2 end

    def Function_8_1D8A(): pass

    label("Function_8_1D8A")

    ClearChrFlags(0x12, 0x4)

    def lambda_1D95():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1D95)

    def lambda_1DB3():
        OP_8F(0xFE, 0xFFFFF79A, 0x0, 0xE60, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1DB3)
    WaitChrThread(0x13, 0x1)

    label("loc_1DCD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EA1")

    def lambda_1DDC():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0xBA4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1DDC)
    WaitChrThread(0x13, 0x1)
    OP_22(0xD1, 0x0, 0x64)

    def lambda_1E01():
        OP_9E(0xFE, 0xA, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1E01)

    def lambda_1E1B():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0xE60, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1E1B)
    WaitChrThread(0x13, 0x1)

    def lambda_1E3B():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0xBB8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1E3B)
    WaitChrThread(0x12, 0x1)
    OP_22(0xD1, 0x0, 0x64)

    def lambda_1E60():
        OP_9E(0xFE, 0xA, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_1E60)

    def lambda_1E7A():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0x8FC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1E7A)
    WaitChrThread(0x12, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E9E")
    Jump("loc_1EA1")

    label("loc_1E9E")

    Jump("loc_1DCD")

    label("loc_1EA1")


    def lambda_1EA7():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0xBA4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1EA7)
    WaitChrThread(0x13, 0x1)

    def lambda_1EC7():
        OP_9E(0xFE, 0xA, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_1EC7)

    def lambda_1EE1():
        OP_9E(0xFE, 0xA, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1EE1)
    Sleep(1000)

    def lambda_1F00():
        OP_6D(-140, 0, 3800, 5000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_1F00)

    def lambda_1F18():
        OP_67(0, 4700, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1F18)

    def lambda_1F30():
        OP_8F(0xFE, 0xFFFFFF9C, 0x0, 0xF8C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1F30)

    def lambda_1F4B():
        OP_8F(0xFE, 0xFFFFFF9C, 0x0, 0xCE4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1F4B)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x12, 0x1)
    Sleep(1000)
    OP_44(0x13, 0x2)
    OP_44(0x12, 0x2)

    def lambda_1F7D():

        label("loc_1F7D")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_1F7D")

    QueueWorkItem2(0x13, 0, lambda_1F7D)

    def lambda_1F8E():

        label("loc_1F8E")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_1F8E")

    QueueWorkItem2(0x12, 0, lambda_1F8E)
    OP_A2(0x1)

    label("loc_1F9C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_211A")

    def lambda_1FAB():
        OP_8F(0xFE, 0xFFFFFD44, 0x0, 0xE42, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1FAB)

    def lambda_1FC6():
        OP_8F(0xFE, 0x1F4, 0x0, 0xE42, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1FC6)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x12, 0x1)

    def lambda_1FEB():
        OP_8F(0xFE, 0xFFFFFF9C, 0x0, 0xCE4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1FEB)

    def lambda_2006():
        OP_8F(0xFE, 0xFFFFFF9C, 0x0, 0xF8C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2006)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x12, 0x1)

    def lambda_202B():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_202B)

    def lambda_2045():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2045)
    Sleep(1000)

    def lambda_2064():
        OP_8F(0xFE, 0xFFFFFD44, 0x0, 0xE42, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2064)

    def lambda_207F():
        OP_8F(0xFE, 0x1F4, 0x0, 0xE42, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_207F)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x12, 0x1)

    def lambda_20A4():
        OP_8F(0xFE, 0xFFFFFF9C, 0x0, 0xCE4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_20A4)

    def lambda_20BF():
        OP_8F(0xFE, 0xFFFFFF9C, 0x0, 0xF8C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_20BF)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x12, 0x1)

    def lambda_20E4():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_20E4)

    def lambda_20FE():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_20FE)
    Sleep(1000)
    Jump("loc_1F9C")

    label("loc_211A")

    Return()

    # Function_8_1D8A end

    def Function_9_211B(): pass

    label("Function_9_211B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2183")
    OP_62(0x107, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)
    OP_62(0x13, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)
    OP_62(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)
    OP_62(0x14, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)
    Jump("Function_9_211B")

    label("loc_2183")

    Return()

    # Function_9_211B end

    def Function_10_2184(): pass

    label("Function_10_2184")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-3220, 0, -1000, 0)
    OP_67(0, 7300, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 1660, 0, 4750, 0)
    SetChrPos(0x107, -2870, 4000, 5150, 270)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x107, 14)
    SetChrSubChip(0x107, 0)

    def lambda_220F():
        OP_6D(-3220, 0, 2300, 4000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_220F)
    FadeToBright(2000, 0)

    def lambda_2230():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_2230)

    def lambda_2242():
        OP_8E(0xFE, 0xFFFFE890, 0x7D0, 0x141E, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2242)
    WaitChrThread(0x107, 0x1)

    def lambda_2262():
        OP_8E(0xFE, 0xFFFFE890, 0x0, 0x334, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2262)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 90, 400)
    Sleep(500)

    ChrTalk(    #39
        0x107,
        (
            "#1271F#6PUgh... I wasn't planning to sleep in that long...\x02\x03",

            "Morning, Grandpa...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #40
        0x14,
        "Man's Voice",
        "#6PMorning, Tita.\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_2322():
        OP_6D(2380, 0, 6080, 3000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_2322)

    def lambda_233A():
        OP_6B(2960, 3000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_233A)

    def lambda_234A():
        OP_67(0, 4560, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_234A)

    def lambda_2362():
        OP_8E(0xFE, 0xFFFFEE3A, 0x0, 0x334, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2362)
    WaitChrThread(0x107, 0x1)

    def lambda_2382():
        OP_8E(0xFE, 0xFFFFFD80, 0x0, 0x1284, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2382)
    WaitChrThread(0x107, 0x1)

    def lambda_23A2():
        OP_8E(0xFE, 0xA0, 0x0, 0x1284, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_23A2)
    WaitChrThread(0x107, 0x1)
    Sleep(300)

    ChrTalk(    #41
        0x107,
        "#1264F#6P...Huh? Dad?\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #42
        0x107,
        (
            "#1267F#6POh, yeah!\x02\x03",

            "I forgot that you and Mom were back!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x107, 300)
    Sleep(300)

    ChrTalk(    #43
        0x14,
        (
            "#1461F#11PWe sure are! Looks like you had a good\x01",
            "night's sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x107,
        (
            "#1272F#6PY-Yeah...\x02\x03",

            "Sorry... I feel bad for forgetting all about it...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #45
        0x107,
        (
            "#1262F#6POh! Hey!\x02\x03",

            "You said you'd tell me what you were up to\x01",
            "today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x14,
        (
            "#1460F#11PYep. That's still the plan.\x02\x03",

            "You might be better off hearing it from\x01",
            "your mother and grandfather, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x107,
        "#1264F#6PHuh? Why?\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_8C(0x107, 180, 500)
    Sleep(600)
    OP_8C(0x107, 225, 500)
    Sleep(600)
    OP_8C(0x107, 180, 500)
    Sleep(300)

    ChrTalk(    #48
        0x14,
        (
            "#1460F#11PThey were up discussing the issue all night.\x02\x03",

            "They both headed out to the central factory\x01",
            "first thing this morning, so they should be\x01",
            "there as we speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x107,
        "#1262F#5PTh-Thanks! Off I go, then!\x02",
    )

    CloseMessageWindow()

    def lambda_26CD():

        label("loc_26CD")

        TurnDirection(0xFE, 0x107, 500)
        OP_48()
        Jump("loc_26CD")

    QueueWorkItem2(0x14, 2, lambda_26CD)

    def lambda_26DE():
        OP_8E(0xFE, 0xA0, 0x0, 0xE9C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_26DE)
    WaitChrThread(0x107, 0x1)

    ChrTalk(    #50
        0x14,
        "#1463F#5PUmm... Tita?\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(500)
    TurnDirection(0x107, 0x14, 500)
    Sleep(500)

    ChrTalk(    #51
        0x14,
        "#1460F#5PYou might want to have breakfast first.\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #52
        0x107,
        (
            "#1273FWhoops. Forgot that, too...\x02\x03",

            "I haven't washed my face or combed my hair,\x01",
            "either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x14,
        (
            "#1460F#5PAll right. Take care of that first,\x01",
            "then let's get some food in you.\x02\x03",

            "I promise it'll be warm when you\x01",
            "finish up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x107,
        "#1267FThanks, Dad!\x02",
    )

    CloseMessageWindow()
    OP_44(0x14, 0xFF)
    OP_43(0x107, 0x3, 0x0, 0xB)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_2184 end

    def Function_11_28BD(): pass

    label("Function_11_28BD")

    SetChrFlags(0x107, 0x1000)
    OP_8C(0x107, 270, 600)

    def lambda_28CF():
        OP_8E(0xFE, 0xFFFFF8E4, 0x0, 0xE9C, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_28CF)
    WaitChrThread(0x107, 0x1)

    def lambda_28EF():
        OP_8E(0xFE, 0xFFFFED72, 0x0, 0x334, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_28EF)
    WaitChrThread(0x107, 0x1)

    def lambda_290F():
        OP_8E(0xFE, 0xFFFFE890, 0x0, 0x334, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_290F)
    WaitChrThread(0x107, 0x1)

    def lambda_292F():
        OP_8E(0xFE, 0xFFFFE890, 0x7D0, 0x141E, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_292F)
    WaitChrThread(0x107, 0x1)

    def lambda_294F():
        OP_8E(0xFE, 0xFFFFF4CA, 0xFA0, 0x141E, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_294F)
    WaitChrThread(0x107, 0x1)
    Return()

    # Function_11_28BD end

    def Function_12_296A(): pass

    label("Function_12_296A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, 32860, -1000, 4940, 90)
    SetChrPos(0x11, 32659, -1000, 2600, 180)
    LoadEffect(0x1, "monster\\ms31000.eff")
    OP_6D(25620, -1000, 4400, 0)
    OP_67(0, 4680, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(45000, 0)
    OP_6E(300, 0)

    def lambda_2A25():
        OP_6D(34020, -880, 5070, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2A25)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(300)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x2, 0x10, 0, 800, 0, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x3, 0x11, 0, 800, 0, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)

    def lambda_2ACA():
        OP_6B(2700, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2ACA)

    def lambda_2ADA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2ADA)

    def lambda_2AEC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2AEC)
    Sleep(1500)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_82(0x3, 0x2)
    WaitChrThread(0x109, 0x1)
    Sleep(500)
    OP_43(0x10, 0x0, 0x0, 0xD)
    OP_43(0x11, 0x0, 0x0, 0xE)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    OP_62(0x10, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2506)
    NewScene("ED6_DT21/T4122   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_296A end

    def Function_13_2B69(): pass

    label("Function_13_2B69")

    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    Return()

    # Function_13_2B69 end

    def Function_14_2B93(): pass

    label("Function_14_2B93")

    Sleep(800)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 600)
    OP_8C(0xFE, 270, 600)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    Return()

    # Function_14_2B93 end

    SaveToFile()

Try(main)
