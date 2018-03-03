from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2400   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2400.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        'Clem',                                 # 9
        'Jill',                                 # 10
        'Target Camera',                        # 11
        'Chicken',                              # 12
        'Chicken',                              # 13
        'Chicken',                              # 14
        'Gull Seaside Way',                     # 15
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
        'ED6_DT07/CH02590 ._CH',             # 00
        'ED6_DT07/CH02640 ._CH',             # 01
        'ED6_DT07/CH02630 ._CH',             # 02
        'ED6_DT07/CH02570 ._CH',             # 03
        'ED6_DT07/CH02320 ._CH',             # 04
        'ED6_DT06/CH20051 ._CH',             # 05
        'ED6_DT07/CH00040 ._CH',             # 06
        'ED6_DT07/CH00041 ._CH',             # 07
        'ED6_DT07/CH01720 ._CH',             # 08
        'ED6_DT07/CH02390 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH02590P._CP',             # 00
        'ED6_DT07/CH02640P._CP',             # 01
        'ED6_DT07/CH02630P._CP',             # 02
        'ED6_DT07/CH02570P._CP',             # 03
        'ED6_DT07/CH02320P._CP',             # 04
        'ED6_DT06/CH20051P._CP',             # 05
        'ED6_DT07/CH00040P._CP',             # 06
        'ED6_DT07/CH00041P._CP',             # 07
        'ED6_DT07/CH01720P._CP',             # 08
        'ED6_DT07/CH02390P._CP',             # 09
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 22900,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 1060,
        Z                   = 0,
        Y                   = -23220,
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


    ScpFunction(
        "Function_0_1DA",          # 00, 0
        "Function_1_222",          # 01, 1
        "Function_2_223",          # 02, 2
        "Function_3_239",          # 03, 3
        "Function_4_38C",          # 04, 4
        "Function_5_40F",          # 05, 5
        "Function_6_435",          # 06, 6
        "Function_7_C1D",          # 07, 7
        "Function_8_1457",         # 08, 8
        "Function_9_14DC",         # 09, 9
    )


    def Function_0_1DA(): pass

    label("Function_0_1DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_221")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_218")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_203")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 9)
    Jump("loc_215")

    label("loc_203")

    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)

    label("loc_215")

    Jump("loc_221")

    label("loc_218")

    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_221")

    Return()

    # Function_0_1DA end

    def Function_1_222(): pass

    label("Function_1_222")

    Return()

    # Function_1_222 end

    def Function_2_223(): pass

    label("Function_2_223")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_238")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_223")

    label("loc_238")

    Return()

    # Function_2_223 end

    def Function_3_239(): pass

    label("Function_3_239")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)
    OP_8D(0xFE, -8760, 13210, 8700, 24630, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_267")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38B")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_350")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2238), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_PUSH_LONG, 0x339A), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x21FC), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x6036), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_325")
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x0, 0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_312():
        OP_94(0x0, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_312)
    Jump("loc_348")

    label("loc_325")


    def lambda_32B():
        OP_8D(0xFE, -8760, 13210, 8700, 24630, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32B)
    Sleep(200)

    label("loc_348")

    Sleep(30)
    Jump("loc_388")

    label("loc_350")

    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_388")
    OP_44(0xFE, 0x2)

    def lambda_370():
        OP_8D(0xFE, -8760, 13210, 8700, 24630, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_370)

    label("loc_388")

    Jump("loc_267")

    label("loc_38B")

    Return()

    # Function_3_239 end

    def Function_4_38C(): pass

    label("Function_4_38C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40E")
    OP_43(0xFE, 0x2, 0x0, 0x5)
    OP_22(0x191, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x38B, 1)"), scpexpr(EXPR_END)), "loc_40E")
    TalkBegin(0xFE)
    OP_A2(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x8B\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFE)

    label("loc_40E")

    Return()

    # Function_4_38C end

    def Function_5_40F(): pass

    label("Function_5_40F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_42A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_5_40F")

    label("loc_42A")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_40F end

    def Function_6_435(): pass

    label("Function_6_435")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(900, 0, 4660, 0)
    OP_67(0, 4460, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(144000, 0)
    OP_6E(304, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 900, 0, -8600, 0)
    SetChrPos(0x105, -160, 0, -8740, 0)

    def lambda_4AB():
        OP_8E(0xFE, 0x384, 0x0, 0xC80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4AB)

    def lambda_4C6():
        OP_8E(0xFE, 0xFFFFFF60, 0x0, 0xA8C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4C6)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x105, 0x1)
    Sleep(500)

    ChrTalk(    #1
        0x105,
        "#043F#11P...Oh.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0x1)
    TurnDirection(0x10, 0x105, 400)
    OP_62(0x10, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #2
        0x10,
        "#772F#3PHmm? What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x105,
        "#049F#11PWell...\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    FadeToDark(2000, 0, 120)
    OP_0D()
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x18\x07\x0C#40WThe place he led me to was Mercia Orphanage.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x18\x07\x0C#40WIt was somewhere I knew well. Somewhere that was\x01",
            "very important to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "\x18\x07\x0C#40WThat was also exactly why I knew I shouldn't be here. \x01",
            "Because I was so weak willed that I knew I would rely\x01",
            "on everyone here and stop living by myself.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x18\x07\x0C#40WI say that, but this was the first place I wanted to see\x01",
            "as soon as I arrived in Ruan. Oh, how badly I wanted\x01",
            "to run straight here! \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #8
        "\x18\x07\x0C#40WBut I knew I couldn't.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x18\x07\x0C#40WI swore when I joined the academy to walk with my\x01",
            "own two feet, and I would do anything to avoid the\x01",
            "places that would make my resolve buckle.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(2000, 0)
    OP_0D()
    OP_C4(0x1, 0x800)
    OP_62(0x10, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_95(0x10, 0x0, 0x0, 0x0, 0x1F4, 0xFA0)
    OP_95(0x10, 0x0, 0x0, 0x0, 0x1F4, 0xFA0)
    Sleep(300)

    ChrTalk(    #10
        0x10,
        (
            "#774F#3PWhat's up with you? Why'd you go quiet?\x02\x03",

            "#772FYou want me to introduce you to the matron?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #11
        0x105,
        "#049F#11PO-Oh. I'm sorry...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #12
        0x105,
        (
            "#047F#11P(I'm a little stronger than I was before, right?)\x02\x03",

            "(I've gotten used to life at the academy...\x01",
            "I've made friends there.)\x02\x03",

            "(I've resumed practicing my swordsmanship.\x01",
            "I've gained stamina through chasing Lechter\x01",
            "around...)\x02\x03",

            "#042F(Maybe I'm ready to come back here. Maybe\x01",
            "I'm strong enough now.)\x02\x03",

            "(Maybe I can finally walk back inside here with\x01",
            "my head held high and not immediately give in\x01",
            "to the weakness in my heart...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "#775F#3PC'mon, you're scaring me! You're not sick\x01",
            "or nothin', are you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x10, 400)
    Sleep(300)

    ChrTalk(    #14
        0x105,
        (
            "#543F#11PI'm fine.\x02\x03",

            "#542FWould you mind showing me inside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "#771F#3PS-Sure! This way!\x02\x03",

            "#770FKeep up, or I'll leave you behind!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BAF():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_BAF)
    Sleep(200)
    OP_8C(0x105, 0, 400)
    Sleep(100)

    def lambda_BCE():
        OP_8F(0xFE, 0x384, 0x0, 0x3390, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_BCE)
    Sleep(300)

    def lambda_BEE():
        OP_8F(0xFE, 0xFFFFFF60, 0x0, 0x319C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BEE)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T2410   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_435 end

    def Function_7_C1D(): pass

    label("Function_7_C1D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x00#40WThe next day...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x11, 0, 0, -5700, 0)
    SetChrPos(0x105, 100, 0, 34400, 180)
    OP_6D(0, 0, 37440, 0)
    OP_67(0, 8540, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(456, 0)
    OP_1D(0xF)

    def lambda_CD6():
        OP_6D(0, 0, 9920, 12000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_CD6)

    def lambda_CEE():
        OP_6C(315000, 12000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_CEE)
    OP_22(0x1C2, 0x0, 0x64)
    OP_C8(0x200, 0x46, "C_PLAC05._CH", 0x1, 0x7D0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x12, 0x0)
    OP_23(0x1C2)
    Sleep(300)
    Fade(1000)
    OP_6D(-580, 0, 5000, 0)
    OP_67(0, 7540, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    def lambda_D71():
        OP_8E(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_D71)
    WaitChrThread(0x11, 0x1)
    Sleep(500)

    ChrTalk(    #17
        0x11,
        "#1890F#6P...I guess this must be the place?\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #18
        0x11,
        (
            "#644F#6PW-Well, it's not like I have to do anything too\x01",
            "daring today. All I need to do is scope it out\x01",
            "for now!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E5B():
        OP_6D(-2580, 0, 5000, 1200)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_E5B)

    def lambda_E73():
        OP_67(0, 6060, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_E73)

    def lambda_E8B():
        OP_8E(0xFE, 0xFFFFF998, 0x0, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_E8B)
    WaitChrThread(0x11, 0x1)

    def lambda_EAB():
        OP_8E(0xFE, 0xFFFFEF34, 0x0, 0xCE4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_EAB)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 180, 700)
    Sleep(500)

    ChrTalk(    #19
        0x11,
        (
            "#1892F#5P(I know I didn't mean any harm by what I said,\x01",
            "but that's no excuse.)\x02\x03",

            "(I never should've made fun of the kids here\x01",
            "without knowing anything about them.)\x02\x03",

            "#647F...\x02\x03",

            "#1890FWhich is why I'm gonna come here, get to know\x01",
            "more about the place, and then try to apologize\x01",
            "to her. Maybe then she'll forgive me...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)
    Sleep(500)
    OP_8C(0x11, 0, 700)
    Sleep(300)
    OP_95(0x11, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(300)
    OP_8C(0x11, 180, 700)
    Sleep(300)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)
    Sleep(500)

    def lambda_108D():
        OP_8E(0xFE, 0xFFFFF6B4, 0x0, 0x5DC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_108D)
    WaitChrThread(0x11, 0x1)

    def lambda_10AD():
        OP_6D(-1660, 0, 15000, 1500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_10AD)

    def lambda_10C5():
        OP_6E(376, 1500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_10C5)

    def lambda_10D5():
        OP_8E(0xFE, 0xFFFFFB8C, 0x0, 0x5DC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_10D5)
    WaitChrThread(0x11, 0x1)

    def lambda_10F5():
        OP_8E(0xFE, 0xFFFFFB8C, 0x0, 0x2328, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_10F5)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 315, 700)
    Sleep(700)
    OP_8C(0x11, 45, 700)
    Sleep(700)
    OP_8C(0x11, 0, 700)
    Sleep(300)

    ChrTalk(    #20
        0x11,
        (
            "#643F#6PHuh? Looks like there's no one here...\x02\x03",

            "#645FWhew...\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x11, 0x3, 0x0, 0x8)
    Sleep(3000)

    ChrTalk(    #21 op#A op#5
        0x11,
        (
            "#643F#6P#15AWow...\x05\x02\x03",

            "#640F#15AThis place is actually pretty cute.\x02",
        )
    )

    Sleep(7000)
    Fade(1000)
    OP_6D(-2540, 0, 34300, 0)
    OP_67(0, 4740, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(314000, 0)
    OP_6E(376, 0)
    Sleep(1000)
    OP_44(0x11, 0xFF)
    SetChrPos(0x11, 100, 0, 23420, 0)

    def lambda_122E():
        OP_8E(0xFE, 0x64, 0x0, 0x73A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_122E)
    WaitChrThread(0x11, 0x1)
    Sleep(300)

    ChrTalk(    #22
        0x11,
        "#1892F#6PWell...here comes the hard part...\x02",
    )

    CloseMessageWindow()
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_70(0x0, 0x14)
    OP_73(0x0)

    def lambda_1294():
        OP_8E(0xFE, 0xDC, 0x0, 0x7D50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1294)
    WaitChrThread(0x105, 0x1)
    Sleep(500)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #23
        0x105,
        (
            "#044F#11PJill?\x02\x03",

            "What are you doing here?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #24
        0x11,
        (
            "#1891F#6PWh-Wh...#20W Whaaat?!\x02\x03",

            "#641FA-Ahaha... F-Fancy seeing you here, Kloe!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x105,
        (
            "#040F#11PUmm...\x02\x01",

            "#543FDo you want to come in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x11,
        (
            "#643F#6PC-Come in?\x02\x03",

            "#1890FYeah... Okay.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 0, 400)

    def lambda_13EC():
        OP_8E(0xFE, 0x64, 0x0, 0x8660, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_13EC)
    Sleep(400)

    def lambda_140C():
        OP_8E(0xFE, 0x64, 0x0, 0x8660, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_140C)
    Sleep(2500)
    OP_72(0x0, 0x8)
    ExitThread()
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x0, 20)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T2410   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_C1D end

    def Function_8_1457(): pass

    label("Function_8_1457")


    def lambda_145D():
        OP_8E(0xFE, 0xFFFFFF9C, 0x0, 0x2774, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_145D)
    WaitChrThread(0x11, 0x1)

    def lambda_147D():
        OP_8E(0xFE, 0xFFFFFF9C, 0x0, 0x3A98, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_147D)
    WaitChrThread(0x11, 0x1)
    Sleep(300)
    OP_8C(0x11, 315, 700)
    Sleep(700)
    OP_8C(0x11, 45, 700)
    Sleep(700)
    OP_8C(0x11, 0, 700)

    def lambda_14C1():
        OP_8E(0xFE, 0xFFFFFF9C, 0x0, 0x5208, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_14C1)
    WaitChrThread(0x11, 0x1)
    Return()

    # Function_8_1457 end

    def Function_9_14DC(): pass

    label("Function_9_14DC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_11(0xA0, 0xB4, 0xFF, 0xA410, 0x2BF20, 0x0)
    SetChrFlags(0x105, 0x8)
    OP_6D(960, 0, 29820, 0)
    OP_67(0, 17600, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(45000, 0)
    OP_6E(356, 0)
    OP_22(0x1C2, 0x0, 0x64)

    def lambda_1545():
        OP_6B(3000, 25000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_1545)
    FadeToBright(2000, 0)
    OP_0D()
    OP_23(0x1C2)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #27
        "\x07\x0C#40WI'm feeling so sleepy all of a sudden...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #28
        (
            "\x07\x0C#40WThis sunlight does wonders at making you\x01",
            "want to drift off...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x0C#40W...Say...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #30
        (
            "\x07\x0C#40WI wonder if this is how it feels to grasp what's\x01",
            "really important to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #31
        "\x07\x0C#40W...Hmm?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(2000)
    FadeToDark(3800, 16777215, -1)
    OP_0D()
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetChrName("")

    AnonymousTalk(    #32
        (
            "\x18\x07\x0C#40WAll this time, this orphanage was right here.\x01",
            "Same as I remembered it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #33
        (
            "\x18\x07\x0C#40WAll the time I was stubbornly refusing to come\x01",
            "back, all the time I was wrestling with myself\x01",
            "about how I felt...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #34
        (
            "\x18\x07\x0C#40WAll that time, it was right here, waiting for me\x01",
            "to come back.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #35
        "\x18\x07\x0C#40WWhether I was being a hypocrite didn't matter.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #36
        (
            "\x18\x07\x0C#40WI genuinely love this place, and that's the only\x01",
            "thing that ever mattered.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #37
        (
            "\x18\x07\x0C#40WAnd now, I know that I'll always feel that way.\x01",
            "No matter how many times I lose sight of myself\x01",
            "or find myself losing my way...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #38
        (
            "\x18\x07\x0C#40W...I know that I'll always eventually come back\x01",
            "and remember how I feel. This orphanage is just\x01",
            "part of who I am.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(2000)
    SetChrName("")

    AnonymousTalk(    #39
        (
            "\x18\x07\x0C#40WThere was also one other important thing that\x01",
            "I found myself realizing.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #40
        (
            "\x18\x07\x0C#40WI still hadn't thanked him for all he had done\x01",
            "for me. Not once.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    ClearMapFlags(0x10)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapFlags(0x10)
    ClearChrFlags(0x105, 0x8)
    OP_20(0xFA0)
    OP_21()
    Sleep(2000)
    OP_A2(0x2504)
    OP_A2(0x2F6F)
    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_14DC end

    SaveToFile()

Try(main)
