from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3172   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3172.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Professor Russell',                    # 9
        'Erika',                                # 10
        'Dan',                                  # 11
        'Tita',                                 # 12
        'Object',                               # 13
        'Coffee',                               # 14
        'Coffee',                               # 15
        'Coffee',                               # 16
        'Orbal Gear',                           # 17
        'Target Camera',                        # 18
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
        'ED6_DT07/CH02020 ._CH',             # 00
        'ED6_DT27/CH03970 ._CH',             # 01
        'ED6_DT27/CH03980 ._CH',             # 02
        'ED6_DT07/CH00065 ._CH',             # 03
        'ED6_DT06/CH20021 ._CH',             # 04
        'ED6_DT07/CH00061 ._CH',             # 05
        'ED6_DT26/CH20230 ._CH',             # 06
        'ED6_DT06/CH20020 ._CH',             # 07
        'ED6_DT07/CH02023 ._CH',             # 08
        'ED6_DT26/CH20696 ._CH',             # 09
        'ED6_DT26/CH20697 ._CH',             # 0A
        'ED6_DT07/CH00060 ._CH',             # 0B
        'ED6_DT26/CH20205 ._CH',             # 0C
        'ED6_DT26/CH20757 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH02020P._CP',             # 00
        'ED6_DT27/CH03970P._CP',             # 01
        'ED6_DT27/CH03980P._CP',             # 02
        'ED6_DT07/CH00065P._CP',             # 03
        'ED6_DT06/CH20021P._CP',             # 04
        'ED6_DT07/CH00061P._CP',             # 05
        'ED6_DT26/CH20230P._CP',             # 06
        'ED6_DT06/CH20020P._CP',             # 07
        'ED6_DT07/CH02023P._CP',             # 08
        'ED6_DT26/CH20696P._CP',             # 09
        'ED6_DT26/CH20697P._CP',             # 0A
        'ED6_DT07/CH00060P._CP',             # 0B
        'ED6_DT26/CH20205P._CP',             # 0C
        'ED6_DT26/CH20757P._CP',             # 0D
    )

    DeclNpc(
        X                   = 29950,
        Z                   = -1000,
        Y                   = 8580,
        Direction           = 270,
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
        X                   = 34440,
        Z                   = -1000,
        Y                   = 8630,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1740,
        Z                   = 0,
        Y                   = 4730,
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34310,
        Z                   = -270,
        Y                   = 10390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1179652,
        ChipIndex           = 0x4,
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
        Unknown3            = 1572871,
        ChipIndex           = 0x7,
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
        Unknown3            = 1572871,
        ChipIndex           = 0x7,
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
        Unknown3            = 1572871,
        ChipIndex           = 0x7,
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
        "Function_0_25A",          # 00, 0
        "Function_1_2AE",          # 01, 1
        "Function_2_2DB",          # 02, 2
        "Function_3_2F1",          # 03, 3
        "Function_4_D2A",          # 04, 4
        "Function_5_2AF7",         # 05, 5
        "Function_6_2B38",         # 06, 6
        "Function_7_2C48",         # 07, 7
        "Function_8_2CA9",         # 08, 8
        "Function_9_2CE7",         # 09, 9
        "Function_10_2D4F",        # 0A, 10
        "Function_11_2E09",        # 0B, 11
        "Function_12_2E35",        # 0C, 12
        "Function_13_2E66",        # 0D, 13
        "Function_14_2E97",        # 0E, 14
        "Function_15_3CC1",        # 0F, 15
        "Function_16_3D23",        # 10, 16
    )


    def Function_0_25A(): pass

    label("Function_0_25A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_266")

    label("loc_266")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_28E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_28E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_2AD")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_2AD")

    Return()

    # Function_0_25A end

    def Function_1_2AE(): pass

    label("Function_1_2AE")

    OP_71(0x405, 0x0)
    ExitThread()
    OP_71(0x5, 0x0)
    ExitThread()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D7")
    OP_22(0xC9, 0x0, 0x64)
    Jump("loc_2DA")

    label("loc_2D7")

    OP_23(0xC9)

    label("loc_2DA")

    Return()

    # Function_1_2AE end

    def Function_2_2DB(): pass

    label("Function_2_2DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2DB")

    label("loc_2F0")

    Return()

    # Function_2_2DB end

    def Function_3_2F1(): pass

    label("Function_3_2F1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(32780, -1000, 9320, 0)
    OP_67(0, 4840, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x13, 30000, -1000, 8300, 270)
    SetChrPos(0x11, 30000, -1000, 9340, 270)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, 33900, -1000, 7900, 225)
    SetChrPos(0x10, 32200, -1000, 8140, 180)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x800)
    SetChrPos(0x18, 32940, -1500, 6120, 0)
    SetChrPos(0x106, 30500, -1000, -1500, 0)
    SoundLoad(521)
    SoundLoad(384)
    SoundLoad(383)
    SoundLoad(501)
    SoundLoad(554)
    SoundLoad(130)

    def lambda_3DB():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3DB)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x13,
        (
            "#063F#11PSo that's what it was...\x02\x03",

            "I can't believe I didn't notice that when I was\x01",
            "doing the final checks... This is all my fault...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x11,
        (
            "#1457F#5PWe don't know that for sure yet, Tita.\x02\x03",

            "#1452FLet's not jump to conclusions.\x02\x03",

            "No good comes from blaming yourself\x01",
            "or feeling responsible before we know\x01",
            "if you even had anything to do with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x13,
        (
            "#063F#11PO-Okay...\x02\x03",

            "S-Still...\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x82, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x22A, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #3
        0x106,
        "Young Man's Voice",
        "#1S#1PGaaah!#2S\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #4
        0x106,
        "Young Man's Voice",
        (
            "#1S#1PWh-Where the hell did this hammer come\x01",
            "from?!#2S\x02\x03",

            "#1SWhat wrong with this place...?#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x13, 180, 500)
    Sleep(300)

    ChrTalk(    #5
        0x13,
        "#064F#5PHuh? That sounded like Agate...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 500)
    Sleep(300)

    ChrTalk(    #6
        0x11,
        "#1451F#5PReally? Probably just your imagination.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x13,
        (
            "#064F#5PMaybe...\x02\x03",

            "#067FThat reminds me! He should be here any\x01",
            "minute now.\x02\x03",

            "I'd better go and warm up the food!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x13, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x13, 5)
    SetChrSubChip(0x13, 0)
    OP_8E(0x13, 0x7620, 0xFFFFFC18, 0x15F4, 0x1194, 0x0)

    def lambda_761():
        OP_8E(0xFE, 0x7530, 0xFFFFFC18, 0xE74, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_761)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x13, 0x1)

    def lambda_798():
        OP_8E(0xFE, 0x7850, 0xFFFFFC18, 0xA50, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_798)
    WaitChrThread(0x13, 0x1)

    def lambda_7B8():
        OP_8E(0xFE, 0x7850, 0xFFFFFC18, 0x26C, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_7B8)
    WaitChrThread(0x13, 0x1)

    def lambda_7D8():
        OP_8E(0xFE, 0x5910, 0xFFFFFC18, 0x26C, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_7D8)
    WaitChrThread(0x13, 0x1)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_22(0x7, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x11)
    Sleep(500)
    OP_22(0x82, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x1F5, 0x0, 0x64)
    Sleep(200)
    OP_22(0x1F5, 0x0, 0x64)
    Sleep(200)
    OP_22(0x1F5, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #8
        0x106,
        "Young Man's Voice",
        "#1S#1PWhoa!#2S\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #9
        0x106,
        "Young Man's Voice",
        "#1S#1PWhy'd a bunch of lances pop outta the ground?!#2S\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10, 270, 400)
    Sleep(100)
    OP_8C(0x12, 270, 400)
    Sleep(300)

    ChrTalk(    #10
        0x10,
        (
            "#104F#11PUmm... Erika...\x02\x03",

            "#100FI think lances may have been overdoing\x01",
            "it a tad...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x12,
        (
            "#1465F#11PAt least stick with concealed holes in the\x01",
            "ground, won't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x82, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x17F, 0x0, 0x64)
    Sleep(3600)

    NpcTalk(    #12
        0x106,
        "Young Man's Voice",
        "#1S#1PGaaaaaah!#2S\x02",
    )

    CloseMessageWindow()
    OP_22(0x209, 0x0, 0x64)
    Sleep(1500)
    OP_22(0x180, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #13
        0x12,
        (
            "#1461F#11PUmm... How long are we looking at before\x01",
            "he's able to make it here, might I ask?\x02\x03",

            "I was hoping to take this chance to have a\x01",
            "a man-to-man talk with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        "#1458F#5PHeehee... That, only the Goddess knows.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 45, 400)
    OP_8E(0x11, 0x780A, 0xFFFFFC18, 0x2828, 0x4B0, 0x0)
    Sleep(300)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #15
        0x11,
        (
            "#1456F#5PSeems like he's putting up a good fight.\x02\x03",

            "#1458FBut make no mistake, Agate Crosner...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 500)
    Sleep(300)

    ChrTalk(    #16
        0x11,
        "#1835F#5P#3SOur testing process has only just begun!#2S\x02",
    )

    Fade(500)
    OP_7C(0x0, 0x12C, 0xBB8, 0x190)
    OP_6D(32670, -1000, 10430, 0)
    OP_67(0, 4840, -10000, 0)
    OP_6B(2600, 0)
    CloseMessageWindow()
    OP_C4(0x1, 0x20000000)
    OP_0D()
    Sleep(300)

    def lambda_C27():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_C27)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_F7(0xA, 0x6, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x00Side Story [Orbal Gear Project Part 2] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_E6(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D1A")
    Sleep(1000)
    OP_28(0x2, 0x4, 0x10)
    OP_28(0x2, 0x4, 0x20)
    OP_35(0x6, 0xD4)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "\x07\x05Tita learned the S-Craft\x01",
            "\x07\x02[Orbal Gear]\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_D1A")

    OP_C2(0x1, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_2F1 end

    def Function_4_D2A(): pass

    label("Function_4_D2A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(1840, 0, 5480, 0)
    OP_67(0, 5300, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -170, 0, 4680, 0)
    SetChrPos(0x107, 1750, 0, 4350, 90)
    SetChrPos(0x10, 4500, 0, 2800, 0)
    SetChrChipByIndex(0x107, 12)
    SetChrSubChip(0x107, 0)

    def lambda_DC0():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_DC0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x19, 0x0)
    TurnDirection(0x12, 0x107, 400)
    Sleep(300)

    ChrTalk(    #19
        0x12,
        (
            "#1460F#6PYou can leave the rest to me now, Tita.\x02\x03",

            "You must be tired. Go on to bed.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x12, 500)
    Sleep(300)

    ChrTalk(    #20
        0x107,
        (
            "#1261F#11PI'm fine, honestly. I'm not doing any more than\x01",
            "I usually do.\x02\x03",

            "#1260FI bet you're even more tired than I am, Dad.\x02\x03",

            "You rushed through all the work you had to\x01",
            "get back here as soon as possible, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x12,
        (
            "#1463F#6PW-Well...\x02\x03",

            "#1465FHaha. You've gotten pretty sharp, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x107,
        "#1267F#11PWell, I'm not a kid anymore! I'm thirteen now!\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #23
        0x10,
        "#1PWh-What in Aidios' name...?!\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_FF5():
        OP_6D(5840, 0, 5480, 3000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_FF5)

    def lambda_100D():
        OP_8C(0x107, 90, 500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_100D)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x19, 0xFF)
    WaitChrThread(0x19, 0x0)
    Sleep(800)
    OP_6D(27640, -1000, 10200, 0)
    OP_67(0, 4840, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x10, 30350, -1000, 9550, 225)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 30290, -1000, 8380, 270)
    OP_72(0x405, 0x0)
    ExitThread()
    OP_72(0x5, 0x0)
    ExitThread()

    def lambda_10A4():
        OP_6D(31640, -1000, 10200, 3000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_10A4)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x19, 0x0)
    Sleep(500)

    ChrTalk(    #24
        0x10,
        (
            "#104F#5PWhat part of your daft brain thought you\x01",
            "should start MAKING this?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        (
            "#1457F#11PIt's why we came back here to begin with.\x02\x03",

            "#1452FZCF is the only place around that will allow\x01",
            "me to do so.\x02\x03",

            "That's what I believe, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        "#102F#5PMaybe so, but still...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    SetChrPos(0x107, 23120, 0, 1760, 0)

    ChrTalk(    #27
        0x107,
        "#1264F#5PWhat're you guys arguing about?\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0x7, 0x0, 0x64)
    ClearChrFlags(0x107, 0x8)
    SetChrPos(0x107, 22340, 0, 860, 90)

    def lambda_1249():
        OP_6D(29640, -1000, 8160, 2500)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_1249)

    def lambda_1261():

        label("loc_1261")

        TurnDirection(0xFE, 0x107, 500)
        OP_48()
        Jump("loc_1261")

    QueueWorkItem2(0x11, 2, lambda_1261)

    def lambda_1272():
        OP_8E(0xFE, 0x62FC, 0x0, 0xF14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1272)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0x19, 0x0)

    ChrTalk(    #28
        0x11,
        (
            "#1454F#11POh, are you still awake?\x02\x03",

            "It's past midnight, you know. You should go\x01",
            "and get some rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x107,
        (
            "#1264F#6PWhat are those? Some kind of blueprints?\x02\x03",

            "#1261FCan I see? Please?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1350():
        OP_6D(31640, -1000, 6400, 3800)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_1350)

    def lambda_1368():
        OP_6C(32000, 3800)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1368)

    def lambda_1378():
        OP_8E(0xFE, 0x62FC, 0x0, 0x49C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1378)
    WaitChrThread(0x107, 0x1)

    def lambda_1398():
        OP_8E(0xFE, 0x797C, 0xFFFFFC18, 0x49C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1398)
    Sleep(500)
    OP_44(0x11, 0x2)
    OP_43(0x11, 0x3, 0x0, 0x5)

    def lambda_13C3():

        label("loc_13C3")

        TurnDirection(0xFE, 0x11, 500)
        OP_48()
        Jump("loc_13C3")

    QueueWorkItem2(0x10, 2, lambda_13C3)
    WaitChrThread(0x107, 0x1)

    def lambda_13D9():
        OP_8E(0xFE, 0x797C, 0xFFFFFC18, 0xE74, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_13D9)
    WaitChrThread(0x11, 0x3)

    ChrTalk(    #30
        0x11,
        (
            "#1452F#5PYou didn't get out of the bath that long ago!\x01",
            "You're going to catch a cold hanging around\x01",
            "in here. You should be getting ready for bed.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x1)

    ChrTalk(    #31
        0x107,
        "#1263F#12PAww, but I want to see those blueprints!\x02",
    )

    CloseMessageWindow()
    OP_43(0x107, 0x3, 0x0, 0x6)

    ChrTalk(    #32
        0x107,
        (
            "#1260F#12PWhatever's on them looks reeeally complicated.\x02\x03",

            "That's an orbal engine on the right-hand side,\x01",
            "right?\x02\x03",

            "#1261FIt looks like a compact one, too.\x02\x03",

            "Oh, I know! Is it a new kind of airship? \x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x3)
    Sleep(500)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #33
        0x107,
        "#1265F#12PCome on, Mom! I really wanna seeeeee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x11,
        (
            "#1833F#5POh, boy. Look at you getting all fired up.\x02\x03",

            "You just can't help yourself when it comes\x01",
            "to machinery, can you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x107,
        "#1262F#12PThat's not fair!\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_1698():
        OP_6D(30640, -1000, 6400, 2000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_1698)
    SetChrPos(0x12, 22500, 0, 560, 90)

    def lambda_16C1():
        OP_8E(0xFE, 0x6590, 0x0, 0x424, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_16C1)
    Sleep(500)

    def lambda_16E1():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_16E1)
    Sleep(200)
    OP_22(0x7, 0x0, 0x64)

    def lambda_16F9():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_16F9)
    Sleep(200)

    def lambda_170C():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_170C)
    WaitChrThread(0x12, 0x1)
    Sleep(500)

    ChrTalk(    #36
        0x12,
        (
            "#1460F#6PAll right, I've finished clearing up now.\x02\x03",

            "Shall we get to work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x11,
        (
            "#1451F#11POooh! Perfect timing.\x02\x03",

            "Get our angel to bed, will you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x12,
        "#1465F#6PSure. It IS past her bedtime.\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #39
        0x107,
        "#1265F#3S#11PWhaaat?!\x02",
    )

    OP_7C(0x0, 0x32, 0xBB8, 0x12C)
    CloseMessageWindow()

    def lambda_1816():
        OP_8E(0xFE, 0x797C, 0xFFFFFC18, 0x424, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1816)
    Sleep(500)

    def lambda_1836():

        label("loc_1836")

        TurnDirection(0xFE, 0x12, 500)
        OP_48()
        Jump("loc_1836")

    QueueWorkItem2(0x107, 2, lambda_1836)

    def lambda_1847():

        label("loc_1847")

        TurnDirection(0xFE, 0x12, 500)
        OP_48()
        Jump("loc_1847")

    QueueWorkItem2(0x11, 2, lambda_1847)

    def lambda_1858():

        label("loc_1858")

        TurnDirection(0xFE, 0x12, 500)
        OP_48()
        Jump("loc_1858")

    QueueWorkItem2(0x10, 2, lambda_1858)
    WaitChrThread(0x12, 0x1)

    def lambda_186E():
        OP_8E(0xFE, 0x797C, 0xFFFFFC18, 0xA28, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_186E)
    WaitChrThread(0x12, 0x1)

    ChrTalk(    #40
        0x12,
        "#1460F#12PLet's go, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x107,
        (
            "#1262F#5PLet me have a quick look! Pleeease?\x01",
            "I can go to bed right after that!\x02\x03",

            "I can't work out why that converter's\x01",
            "torque is so low, and it's bugging me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x12,
        (
            "#1465F#12P(...It looks like her obsession's grown by\x01",
            "monstrous proportions since we've been\x01",
            "away.)\x02\x03",

            "#1461FBe as that may be, it's still past your bedtime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x107,
        "#1265F#5PB-But!\x02",
    )

    CloseMessageWindow()
    OP_44(0x107, 0x2)
    OP_44(0x11, 0x2)
    OP_44(0x10, 0x2)

    def lambda_1A10():

        label("loc_1A10")

        TurnDirection(0xFE, 0x107, 500)
        OP_48()
        Jump("loc_1A10")

    QueueWorkItem2(0x11, 2, lambda_1A10)

    def lambda_1A21():

        label("loc_1A21")

        TurnDirection(0xFE, 0x107, 500)
        OP_48()
        Jump("loc_1A21")

    QueueWorkItem2(0x10, 2, lambda_1A21)

    def lambda_1A32():

        label("loc_1A32")

        TurnDirection(0xFE, 0x107, 500)
        OP_48()
        Jump("loc_1A32")

    QueueWorkItem2(0x12, 2, lambda_1A32)

    def lambda_1A43():
        OP_8F(0xFE, 0x7C74, 0xFFFFFC18, 0xE74, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1A43)
    WaitChrThread(0x12, 0x1)
    OP_43(0x12, 0x3, 0x0, 0x7)

    def lambda_1A6A():
        OP_8E(0xFE, 0x797C, 0xFFFFFC18, 0x398, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1A6A)
    WaitChrThread(0x107, 0x1)

    def lambda_1A8A():
        OP_8E(0xFE, 0x5CBC, 0x0, 0x398, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1A8A)
    Sleep(2000)
    OP_43(0x11, 0x3, 0x0, 0x8)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0x12, 0x3)
    OP_44(0x12, 0x2)
    Sleep(500)
    OP_43(0x12, 0x3, 0x0, 0x9)
    Sleep(2000)
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x107)
    Sleep(500)
    OP_8C(0x107, 45, 500)

    def lambda_1AF6():
        OP_6D(31400, -1000, 9740, 2500)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_1AF6)

    def lambda_1B0E():
        OP_6C(45000, 2500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1B0E)
    WaitChrThread(0x19, 0x0)
    WaitChrThread(0x12, 0x3)

    ChrTalk(    #44
        0x11,
        "#1452F#11POkay! Let's start with this unit here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        (
            "#104F#5PEven at a glance, I can tell it's not going to be\x01",
            "easy to make.\x02\x03",

            "#102FWe're best off starting by running a simulation\x01",
            "on it with the Capel before actually attempting\x01",
            "to make the blasted thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x12,
        (
            "#1462F#12PNothing comes to mind that would be strong\x01",
            "enough to build the frame out of, either.\x02\x03",

            "I say we should consider looking into a new\x01",
            "one.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(24920, 0, 2100, 0)
    OP_67(0, 4840, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_43(0x11, 0x3, 0x0, 0xB)
    OP_43(0x10, 0x3, 0x0, 0xC)
    OP_43(0x12, 0x3, 0x0, 0xD)
    Sleep(1000)
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #47
        0x107,
        (
            "#1260F(I wonder what they're talking about.\x01",
            "It all sounds so exciting...)\x02\x03",

            "(Maybe I can scooch closer without them\x01",
            "noticing?)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1DC1():
        OP_6D(26820, 0, 3800, 2400)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_1DC1)

    def lambda_1DD9():
        OP_8E(0xFE, 0x6360, 0x0, 0xA3C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1DD9)
    WaitChrThread(0x107, 0x1)
    Sleep(300)
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x107)
    Sleep(500)

    def lambda_1E1D():
        OP_6D(27220, 0, 5440, 1300)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_1E1D)

    def lambda_1E35():
        OP_8F(0xFE, 0x6360, 0x0, 0xF14, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1E35)
    WaitChrThread(0x107, 0x1)
    OP_44(0x12, 0x3)
    OP_63(0x12)
    Sleep(500)
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_8C(0x12, 225, 500)
    Sleep(300)

    ChrTalk(    #48
        0x12,
        "#1463F#11PTita?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x107,
        "#1271FAww... I shouldn't have pushed my luck.\x02",
    )

    CloseMessageWindow()

    def lambda_1ECC():

        label("loc_1ECC")

        TurnDirection(0xFE, 0x12, 500)
        OP_48()
        Jump("loc_1ECC")

    QueueWorkItem2(0x107, 2, lambda_1ECC)

    def lambda_1EDD():
        OP_8E(0xFE, 0x79E0, 0xFFFFFC18, 0x1874, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1EDD)
    WaitChrThread(0x12, 0x1)

    def lambda_1EFD():
        OP_8E(0xFE, 0x79E0, 0xFFFFFC18, 0x4EC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1EFD)
    WaitChrThread(0x12, 0x1)

    def lambda_1F1D():
        OP_8E(0xFE, 0x639C, 0x0, 0x4EC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1F1D)
    WaitChrThread(0x12, 0x1)

    def lambda_1F3D():
        OP_8E(0xFE, 0x639C, 0x0, 0xA3C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1F3D)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    ChrTalk(    #50
        0x12,
        "#1465F#12PSeriously, now. Go to bed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x107,
        "#1263F#5PBuuut...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x12,
        (
            "#1460F#12PIf you're that curious, I can tell you tomorrow.\x01",
            "But right now, you need sleep.\x02\x03",

            "How does that sound? Good enough?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x107,
        (
            "#1272F#5PBut...\x01",
            "...\x01",
            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #54
        0x107,
        (
            "#1262F#5PThat's a promise, okay?\x02\x03",

            "A PROMISE.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x12,
        "#1461F#12PYes, yes. I promise.\x02",
    )

    CloseMessageWindow()
    OP_44(0x107, 0x2)
    OP_8C(0x107, 225, 400)

    def lambda_20C2():
        OP_8E(0xFE, 0x5820, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_20C2)
    Sleep(500)
    OP_8C(0x12, 225, 400)

    def lambda_20E9():
        OP_8E(0xFE, 0x5820, 0x0, 0xFFFFFEE8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_20E9)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(-1900, 0, 33040, 0)
    OP_67(0, 5300, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_6F(0x7, 20)
    OP_44(0x107, 0xFF)
    OP_44(0x12, 0xFF)
    SetChrFlags(0x107, 0x2)
    SetChrFlags(0x107, 0x4)
    SetChrFlags(0x107, 0x40)
    SetChrPos(0x107, -2180, 200, 31320, 0)
    SetChrChipByIndex(0x107, 6)
    SetChrSubChip(0x107, 10)
    SetChrPos(0x12, -4059, 0, 31660, 90)
    SetChrSubChip(0x12, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #56
        0x107,
        (
            "#1252F#11PI'm not going to let you forget that you promised!\x02\x03",

            "And don't go making whatever it is without me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x12,
        (
            "#1460F#6PI know. We won't.\x02\x03",

            "I promise in the name of the Goddess above\x01",
            "that I'll tell you tomorrow, and that we won't\x01",
            "make it without you.\x02\x03",

            "#1461FAnyway, good night, Tita.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x107,
        "#1250F#11PO-Okay...\x02",
    )

    CloseMessageWindow()
    OP_99(0x107, 0xB, 0x13, 0x320)
    Sleep(1000)

    ChrTalk(    #59
        0x107,
        "#1253F#100W#11PGood...night...\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #60
        0x107,
        "#1253F#100W#11PZzz... Zzz...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrFlags(0x12, 0x4)

    def lambda_2349():
        OP_8E(0xFE, 0xFFFFF1F0, 0x0, 0x7BAC, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2349)
    WaitChrThread(0x12, 0x1)
    Sleep(300)
    OP_22(0x186, 0x0, 0x64)
    OP_70(0x7, 0xC)
    OP_73(0x7)
    Sleep(300)

    def lambda_2382():
        OP_8F(0xFE, 0xFFFFF025, 0x0, 0x7BAC, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2382)
    WaitChrThread(0x12, 0x1)
    ClearChrFlags(0x12, 0x4)
    Sleep(300)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #61
        0x12,
        "#1465F#6P(She takes after her mother in every way.)\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x107, 0x2)
    ClearChrFlags(0x107, 0x4)
    ClearChrFlags(0x107, 0x40)
    SetChrPos(0x107, -6160, 0, 5160, 0)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)
    OP_6D(420, 0, 2360, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x15, -1660, 800, 1400, 0)
    SetChrPos(0x16, -900, 800, 1400, 0)
    SetChrPos(0x17, -900, 800, 150, 0)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrChipByIndex(0x10, 8)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x11, 9)
    SetChrSubChip(0x11, 0)
    SetChrPos(0x10, -2300, 200, 1800, 90)
    SetChrPos(0x11, 340, 200, 1610, 270)
    OP_44(0x10, 0x3)
    OP_63(0x10)
    OP_44(0x11, 0x3)
    OP_63(0x11)
    SetChrPos(0x12, -2870, 4000, 4750, 270)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(300)
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_43(0x12, 0x3, 0x0, 0xA)
    Sleep(1000)
    OP_63(0x10)
    Sleep(100)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #62
        0x10,
        "#104F#6P...Well, that about wraps it up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x11,
        (
            "#1453F#11PThis is amazing...\x02\x03",

            "Ouroboros' technology is even more impressive\x01",
            "than I could've dreamed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10,
        (
            "#100F#6PThat's a fine understatement.\x02\x03",

            "Their technological level's far beyond that of\x01",
            "ours.\x02\x03",

            "#104FThat's true for virtually everything we've seen\x01",
            "of theirs, too--the archaisms, the Gospels,\x01",
            "the Glorious...\x02\x03",

            "I'm not entirely without ideas on how they have\x01",
            "all of it, though.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 0x3)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 10)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, 310, 200, 450, 270)
    Sleep(1000)

    ChrTalk(    #65
        0x10,
        (
            "#100F#6PWhy the sudden questions, anyway?\x02\x03",

            "I've already sent you the info I had\x01",
            "on them before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x12,
        (
            "#1464F#2PThe thing is...\x02\x03",

            "#1462F...we didn't actually learn of them through the\x01",
            "information you sent. We knew of them before\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(300)

    ChrTalk(    #67
        0x10,
        "#103F#6PYou did?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0xC8)
    CloseMessageWindow()

    ChrTalk(    #68
        0x12,
        (
            "#1462F#2PWe haven't actually encountered them or any of\x01",
            "their members, exactly.\x02\x03",

            "But they've been expanding their influence across\x01",
            "the continent for a while now through jaegers and\x01",
            "certain wealthy individuals.\x02\x03",

            "#1464FWe can confirm as much beyond a shadow of a\x01",
            "doubt based on our travels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x11,
        (
            "#1453F#11PThat's why we came back here.\x02\x03",

            "We never imagined they'd be so bold as to try\x01",
            "anything in Liberl, or we would have come back\x01",
            "earlier...\x02\x03",

            "#1452F...but they're not getting any more of a head start\x01",
            "on us. We need to finish this, and we need to do it\x01",
            "as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2ACA():
        OP_6B(2700, 3000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_2ACA)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_D2A end

    def Function_5_2AF7(): pass

    label("Function_5_2AF7")


    def lambda_2AFD():
        OP_8E(0xFE, 0x797C, 0xFFFFFC18, 0x1E50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2AFD)
    WaitChrThread(0x11, 0x1)

    def lambda_2B1D():
        OP_8E(0xFE, 0x797C, 0xFFFFFC18, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2B1D)
    WaitChrThread(0x11, 0x1)
    Return()

    # Function_5_2AF7 end

    def Function_6_2B38(): pass

    label("Function_6_2B38")


    def lambda_2B3E():
        OP_8F(0xFE, 0x7724, 0xFFFFFC18, 0xE74, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2B3E)
    Sleep(300)

    def lambda_2B5E():
        OP_8F(0xFE, 0x7724, 0xFFFFFC18, 0x125C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2B5E)
    WaitChrThread(0x107, 0x1)
    Sleep(1000)

    def lambda_2B83():
        OP_8F(0xFE, 0x797C, 0xFFFFFC18, 0xE74, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2B83)
    Sleep(300)

    def lambda_2BA3():
        OP_8F(0xFE, 0x797C, 0xFFFFFC18, 0x125C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2BA3)
    WaitChrThread(0x107, 0x1)
    Sleep(1000)

    def lambda_2BC8():
        OP_8F(0xFE, 0x7724, 0xFFFFFC18, 0xE74, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2BC8)
    Sleep(300)

    def lambda_2BE8():
        OP_8F(0xFE, 0x7724, 0xFFFFFC18, 0x125C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2BE8)
    WaitChrThread(0x107, 0x1)
    Sleep(1000)

    def lambda_2C0D():
        OP_8F(0xFE, 0x797C, 0xFFFFFC18, 0xE74, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2C0D)
    Sleep(300)

    def lambda_2C2D():
        OP_8F(0xFE, 0x797C, 0xFFFFFC18, 0x125C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2C2D)
    WaitChrThread(0x107, 0x1)
    Return()

    # Function_6_2B38 end

    def Function_7_2C48(): pass

    label("Function_7_2C48")


    def lambda_2C4E():
        OP_8F(0xFE, 0x797C, 0xFFFFFC18, 0xE74, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2C4E)
    WaitChrThread(0x12, 0x1)

    def lambda_2C6E():
        OP_8F(0xFE, 0x797C, 0xFFFFFC18, 0x398, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2C6E)
    WaitChrThread(0x12, 0x1)

    def lambda_2C8E():
        OP_8F(0xFE, 0x6040, 0x0, 0x398, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2C8E)
    WaitChrThread(0x12, 0x1)
    Return()

    # Function_7_2C48 end

    def Function_8_2CA9(): pass

    label("Function_8_2CA9")

    OP_44(0x11, 0x2)
    OP_44(0x10, 0x2)
    OP_8C(0x11, 0, 500)

    def lambda_2CBE():
        OP_8E(0xFE, 0x7652, 0xFFFFFC18, 0x20BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2CBE)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 270, 500)
    OP_8C(0x10, 225, 500)
    Return()

    # Function_8_2CA9 end

    def Function_9_2CE7(): pass

    label("Function_9_2CE7")

    OP_8C(0x12, 90, 500)

    def lambda_2CF4():
        OP_8E(0xFE, 0x797C, 0xFFFFFC18, 0x398, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2CF4)
    WaitChrThread(0x12, 0x1)

    def lambda_2D14():
        OP_8E(0xFE, 0x797C, 0xFFFFFC18, 0x1A2C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2D14)
    WaitChrThread(0x12, 0x1)

    def lambda_2D34():
        OP_8E(0xFE, 0x75F8, 0xFFFFFC18, 0x1C98, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2D34)
    WaitChrThread(0x12, 0x1)
    Return()

    # Function_9_2CE7 end

    def Function_10_2D4F(): pass

    label("Function_10_2D4F")


    def lambda_2D55():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2D55)

    def lambda_2D67():
        OP_8E(0xFE, 0xFFFFE890, 0x7D0, 0x128E, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2D67)
    WaitChrThread(0x12, 0x1)

    def lambda_2D87():
        OP_8E(0xFE, 0xFFFFE890, 0x0, 0x2D0, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2D87)
    WaitChrThread(0x12, 0x1)

    def lambda_2DA7():
        OP_8E(0xFE, 0xFFFFED4A, 0x0, 0xFFFFFD44, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2DA7)
    WaitChrThread(0x12, 0x1)

    def lambda_2DC7():
        OP_8E(0xFE, 0x190, 0x0, 0xFFFFFD44, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2DC7)
    WaitChrThread(0x12, 0x1)

    def lambda_2DE7():
        OP_8E(0xFE, 0x190, 0x0, 0xFFFFFF38, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2DE7)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 270, 500)
    Return()

    # Function_10_2D4F end

    def Function_11_2E09(): pass

    label("Function_11_2E09")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E34")
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Sleep(2000)
    Jump("Function_11_2E09")

    label("loc_2E34")

    Return()

    # Function_11_2E09 end

    def Function_12_2E35(): pass

    label("Function_12_2E35")

    Sleep(1000)

    label("loc_2E3A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E65")
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Sleep(2000)
    Jump("loc_2E3A")

    label("loc_2E65")

    Return()

    # Function_12_2E35 end

    def Function_13_2E66(): pass

    label("Function_13_2E66")

    Sleep(2000)

    label("loc_2E6B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E96")
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Sleep(2000)
    Jump("loc_2E6B")

    label("loc_2E96")

    Return()

    # Function_13_2E66 end

    def Function_14_2E97(): pass

    label("Function_14_2E97")

    EventBegin(0x0)
    Fade(500)
    OP_6D(3170, 500, 36110, 0)
    OP_67(0, 4730, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(45000, 0)
    OP_6E(289, 0)
    SetChrPos(0x107, 1840, 500, 35070, 90)
    OP_0D()
    Sleep(300)
    Sleep(1000)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #70
        0x107,
        (
            "#060FAh, here we are.\x02\x03",

            "...Right.\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x12, 255)
    SetChrPos(0x12, -3950, -1000, 39060, 90)
    OP_8E(0x12, 0xFFFFFA88, 0x0, 0x95B0, 0x7D0, 0x0)
    OP_8C(0x12, 135, 400)

    ChrTalk(    #71
        0x12,
        "#1460F#2PDid you find what you were looking for?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)
    Sleep(300)

    ChrTalk(    #72
        0x107,
        "#060F#2PDad?\x02",
    )

    CloseMessageWindow()

    def lambda_2FC3():
        OP_6D(3150, 0, 36870, 1500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_2FC3)
    OP_8E(0x12, 0x262, 0x1F4, 0x8912, 0x7D0, 0x0)
    OP_8C(0x12, 90, 400)
    WaitChrThread(0x107, 0x0)

    ChrTalk(    #73
        0x107,
        "#060F#2PI thought you needed to watch over the hotpot?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x12,
        (
            "#1460F#6POh, no, I just need to leave it to boil now.\x02\x03",

            "So I thought I'd come and check on you instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x107,
        "#060F#2PM-Me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x12,
        (
            "#1460F#6PWell, you were saying earlier that you wanted to\x01",
            "spend time talking to us.\x02\x03",

            "Didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x107,
        "#060F#2PY-Yeah, I did, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x12,
        (
            "#1460F#6PHearing that really made me think.\x02\x03",

            "I'm pretty blessed to have a daughter who thinks\x01",
            "that about the father who's basically left her\x01",
            "to herself for two whole years...\x02\x03",

            "And a real failure of a father for not being able\x01",
            "to give her what she wants even after finally\x01",
            "coming back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x107,
        (
            "#060F#2PD-Dad...\x02\x03",

            "That's not true at all!\x02\x03",

            "I think this is for the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x12,
        "#1460F#6P...You do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x107,
        (
            "#060F#2PI'm not going to deny that I do kind of wish we \x01",
            "had time to sit and talk after you both being \x01",
            "away for so long...\x02\x03",

            "But being able to work with you, Mom and Grandpa\x01",
            "is just as fun.\x02\x03",

            "This might not be how most families come together,\x01",
            "but it feels like it's how ours does.\x02\x03",

            "Heehee. So I really don't mind at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x12,
        "#1460F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x107,
        "#060F#2P...Wh-What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x12,
        (
            "#1460F#6PN-No, it's nothing. You just took me by surprise,\x01",
            "that's all.\x02\x03",

            "That feels like such an adult thing to say.\x02\x03",

            "*sigh* I really am amazed by just how much you've\x01",
            "grown in the relatively short time we've been away\x01",
            "from home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x107,
        (
            "#060F#2PR-Really?\x02\x03",

            "Well, a lot has happened in the time you've been\x01",
            "away back here, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x12,
        (
            "#1460F#6PHas it, now?\x02\x03",

            "...With Agate, I presume?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x107,
        (
            "#060F#2PWh-What?!\x02\x03",

            "Wh-Why are you bringing him up?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x12,
        (
            "#1460F#6PHaha. I'll take that as a yes, then.\x02\x03",

            "...Is he really important to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x107,
        (
            "#060F#2PWell...\x02\x03",

            "...Yeah, he is.\x02\x03",

            "Mom seems to have him all wrong, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x12,
        (
            "#1460F#6PIt's no surprise that she's concerned about him,\x01",
            "though.\x02\x03",

            "I caused your Mom a whole lot of worries back when\x01",
            "I was a bracer.\x02\x03",

            "She probably doesn't want you to go through the\x01",
            "same thing that she did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x107,
        (
            "#060F#2POh...\x02\x03",

            "S-So that's why...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x12,
        (
            "#1460F#6PJust try and see where she's coming from, if you\x01",
            "can.\x02\x03",

            "Although misunderstandings are best cleared up as\x01",
            "quickly as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x107,
        (
            "#060F#2PY-Yeah...\x02\x03",

            "Still, if I was to invite him over here to do\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x12,
        (
            "#1460F#6P...Yeah, that would be a bad idea.\x02\x03",

            "There's no telling what she'd do if she got angry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x107,
        "#060F#2P...Y-Yeah, you're right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x12,
        (
            "#1460F#6PHmm... This might be difficult...\x02\x03",

            "If only we could find some kind of excuse to get\x01",
            "him to come here that wouldn't cause problems...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x107,
        "#060F#2PWh-What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x12,
        (
            "#1460F#6P...I think I've thought of an idea.\x02\x03",

            "Well, I guess I should go and stir the hotpot a\x01",
            "bit.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A20():
        OP_6D(2500, 0, 37500, 1500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_3A20)

    def lambda_3A38():
        OP_6E(300, 1500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3A38)
    OP_8C(0x12, 315, 400)

    def lambda_3A4F():
        OP_8E(0xFE, 0xFFFFFE3E, 0x0, 0x8F8E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_3A4F)
    Sleep(200)

    ChrTalk(    #99
        0x107,
        "#060F#2PD-Dad?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x12, 0x0)
    Sleep(300)
    OP_8C(0x12, 90, 400)
    Sleep(300)

    ChrTalk(    #100
        0x12,
        (
            "#1460F#6PLeave sorting out the misunderstanding with Agate\x01",
            "to me.\x02\x03",

            "It might take a bit of time, but I think I have\x01",
            "just the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x107,
        "#060F#2PO-Okay, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x12,
        "#1460F#6PWell, I'll see you later at dinner, then.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_3B7E():
        OP_6D(930, 0, 38980, 1500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_3B7E)
    OP_43(0x12, 0x0, 0x0, 0x10)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x107, 0x0)

    def lambda_3BA7():
        OP_6D(2950, 500, 36100, 1500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_3BA7)

    def lambda_3BBF():
        OP_6B(2500, 1500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3BBF)
    WaitChrThread(0x107, 0x0)

    ChrTalk(    #103
        0x107,
        (
            "#060F#5PWhew... That caught me by surprise.\x02\x03",

            "I wasn't expecting him to suddenly bring Agate up\x01",
            "like that...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #104
        0x107,
        "#060F#5PO-Oh, I need to hurry up and deliver this book!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x107, 0x0, 0x0, 0xF)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x250A)
    NewScene("ED6_DT21/T3133   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_2E97 end

    def Function_15_3CC1(): pass

    label("Function_15_3CC1")

    OP_8C(0xFE, 315, 400)
    OP_8E(0xFE, 0xFFFFFB14, 0x0, 0x975E, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFECAA, 0xFFFFF830, 0x97E0, 0x1388, 0x0)

    def lambda_3CF6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CF6)
    OP_8E(0xFE, 0xFFFFE6B0, 0xFFFFF830, 0x9772, 0x1388, 0x0)
    OP_8C(0xFE, 180, 400)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_15_3CC1 end

    def Function_16_3D23(): pass

    label("Function_16_3D23")

    OP_8C(0xFE, 315, 400)
    OP_8E(0xFE, 0xFFFFF813, 0x0, 0x96D2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFECAA, 0xFFFFF830, 0x97E0, 0x7D0, 0x0)

    def lambda_3D58():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D58)
    OP_8E(0xFE, 0xFFFFE6B0, 0xFFFFF830, 0x9772, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_16_3D23 end

    SaveToFile()

Try(main)
