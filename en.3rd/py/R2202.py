from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R2202   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2202.x',
        MapIndex            = 101,
        MapDefaultBGM       = "ed60029",
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
        'Target Camera',                        # 10
        'Ruan',                                 # 11
        'Vista Forest Road',                    # 12
        'Manoria Village',                      # 13
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
        'ED6_DT07/CH00045 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH02590P._CP',             # 00
        'ED6_DT07/CH00045P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = 146110,
        Z                   = -2000,
        Y                   = -272220,
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
        X                   = 195320,
        Z                   = -2000,
        Y                   = -200020,
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
        X                   = 117860,
        Z                   = -1990,
        Y                   = -86810,
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


    DeclActor(
        TriggerX            = 145130,
        TriggerZ            = -2029,
        TriggerY            = -194770,
        TriggerRange        = 1500,
        ActorX              = 145130,
        ActorZ              = -500,
        ActorY              = -194770,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 143160,
        TriggerZ            = -1960,
        TriggerY            = -203990,
        TriggerRange        = 1500,
        ActorX              = 143160,
        ActorZ              = -550,
        ActorY              = -203990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1A2",          # 00, 0
        "Function_1_1B8",          # 01, 1
        "Function_2_1C8",          # 02, 2
        "Function_3_1DE",          # 03, 3
        "Function_4_E73",          # 04, 4
        "Function_5_F45",          # 05, 5
        "Function_6_F56",          # 06, 6
        "Function_7_FAE",          # 07, 7
        "Function_8_1017",         # 08, 8
    )


    def Function_0_1A2(): pass

    label("Function_0_1A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B7")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_1B7")

    Return()

    # Function_0_1A2 end

    def Function_1_1B8(): pass

    label("Function_1_1B8")

    OP_22(0x1C8, 0x1, 0x64)
    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x1900), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_1B8 end

    def Function_2_1C8(): pass

    label("Function_2_1C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_1C8")

    label("loc_1DD")

    Return()

    # Function_2_1C8 end

    def Function_3_1DE(): pass

    label("Function_3_1DE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(137420, -2000, -210960, 0)
    OP_67(0, 5820, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SoundLoad(125)
    LoadEffect(0x0, "map\\mp257_00.eff")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 138720, -2020, -186800, 180)
    SetChrPos(0x105, 137420, -2000, -210960, 0)
    OP_6A(0x105)
    FadeToBright(2000, 0)

    def lambda_276():
        OP_6C(60000, 7500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_276)

    def lambda_286():
        OP_8E(0xFE, 0x218CC, 0xFFFFF830, 0xFFFCEAB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_286)
    WaitChrThread(0x105, 0x1)

    def lambda_2A6():
        OP_8E(0xFE, 0x22AB0, 0xFFFFF830, 0xFFFCF5F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2A6)
    WaitChrThread(0x105, 0x1)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x105, 330, 400)
    Sleep(300)
    OP_6A(0xFF)

    ChrTalk(    #0
        0x105,
        "#044F#11PHmm...?\x02",
    )

    CloseMessageWindow()

    def lambda_302():
        OP_6D(139260, -1500, -187080, 3000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_302)

    def lambda_31A():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_31A)

    def lambda_32A():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_32A)

    def lambda_33A():
        OP_67(0, 5020, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_33A)
    OP_43(0x10, 0x3, 0x0, 0x4)
    WaitChrThread(0x11, 0x0)
    Sleep(4000)
    SetChrPos(0x105, 139620, -2000, -196300, 0)

    def lambda_374():
        OP_8F(0xFE, 0x21D7C, 0xFFFFF830, 0xFFFD1FE8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_374)
    WaitChrThread(0x105, 0x1)
    Sleep(500)

    ChrTalk(    #1
        0x105,
        (
            "#040F#12PIs something wrong?\x02\x03",

            "#044FOh, are you lost?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0x3)
    OP_8C(0x10, 180, 500)

    NpcTalk(    #2
        0x10,
        "Young Boy",
        (
            "#776F#5PN-No! I'm not lost!\x02\x03",

            "#773FI'm just trying to find something!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x105,
        "#044F#12PLike what?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #4
        0x10,
        "Young Boy",
        "#776F#5P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x105,
        (
            "#542F#12PUmm...\x02\x03",

            "#041FI can help you look if you'd like.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x10, 270, 500)
    Sleep(300)

    NpcTalk(    #6
        0x10,
        "Young Boy",
        (
            "#775F#11PY-You don't have to do that...but if you\x01",
            "reeeally wanna...\x02\x03",

            "#773FIt's a red stone. It's really, really pretty.\x02\x03",

            "I'm sure I dropped it somewhere around\x01",
            "here, but I can't find it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x105,
        "#040F#12PA red stone, right?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #8
        0x10,
        "Young Boy",
        (
            "#773F#11PY-Yeah...\x02\x03",

            "I don't get why I haven't found it already...\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x10, 0x3, 0x0, 0x5)
    Sleep(1000)
    OP_8C(0x105, 190, 400)
    Sleep(500)

    def lambda_619():
        OP_8E(0xFE, 0x219A8, 0xFFFFF808, 0xFFFD1BC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_619)
    WaitChrThread(0x105, 0x1)
    Sleep(500)
    OP_8C(0x105, 315, 500)
    Sleep(800)
    OP_8C(0x105, 180, 500)
    Sleep(800)
    OP_8C(0x105, 90, 500)

    def lambda_65D():
        OP_8E(0xFE, 0x223F8, 0xFFFFF808, 0xFFFD1C28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_65D)
    WaitChrThread(0x105, 0x1)
    PlayEffect(0x0, 0x0, 0xFF, 140850, -1500, -189430, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1500)
    OP_22(0x8F, 0x0, 0x64)
    OP_82(0x0, 0x2)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Kloe found a pretty red stone.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)

    def lambda_72B():
        OP_8F(0xFE, 0x22010, 0xFFFFF808, 0xFFFD1C28, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_72B)
    WaitChrThread(0x105, 0x1)

    def lambda_74B():

        label("loc_74B")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_74B")

    QueueWorkItem2(0x105, 2, lambda_74B)
    Sleep(400)

    ChrTalk(    #10
        0x105,
        (
            "#542F#12PExcuse me...\x02\x03",

            "This wouldn't happen to be what\x01",
            "you're looking for, would it?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x10, 0x3)
    OP_62(0x10, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x10, 0x105, 400)

    def lambda_7DD():
        OP_6D(140080, -2000, -187900, 800)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_7DD)

    def lambda_7F5():
        OP_8E(0xFE, 0x21F20, 0xFFFFF81C, 0xFFFD209C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7F5)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 180, 500)
    Sleep(500)
    OP_44(0x105, 0x2)

    NpcTalk(    #11
        0x10,
        "Young Boy",
        "#772F#5PTh-That's it...!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05Kloe handed the boy the stone.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #13
        0x105,
        "#048F#12PPhew! I'm glad we were able to find it.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    NpcTalk(    #14
        0x10,
        "Young Boy",
        (
            "#774F#5PY-Yeah...\x02\x03",

            "#773F...I-I'm... I'm Clem. And...umm...th...nks...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 0, 500)
    Sleep(300)

    ChrTalk(    #15
        0x10,
        "#772F#11P#3SA-Anyway, bye!#2S\x02",
    )

    CloseMessageWindow()

    def lambda_964():
        OP_6D(139990, -2000, -186060, 1500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_964)

    def lambda_97C():
        OP_8F(0xFE, 0x21EBC, 0xFFFFF830, 0xFFFD23D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_97C)
    WaitChrThread(0x10, 0x1)
    OP_22(0x19E, 0x0, 0x64)
    Fade(250)
    ClearChrFlags(0x10, 0x100)
    ClearChrFlags(0x10, 0x1)
    SetChrFlags(0x10, 0x800)
    SetChrFlags(0x10, 0x4)
    OP_D1(16, 20000, 45000, 0, 0)

    def lambda_9CD():
        OP_96(0xFE, 0x22038, 0xFFFFF81C, 0xFFFD2880, 0x1F4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_9CD)
    OP_D1(16, 20000, 45000, 80000, 0)
    WaitChrThread(0x10, 0x1)
    OP_22(0x7D, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    Sleep(1000)
    WaitChrThread(0x105, 0x0)

    def lambda_A23():
        OP_8F(0xFE, 0x21F5C, 0xFFFFF81C, 0xFFFD2254, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A23)
    WaitChrThread(0x105, 0x1)

    ChrTalk(    #16
        0x105,
        "#043F#12PA-Are you all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        "#773F#5PI-I'm okay...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrFlags(0x10, 0x100)
    SetChrFlags(0x10, 0x1)
    ClearChrFlags(0x10, 0x800)
    ClearChrFlags(0x10, 0x4)
    SetChrPos(0x10, 138940, -2020, -185900, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #18
        0x105,
        "#048F#12PI'll escort you back home.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 500)
    Sleep(300)
    OP_62(0x10, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #19
        0x10,
        (
            "#776F#5PI can get home on my own! I'm not some\x01",
            "dumb kid, you know!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #20
        0x105,
        (
            "#542F#12PI know, but you see, I'm a little lost myself.\x02\x03",

            "I was hoping that I might be able to ask\x01",
            "your family for directions.\x02\x03",

            "#041FSo while you might not need my help,\x01",
            "would you be willing to let me go with\x01",
            "you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        (
            "#772F#5PHuh?\x02\x03",

            "#773FO-Oh, then I guess I could. Sure.\x02\x03",

            "#770F...This way!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 0, 600)

    def lambda_C9C():
        OP_6D(140080, -2000, -182900, 800)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_C9C)

    def lambda_CB4():
        OP_8E(0xFE, 0x21B38, 0xFFFFF81C, 0xFFFD35DC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_CB4)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 180, 600)
    OP_95(0x10, 0x0, 0x0, 0x0, 0x1F4, 0xFA0)
    OP_95(0x10, 0x0, 0x0, 0x0, 0x1F4, 0xFA0)

    ChrTalk(    #22
        0x10,
        "#771F#5PCome on! Hurry up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x105,
        (
            "#048F#12PHeehee. I'm coming, I'm coming.\x02\x03",

            "#044F(His house is this way, though?)\x02\x03",

            "(I guess he must be from Manoria...)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DA4():
        OP_8F(0xFE, 0x21750, 0xFFFFF830, 0xFFFD407C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DA4)
    Sleep(1000)
    OP_8C(0x10, 0, 600)

    def lambda_DCB():
        OP_8F(0xFE, 0x216C4, 0xFFFFF81C, 0xFFFD41F8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_DCB)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 180, 600)
    OP_62(0x10, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_95(0x10, 0x0, 0x0, 0x0, 0x1F4, 0xFA0)
    OP_95(0x10, 0x0, 0x0, 0x0, 0x1F4, 0xFA0)
    Sleep(500)
    OP_8C(0x10, 0, 600)

    def lambda_E3E():
        OP_8F(0xFE, 0x20F80, 0xFFFFF81C, 0xFFFD6138, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E3E)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    NewScene("ED6_DT21/T2400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_1DE end

    def Function_4_E73(): pass

    label("Function_4_E73")

    OP_8C(0x10, 280, 500)
    Sleep(800)
    OP_8C(0x10, 90, 500)
    Sleep(500)

    def lambda_E91():
        OP_8E(0xFE, 0x221F0, 0xFFFFF830, 0xFFFD2650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E91)
    WaitChrThread(0x10, 0x1)
    Sleep(500)
    OP_8C(0x10, 120, 500)
    Sleep(800)
    OP_8C(0x10, 0, 500)
    Sleep(800)
    OP_8C(0x10, 270, 500)

    def lambda_ED5():
        OP_8E(0xFE, 0x21958, 0xFFFFF830, 0xFFFD2650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_ED5)
    WaitChrThread(0x10, 0x1)
    Sleep(500)
    OP_8C(0x10, 225, 500)
    Sleep(800)
    OP_8C(0x10, 315, 500)
    Sleep(800)
    OP_8C(0x10, 90, 500)
    Sleep(800)

    def lambda_F1E():
        OP_8E(0xFE, 0x21DE0, 0xFFFFF81C, 0xFFFD2650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_F1E)
    WaitChrThread(0x10, 0x1)
    Sleep(500)
    OP_8C(0x10, 0, 500)
    Return()

    # Function_4_E73 end

    def Function_5_F45(): pass

    label("Function_5_F45")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F55")
    Call(0, 4)
    Jump("Function_5_F45")

    label("loc_F55")

    Return()

    # Function_5_F45 end

    def Function_6_F56(): pass

    label("Function_6_F56")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #24
        "\x07\x05East: Jenis Royal Academy - 252 selge\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_F56 end

    def Function_7_FAE(): pass

    label("Function_7_FAE")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #25
        (
            "\x07\x05South: City of Ruan\x01",
            "North: Manoria Village - 312 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_FAE end

    def Function_8_1017(): pass

    label("Function_8_1017")

    EventBegin(0x1)

    ChrTalk(    #26
        0x101,
        "#1001FThis looks like a good spot to fish.\x02",
    )

    CloseMessageWindow()

    def lambda_104F():
        OP_6D(109750, -6680, -243120, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_104F)

    def lambda_1067():
        OP_6B(3200, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1067)

    def lambda_1077():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_1077)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #27
        "\x07\x05Fish?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F8")
    OP_C0(0xE, 0x17, 0x1AED2, 0xFFFFE5F2, 0xFFFC5180, 0xB4, 0x1AC16, 0xFFFFE958, 0xFFFC406E)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_1107")

    label("loc_10F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1107")
    EventEnd(0x1)

    label("loc_1107")

    Return()

    # Function_8_1017 end

    SaveToFile()

Try(main)
